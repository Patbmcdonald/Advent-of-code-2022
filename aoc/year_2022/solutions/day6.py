from aoc.solution import BaseSolution

class DaySixSolution(BaseSolution):

    def get_puzzle_day(self):
        return "day6"
    
    def part_one_expected_test_value(self):
        """ Return Part One Expected Test Answer """
        return 7
        
    def part_two_expected_test_value(self):
        """ Return Part Two Expected Test Answer """
        return 19
    
    def get_first_start_of_packet(self, line, size):
        index = 0
        data_packet = ''
        for char in line:
            data_packet = (data_packet + char)[-size:]
            # If our seen packet is euqal to our size due to the set, (removes duolicate characters), we know its the answer
            if len(set(data_packet)) == size:
                return index + 1
            
            index = index + 1
    
    def part_one(self):
        return self.get_first_start_of_packet(self._get_puzzle_data()[0], 4)
        
    def part_two(self):
        return self.get_first_start_of_packet(self._get_puzzle_data()[0], 14)
        