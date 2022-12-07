from collections import defaultdict
from aoc.solution import BaseSolution
 
class DaySevenSolution(BaseSolution):

    def get_puzzle_day(self):
        return "day7"
    
    def part_one_expected_test_value(self):
        """ Return Part One Expected Test Answer """
        return 95437
        
    def part_two_expected_test_value(self):
        """ Return Part Two Expected Test Answer """
        return 24933642
    
    def calculate_folder_sizes(self):
        """ Calculate the folder sizes by command."""
        folder_sizes = defaultdict(int)
        current_path = []
        commands = self._get_puzzle_data()
        for line in commands:
            if line.split()[1] in ["dir","ls","cd"]:
                cmd = line.split()[1]

            if cmd == "cd":
                new_dir = line.split().pop()
                if new_dir == "..":
                    current_path.pop()
                elif new_dir == "/":
                    current_path = ["/"]
                else:
                    current_path.append(new_dir)

            else:
                value, name = line.split()
                if value.isnumeric():
                    size = int(value)
                    for i in range(1, len(current_path)+1):
                        pathname = '/'.join(current_path[:i])
                        folder_sizes[pathname] += size               
        
        return folder_sizes
        
    
    def part_one(self):
        folder_sizes = self.calculate_folder_sizes()
        return sum(folder_sizes[folder] for folder in folder_sizes if folder_sizes[folder] <= 100_000)
        
    def part_two(self):
        folder_sizes = self.calculate_folder_sizes()
        to_free = 30_000_000 - (70_000_000 - folder_sizes['/'])
        # filter the files by greater than to_free
        # then sort and the last element is the folder size we would clean up
        smallest_folder =  sorted([folder for folder in folder_sizes if folder_sizes[folder] >= to_free], key=lambda folder: folder_sizes[folder])[0]
        return folder_sizes[smallest_folder]
        