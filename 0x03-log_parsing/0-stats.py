#!/usr/bin/python3
import sys
import signal

"""
Reads stdin line by line and computes metrics
"""

total_size = 0
status_code_count = {200: 0, 301: 0, 400: 0,
                     401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """
    Print the total file size and count of each status code.
    """
    print("Total file size:", total_size)
    for status_code in sorted(status_code_count.keys()):
        if status_code_count[status_code] > 0:
            print(f"{status_code}: {status_code_count[status_code]}")


def signal_handler(signal, frame):
    """
    Handle the SIGINT signal (Ctrl+C) by printing statistics and exiting.
    """
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) != 7:
            continue

        ip, _, _, status_code, file_size, *_ = parts
        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        if status_code in status_code_count:
            status_code_count[status_code] += 1
            total_size += file_size
            line_count += 1

        if line_count == 10:
            print_statistics()
            line_count = 0

    print_statistics()


except KeyboardInterrupt:
    print_statistics()
