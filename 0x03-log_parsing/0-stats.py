#!/usr/bin/python3
"""
Log Parsing
"""

import sys
import re


def display_statistics(log):
    """
    Display file size and status code statistics
    """
    print("Total file size:", log["file_size"])
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print(f"{code}: {log['code_frequency'][code]}")


if __name__ == "__main__":
    regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

    log = {"file_size": 0, "code_frequency": {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.match(line)
            if match:
                line_count += 1
                status_code = match.group(2)
                file_size = int(match.group(3))

                log["file_size"] += file_size

                if status_code in log["code_frequency"]:
                    log["code_frequency"][status_code] += 1

                if line_count % 10 == 0:
                    display_statistics(log)
    finally:
        display_statistics(log)
