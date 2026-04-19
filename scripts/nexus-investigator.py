#!/usr/bin/env python3
import sys
import os
import argparse
from playwright.sync_api import sync_playwright

def main():
    parser = argparse.ArgumentParser(description="Nexus Investigator (Persistent Browsing Node)")
    parser.add_argument("url", help="URL to investigate")
    parser.add_argument("--interactive", action="store_true", help="Launch in headful mode to allow manual login")
    args = parser.parse_args()

    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    profile_dir = os.path.join(project_dir, ".agent", "browser_profiles")
    os.makedirs(profile_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=profile_dir,
            headless=not args.interactive
        )
        page = browser.new_page()
        print(f"Investigating {args.url}...")
        page.goto(args.url)
        
        if args.interactive:
            print("Interactive mode active. Please log in or interact with the page if needed.")
            print("Press Enter to continue and save state...")
            input()
            
        content = page.content()
        # In a real scenario, this would parse or extract content robustly
        print(f"Successfully scraped {len(content)} bytes of content.")
        
        browser.close()

if __name__ == "__main__":
    main()
