import sys
from aoc.enum import SOLUTION_CASES


if len(sys.argv) == 1:
    print("Usage: python3 main.py <day1-31>")
else:
    try:
        function = SOLUTION_CASES[sys.argv[1]]
        function().run()
    except KeyError:
        print(f"Solution for {sys.argv[1]} not found.")
    
    