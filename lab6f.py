# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Sepehr Sabzevari
# Date: 2026-11-06
# Purpose: Use Dictionary for Problem solving.
# Usage: ./lab6f.py

def histogram(text):
   
    counts = {}
    for char in text:
        if char == " ":         
            continue
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

   
    for letter, count in counts.items():
        print(letter, "*" * count)

def main():
    histogram("hello amma")

main()
