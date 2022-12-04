from aoc.helper import read_lines_to_list, bcolors
from abc import abstractmethod

class BaseSolution:

    use_test_data = False
    
    @abstractmethod
    def part_one(self):
        """ Part One Solution. """
        pass 
    
    @abstractmethod
    def part_two(self):
        """ Part Two Solution. """
        pass
    
    @abstractmethod
    def test_part_one(self):
        """ Part One Test. """
        pass 

    @abstractmethod
    def test_part_two(self):
        """ Part Two Test. """
        pass 
    
    @abstractmethod
    def get_puzzle_day(self):
        """ The Puzzle Day. """
        pass
        
    def run_test(self):
        """ Run the two test cases."""
        self.use_test_data = True
        print(f"{bcolors.OKCYAN}Executing {self.get_puzzle_day()} test cases.\n")
        print(f"{bcolors.WARNING}RUNNING Part One Test.")
        if self.test_part_one():
            print(f"{bcolors.OKGREEN}PASSED Part One Test.")
        else:
            print(f"{bcolors.FAIL}FAILED Part One Test.")
        print("\n")

        print(f"{bcolors.WARNING}RUNNING Part Two Test.")
        if self.test_part_two():
            print(f"{bcolors.OKGREEN}PASSED Part Two Test.")
        else:
            print(f"{bcolors.FAIL}FAILED Part Two Test.")
        
    def run_puzzle(self):
        """ Run the puzzle solution. """
        prompt = self._get_puzzle_prompt()
        
        for line in prompt[0]:
            print(f"{bcolors.HEADER}{line}")
            
        print(f"{bcolors.OKGREEN}{self.part_one()}")
        
        for line in prompt[1]:
            print(f"{bcolors.HEADER}{line}")
        
        print(f"{bcolors.OKGREEN}{self.part_two()}")
        
    def show_prompt(self):
        """ Show the puzzle prompt. """
        prompt = self._get_puzzle_prompt()
        
        for line in prompt[0] + prompt[1]:
            print(f"{bcolors.HEADER}{line}")

    def _get_test_data(self, overwrite_day:str=None) -> list:
        return read_lines_to_list("./data/test_data/"+overwrite_day+".txt") if overwrite_day  else read_lines_to_list("./data/test_data/"+self.get_puzzle_day()+".txt") 
    
    def _get_puzzle_data(self, overwrite_day:str=None) -> list:
        if self.use_test_data:
            return self._get_test_data(overwrite_day=overwrite_day)
        
        return read_lines_to_list("./data/puzzle_input/"+overwrite_day+".txt") if overwrite_day  else read_lines_to_list("./data/puzzle_input/"+self.get_puzzle_day()+".txt") 
    
    def _get_puzzle_prompt(self, overwrite_day:str=None) -> list:
        temp_lines = read_lines_to_list("./data/prompts/"+overwrite_day+".txt") if overwrite_day  else read_lines_to_list("./data/prompts/"+self.get_puzzle_day()+".txt") 

        mid_point = temp_lines.index("--- Part Two ---")
        
        return [temp_lines[:mid_point], temp_lines[mid_point-1:]] 
        