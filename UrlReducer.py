#!/usr/bin/env python3
"""
UrlReducer.py
Aggregates counts per URL from "<url>\t1" lines on STDIN,
and prints only those with total > 5 as: "<url> <count>"
"""
import sys

def flush(url, total):
    # Only output URLs whose total count is > 5
    if url is not None and total > 5:
        # NOTE: space between url and count to match assignment sample
        print(f"{url} {total}")

def main():
    current_url = None
    current_count = 0

    for line in sys.stdin:
        line = line.rstrip("\n")
        if "\t" not in line:
            continue
        url, val = line.split("\t", 1)
        try:
            cnt = int(val)
        except ValueError:
            continue

        if current_url is None:
            current_url, current_count = url, cnt
        elif url == current_url:
            current_count += cnt
        else:
            flush(current_url, current_count)
            current_url, current_count = url, cnt

    # Flush last key
    flush(current_url, current_count)

if __name__ == "__main__":
    main()