#!/usr/bin/env python3
import os
import re
from pathlib import Path

WORKSPACE_ROOT = Path("/Users/ton_dev/desenvolvimento/aurion-nexus")
WIKILINK_RE = re.compile(r"\[\[(.*?)\]\]")

def is_false_positive(link):
    # Ignore coordinates, numeric arrays, and dates
    if re.match(r"^[\d\s,\[\]\.-]+$", link):
        return True
    return False

def audit_links(fix=False):
    print(f"🔍 Starting Semantic Integrity Scan in {WORKSPACE_ROOT}...")
    broken_links = []
    scanned_files = 0
    fixed_files = 0

    for root, _, files in os.walk(WORKSPACE_ROOT):
        for file in files:
            if file.endswith(".md"):
                file_path = Path(root) / file
                scanned_files += 1
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                original_content = content
                links = WIKILINK_RE.findall(content)
                broken_in_file = []

                for link in links:
                    if is_false_positive(link):
                        continue
                    
                    target = link.split("|")[0].strip()
                    if target.startswith(("http://", "https://")):
                        continue

                    # Path resolution
                    if target.startswith("/"):
                        target_path = WORKSPACE_ROOT / target.lstrip("/")
                    else:
                        target_path = WORKSPACE_ROOT / target

                    if not target_path.exists():
                        # Try relative to current file
                        rel_target_path = Path(root) / target
                        if not rel_target_path.exists():
                            broken_links.append((file_path.relative_to(WORKSPACE_ROOT), link))
                            broken_in_file.append(link)

                if fix and broken_in_file:
                    for broken in broken_in_file:
                        # Convert [[BrokenLink]] -> BrokenLink 
                        # Or [[BrokenLink|Display]] -> Display
                        replacement = broken.split("|")[-1].strip()
                        content = content.replace(f"[[{broken}]]", replacement)
                    
                    if content != original_content:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(content)
                        fixed_files += 1

    print(f"✅ Scanned {scanned_files} markdown files.")
    if broken_links:
        print(f"⚠️  Found {len(broken_links)} broken links.")
        if fix:
            print(f"🛠️  Auto-Fix applied to {fixed_files} files.")
            return True
        return False
    else:
        print("🟢 All Wikilinks are valid!")
        return True

if __name__ == "__main__":
    import sys
    fix_mode = "--fix" in sys.argv
    success = audit_links(fix=fix_mode)
    sys.exit(0 if (success or fix_mode) else 1)
