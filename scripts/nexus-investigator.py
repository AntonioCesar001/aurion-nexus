#!/usr/bin/env python3
"""
Nexus Investigator — Token-Efficient Persistent Browsing Node.

Scrapes web pages using Playwright with persistent browser profiles,
then applies aggressive DOM compression to strip all non-semantic content
(scripts, styles, SVGs, nav, footer, ads) before returning clean text.

This reduces downstream LLM token consumption by 60-80% compared to
feeding raw HTML into the agent context window.
"""

import argparse
import json
import os
import re
import sys
from datetime import UTC, datetime

import structlog

# Configure structlog
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ]
)
log = structlog.get_logger()



def strip_dom_noise(raw_html: str) -> str:
    """Remove non-semantic HTML elements and return dense, clean text.

    Pipeline:
    1. Remove <script>, <style>, <svg>, <noscript>, <iframe> blocks entirely.
    2. Remove all HTML comments.
    3. Remove common ad/analytics containers by class/id heuristics.
    4. Strip all remaining HTML tags but preserve line breaks from block elements.
    5. Collapse excessive whitespace.
    6. Truncate to a safe ceiling (MAX_CHARS) to prevent context overflow.
    """
    max_chars = 15_000  # ~3,750 tokens at 4 chars/token — safe for most LLM windows

    text = raw_html

    # Phase 1: Remove entire blocks of non-content elements
    block_tags = r"script|style|svg|noscript|iframe|object|embed|canvas|video|audio"
    text = re.sub(
        rf"<({block_tags})\b[^>]*>.*?</\1>",
        "",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

    # Phase 2: Remove HTML comments (including conditional IE comments)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    # Phase 3: Remove common non-content containers by class/id patterns
    noise_patterns = [
        r'<(nav|footer|header)\b[^>]*>.*?</\1>',
        r'<[^>]+(class|id)="[^"]*?(cookie|banner|popup|modal|sidebar|newsletter|advert|tracking|analytics)[^"]*?"[^>]*>.*?</\1?>',
    ]
    for pattern in noise_patterns:
        text = re.sub(pattern, "", text, flags=re.DOTALL | re.IGNORECASE)

    # Phase 4: Convert block-level elements to newlines for readability
    text = re.sub(r"<(br|hr|/p|/div|/li|/h[1-6]|/tr|/section|/article)[^>]*>", "\n", text, flags=re.IGNORECASE)

    # Phase 5: Strip all remaining HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Phase 6: Decode common HTML entities
    entity_map = {
        "&amp;": "&", "&lt;": "<", "&gt;": ">",
        "&quot;": '"', "&#39;": "'", "&nbsp;": " ",
        "&mdash;": "—", "&ndash;": "-", "&hellip;": "…",
    }
    for entity, char in entity_map.items():
        text = text.replace(entity, char)

    # Phase 7: Collapse whitespace
    text = re.sub(r"[ \t]+", " ", text)         # horizontal whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)       # vertical whitespace
    text = "\n".join(line.strip() for line in text.splitlines() if line.strip())

    # Phase 8: Truncate to safe ceiling
    if len(text) > max_chars:
        text = text[:max_chars] + "\n\n[... TRUNCATED — content exceeded safe token ceiling ...]"

    return text


def main():
    parser = argparse.ArgumentParser(
        description="Nexus Investigator — Token-Efficient Persistent Browsing Node"
    )
    parser.add_argument("url", help="URL to investigate")
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Launch in headful mode to allow manual login",
    )
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Output raw HTML instead of compressed text (debug only)",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=15_000,
        help="Maximum characters to return (default: 15000 ≈ 3750 tokens)",
    )
    parser.add_argument(
        "--output-json",
        action="store_true",
        help="Output result as structured JSON for pipeline consumption",
    )
    args = parser.parse_args()

    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    profile_dir = os.path.join(project_dir, ".agent", "browser_profiles")
    os.makedirs(profile_dir, exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: Playwright is not installed. Run: pip install playwright && playwright install chromium", file=sys.stderr)
        sys.exit(1)

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=not args.interactive,
        )
        page = browser.new_page()

        log.info("investigating_url", url=args.url)
        page.goto(args.url, wait_until="domcontentloaded", timeout=30_000)


        # Wait briefly for dynamic content
        page.wait_for_timeout(2000)

        if args.interactive:
            print(
                "Interactive mode active. Log in or interact, then press Enter to continue...",
                file=sys.stderr,
            )
            input()

        raw_content = page.content()
        page_title = page.title()
        browser.close()

    # --- Compression Pipeline ---
    compressed = raw_content if args.raw else strip_dom_noise(raw_content)

    if not compressed.strip():
        compressed = "[WARNING] Page content was empty after compression. The page may require JavaScript rendering or login."

    # --- Output ---
    if args.output_json:
        result = {
            "url": args.url,
            "title": page_title,
            "scraped_at": datetime.now(UTC).isoformat(),
            "raw_bytes": len(raw_content),
            "compressed_chars": len(compressed),
            "compression_ratio": f"{(1 - len(compressed) / max(len(raw_content), 1)) * 100:.1f}%",
            "content": compressed,
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        ratio = (1 - len(compressed) / max(len(raw_content), 1)) * 100
        print(f"--- [{page_title}] ---", file=sys.stderr)
        print(f"--- Raw: {len(raw_content)} bytes → Compressed: {len(compressed)} chars ({ratio:.1f}% reduction) ---", file=sys.stderr)
        print(compressed)


if __name__ == "__main__":
    main()
