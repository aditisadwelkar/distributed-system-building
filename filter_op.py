#!/usr/bin/env python3
"""
RainStorm Filter Operator
Filters lines that contain a specified pattern (case-sensitive).

Usage: ./filter_op.py <pattern>
Input via stdin: key<TAB>value
Output to stdout: key<TAB>value (only if pattern in value)
"""
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: filter_op.py <pattern>", file=sys.stderr)
        sys.exit(1)
    
    pattern = sys.argv[1]
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        # Parse key<TAB>value format
        parts = line.split('\t', 1)
        if len(parts) == 2:
            key, value = parts
        else:
            key = ""
            value = line
        
        # Case-sensitive pattern matching
        if pattern in value:
            print(f"{key}\t{value}")


if __name__ == '__main__':
    main()
