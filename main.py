import sys
from settings import CURRENT_YEAR, SOLUTION_FUNCTIONS
from aoc.helper import bcolors


def main():

    args = sys.argv[1:]

    if len(args) < 2:
        print(f"{bcolors.FAIL}Invalid Usage.")
        print("Usage: python3 main.py run|test|show_prompt <year|defaults-to-current-year> <day1-31>")
        return False
    
    command = args[0]
    year = args[1] if len(args) == 3 else CURRENT_YEAR
    day_to_run = args[1] if len(args) == 2 else args[2]

    try:
            function = SOLUTION_FUNCTIONS[year][day_to_run]
    except KeyError:
            print(f"{bcolors.FAIL}Solution for Year: {year}, Day: {day_to_run} was not found.")
            print("Usage: python3 main.py run|test|show_prompt <year|defaults-to-current-year> <day1-31>")
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