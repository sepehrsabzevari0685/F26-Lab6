# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Sepehr Sabzevari
# Date: 2026-11-06
# Purpose: Creating dictionary.
# Usage: ./lab6d.py

def times_ten(start_index: int, end_index: int):
    # Keys are start_index..end_index (inclusive), each value is key * 10
    result = {}
    for key in range(start_index, end_index + 1):
        result[key] = key * 10
    return result

def main():
    my_dictionary = times_ten(2, 6)
    print(my_dictionary)

main()
