from aoc.solution import BaseSolution

class DayFourSolution(BaseSolution):

    def get_puzzle_day(self):
        return "day4"
    
    def part_one_expected_test_value(self):
        """ Return Part One Expected Test Answer """
        return 2
        
    def part_two_expected_test_value(self):
        """ Return Part Two Expected Test Answer """
        return 4
    
    def _fill_pairing_range(self, pair):
        """ We need to fill a set with our start - end """
        this_range = pair.split("-")
        start = int(this_range[0])
        end = int(this_range[1])
        pairing_range = set()
        
        # Add Start to End + 1 for our 
        for i in range(start, end + 1):
            pairing_range.add(i)
            
        return pairing_range
    
    def part_one(self):
        """ We want to find the assignment pairs where one range fully contain the other
            we can do this by filling a set with start to end and unioning the set ^^ 
        """
        counter = 0
        for line in self._get_puzzle_data():
            
            this_pairing = line.split(",")
            
            first_pairing = self._fill_pairing_range(this_pairing[0])
            second_pairing = self._fill_pairing_range(this_pairing[1])

            # Intersection
            overlapping_pairings = first_pairing & second_pairing
            
            # If overlapping_pairings equals either first or second, then we consumed one totally.
            if overlapping_pairings == first_pairing or overlapping_pairings == second_pairing:
                counter += 1
            
        return counter
        
    def part_two(self):
        """ 
        We want to find  any overlapping_pairings ^^, same as part one, change if statement ^^ 
        """
        counter = 0
        for line in self._get_puzzle_data():
            
            this_pairing = line.split(",")
            
            first_pairing = self._fill_pairing_range(this_pairing[0])
            second_pairing = self._fill_pairing_range(this_pairing[1])

            # Intersection
            overlapping_pairings = first_pairing & second_pairing
            
            if len(overlapping_pairings) > 0:
                counter += 1
            
        return counter
        