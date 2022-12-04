from aoc.solution import BaseSolution

class DayOneSolution(BaseSolution):
    
    def get_puzzle_day(self):
        return "day1"
    
    def part_one_expected_test_value(self):
        """ Return Part One Expected Test Answer """
        return 24000
        
    def part_two_expected_test_value(self):
        """ Return Part Two Expected Test Answer """
        return 45000
    
    
    def _build_calorie_map(self) -> dict:
        """ Build a dictionary of calories and their associated totals."""
        
        totals = {}
        current_index = 1

        for line in self._get_puzzle_data():
            this_line = line.strip()
            
            if len(this_line) == 0:
                current_index += 1
                continue
                
            if totals.get(current_index) is None:
                totals[current_index] = int(this_line)
            else:
                totals[current_index] = totals[current_index]  + int(this_line)
                
        return totals
    
    def part_one(self):
        """ Return the top elf calories """
        calorie_mapping_per_elf = self._build_calorie_map()
        
        # Sort Map by Values and return top 1 
        top_elf_index = sorted(calorie_mapping_per_elf, key=calorie_mapping_per_elf.get, reverse=True)[:1]
        
        return calorie_mapping_per_elf[top_elf_index[0]]
        
    def part_two(self):
        """ Return the sum of the top 3 elf calories """

        calorie_mapping_per_elf = self._build_calorie_map()
        
        # Sort Map by Values and return top 1 
        top_elf_3_elfs = sorted(calorie_mapping_per_elf, key=calorie_mapping_per_elf.get, reverse=True)[:3]
        
        total_sum_of_calories = 0
        
        for index in top_elf_3_elfs:
            total_sum_of_calories+= calorie_mapping_per_elf[index]
            
        return total_sum_of_calories
    