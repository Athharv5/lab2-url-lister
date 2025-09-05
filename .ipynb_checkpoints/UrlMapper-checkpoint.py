import sys
import re
import html

HREF_RE = re.compile(r'href\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)

def main():
    for raw_line in sys.stdin:
        line = html.unescape(raw_line)
        for m in HREF_RE.finditer(line):
            url = m.group(1).strip()
            if url:  
                print(f"{url}\t1")

if __name__ == "__main__":
    main()
