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
    def get_puzzle_day(self):
        """ The Puzzle Day. """
        pass
    
    def test_part_one(self):
        """ Test Part One """
        return self.part_one() == self.part_one_expected_test_value()
        
    def test_part_two(self):
        """ Test Part Two """
        return self.part_two() == self.part_two_expected_test_value()
    
    def part_one_expected_test_value(self):
        return 0
    
    def part_two_expected_test_value(self):
        return 0
        
    def run_test(self):
        """ Run the two test cases."""
        self.use_test_data = True
        print(f"{bcolors.OKCYAN}Executing {self.get_puzzle_day()} test cases.\n")
        print(f"{bcolors.WARNING}RUNNING Part One Test.")
        
        part_one_solution = self.part_one()
        
        if part_one_solution == self.part_one_expected_test_value() :
            print(f"{bcolors.OKGREEN}PASSED Part One Test.")
        else:
            print(f"{bcolors.FAIL}FAILED Part One Test. Actual: {part_one_solution} Expected: {self.part_one_expected_test_value()}")
        print("\n")

        print(f"{bcolors.WARNING}RUNNING Part Two Test.")
        
        part_two_solution = self.part_two()
        
        if part_two_solution == self.part_two_expected_test_value():
            print(f"{bcolors.OKGREEN}PASSED Part Two Test.")
        else:
            print(f"{bcolors.FAIL}FAILED Part Two Test. Actual: {part_two_solution} Expected: {self.part_two_expected_test_value()}")
        
    def run_puzzle(self):
        """ Run the puzzle solution. """
        prompt = self._get_puzzle_prompt()
        
        if len(prompt) > 0:
            for line in prompt[0]:
                print(f"{bcolors.HEADER}{line}")
            
        print(f"{bcolors.OKGREEN}{self.part_one()}")
        
        if len(prompt) > 0:
            for line in prompt[1]:
                print(f"{bcolors.HEADER}{line}")
        
        print(f"{bcolors.OKGREEN}{self.part_two()}")
        
    def show_prompt(self):
        """ Show the puzzle prompt. """
        prompts = self._get_puzzle_prompt()
        
        for prompt in prompts:
            for line in prompt:
                print(f"{bcolors.HEADER}{line}")

    def _get_test_data(self, overwrite_day:str=None) -> list:
        return read_lines_to_list("./data/test_data/"+overwrite_day+".txt") if overwrite_day  else read_lines_to_list("./data/test_data/"+self.get_puzzle_day()+".txt") 
    
    def _get_puzzle_data(self, overwrite_day:str=None) -> list:
        if self.use_test_data:
            return self._get_test_data(overwrite_day=overwrite_day)
        
        return read_lines_to_list("./data/puzzle_input/"+overwrite_day+".txt") if overwrite_day  else read_lines_to_list("./data/puzzle_input/"+self.get_puzzle_day()+".txt") 
    
    def _get_puzzle_prompt(self, overwrite_day:str=None) -> list:
        temp_lines = read_lines_to_list("./data/prompts/"+overwrite_day+".txt") if overwrite_day  else read_lines_to_list("./data/prompts/"+self.get_puzzle_day()+".txt") 

        try:
            mid_point = temp_lines.index("--- Part Two ---")
        except ValueError:
            return temp_lines
        
        return [temp_lines[:mid_point], temp_lines[mid_point-1:]] 
        