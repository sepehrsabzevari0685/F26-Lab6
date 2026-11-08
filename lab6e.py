# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Sepehr Sabzevari
# Date: 2026-11-06
# Purpose: Traverse dictionary.
# Usage: ./lab6e.py

my_dict = {"switzerland" : "Alps", "United States" : "Alska Range", "Armenia" : "Caucasus", "Argentina" : "Andes", "Karakoram" : "Pakistan"}

# items() gives back each (key, value) pair, which we unpack into two variables
for key, value in my_dict.items():
    print(f"{key} : {value}")
