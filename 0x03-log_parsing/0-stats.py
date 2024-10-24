#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:
"""
import sys
import signal
import re

# Initialize variables
total_file_size = 0
status_code_count = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
        }
line_count = 0

# Regular expression to match the expected log format
log_pattern = re.compile(
    r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

def print_matrices():
    """
    After every 10 lines and/or a keyboard interruption (CTRL + C)
    print these statistics from the beginning:
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code} {status_code_count[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C) and print metrics"""
    print_metrices()
    sys.exit(0)

# Register signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # remove white space at the beginning and end
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            # Extract the file size and status code
            status_code = match.group(3)
            file_size = int(match.group(4))

            # Update the total file size
            total_file_size += file_size

            # Update status count if it is valid
            if status_code in status_code_count:
                status_code_count[status_code] += 1

            line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_matrices()

except Exception:
    pass

finally:
    # Print the final metrics if exiting
    print_metrices()
