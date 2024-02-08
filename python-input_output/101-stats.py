#!/usr/bin/python3
"""
Log Parsing Module
"""
import sys

def print_metrics(total_size, status_codes):
    """
    Print the metrics calculated so far
    """
    print("File size: {}".format(total_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    """
    Parse a single log line and update metrics
    """
    parts = line.split(" ")
    if len(parts) < 9:
        return None, None
    status_code = parts[-2]
    file_size = int(parts[-1])
    return status_code, file_size

def main():
    """
    Main function to read stdin and compute metrics
    """
    count = 0
    total_size = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            count += 1
            status_code, file_size = parse_line(line)
            if status_code is None or file_size is None:
                continue
            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
