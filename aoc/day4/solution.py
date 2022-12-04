from aoc.solution import BaseSolution

class DayFourSolution(BaseSolution):

    def get_puzzle_day(self):
        return "day4"
    
    def part_one(self):
        
        counter = 0
        for line in self._get_puzzle_data():
            pairings = line.split(",")
            
            first = self._fill_range(pairings[0])
            second = self._fill_range(pairings[1])

            # Get Union
            overlaps = first & second
            
            # If Overlaps equals either first or second, then we consumed one totally.
            if overlaps == first or overlaps == second:
                counter += 1
            
        return counter
        
    def _fill_range(self, pair):
        """ Fill in elfs based on range """
        pairing = pair.split("-")
        start = int(pairing[0])
        end = int(pairing[1])
        overlaps = set()
        for i in range(start, end + 1):
            overlaps.add(i)
            
        return overlaps
      
    def part_two(self):
        counter = 0
        for line in self._get_puzzle_data():
            pairings = line.split(",")
            
            first = self._fill_range(pairings[0])
            second = self._fill_range(pairings[1])

            overlaps = first & second
            
            if len(overlaps) > 0:
                counter += 1
            
        return counter
    
    def test_part_one(self):
        return self.part_one() == 2
        
    def test_part_two(self):
        return self.part_two() == 4
        