#!/usr/bin/env python3
"""
UrlMapper.py
Reads lines from STDIN, extracts every href="..." or href='...'
and emits: <url>\t1
"""
import sys
import re
import html

# Match quoted href values (double or single quotes), case-insensitive.
HREF_RE = re.compile(r'href\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)

def main():
    for raw_line in sys.stdin:
        # Normalize HTML entities like &quot;
        line = html.unescape(raw_line)
        # Find all href="..."/href='...'
        for m in HREF_RE.finditer(line):
            url = m.group(1).strip()
            if url:  # skip empty
                # Hadoop streaming expects: key \t value
                print(f"{url}\t1")

if __name__ == "__main__":
    main()
