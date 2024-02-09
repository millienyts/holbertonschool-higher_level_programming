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
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
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
    total_size
