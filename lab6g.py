# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Sepehr Sabzevari
# Date: 2026-11-06
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6g.py

def add_movie(database, name, director, year, runtime):
   
    movie = {"name": name, "director": director, "year": year, "runtime": runtime}
    database.append(movie)

def main():
    database = []

    add_movie(database, "Gone with the Wind", "Victor Fleming", 1939, 238)
    add_movie(database, "Forever Gone", "Jane Smith", 2020, 95)
    add_movie(database, "Inception", "Christopher Nolan", 2010, 148)
    add_movie(database, "The Dark Knight", "Christopher Nolan", 2008, 152)

   
    for movie in database:
        print(movie)

main()
