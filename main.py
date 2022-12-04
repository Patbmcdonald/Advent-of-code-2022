import sys
from aoc.enum import SOLUTION_CASES
from aoc.helper import bcolors


def main():

    args = sys.argv[1:]

    if len(args) < 2:
        print(f"{bcolors.FAIL}Invalid Usage.")
        print("Usage: python3 main.py run|test|show_prompt <day1-31>")
        return False
    
    command = args[0]
    day_to_run = args[1]

    try:
            function = SOLUTION_CASES[day_to_run]
    except KeyError:
            print(f"{bcolors.FAIL}Solution for {day_to_run} was not found.")
            print("Usage: python3 main.py run|test|show_prompt <day1-31>")
            return False
            
    if command == "test":
        function().run_test()
    elif command == "show_prompt":
        function().show_prompt()
    elif command == "run":
        function().run_puzzle()
    else:
        print(f"{bcolors.FAIL}Unknown command: {command}")
        print("Usage: python3 main.py run|test|show_prompt <day1-31>")
        
    
if __name__ == "__main__":
    main()