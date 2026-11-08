# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Sepehr Sabzevari
# Date: 2026-11-06
# Purpose: Practice Set Operations.
# Usage: ./lab6c.py

def buildtheSet(divisor):
   
    result = set()
    for num in range(0, 101):
        if num % divisor == 0:
            result.add(num)
    return result

def s3_and_s5_not_s7(s3, s5, s7):
   
    in_both = s3.intersection(s5)
    return in_both.difference(s7)

def main():

    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s7 = buildtheSet(7)
    print("s7: ", s7)
    print("----------------------------------------")

    result = s3_and_s5_not_s7(s3, s5, s7)
    print("s3 and s5 but not s7: ", result)

main()
