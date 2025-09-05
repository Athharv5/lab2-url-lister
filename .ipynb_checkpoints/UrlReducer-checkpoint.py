import sys

def flush(url, total):
    if url is not None and total > 5:
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

    flush(current_url, current_count)

if __name__ == "__main__":
    main()