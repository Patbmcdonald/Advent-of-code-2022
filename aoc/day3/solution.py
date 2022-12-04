from aoc.helper import read_lines_to_list
from aoc.solution import BaseSolution

class DayThreeSolution(BaseSolution):
    
    def get_puzzle_day(self):
        return "day3"
    
    def _get_priority(self, character):
        """ Get Priority for a given character. """
        return ord(character) - 38  if character.isupper() else ord(character) - 96
    
    def _split_ransack(self, line):
        """ Split the line by the mid point and return only common occurances between the two lines."""
        mid_point = len(line) // 2
        return set(line[:mid_point]) & set(line[mid_point:])   
    
    def _group_ransacks_and_get_badge(self, groups):
        """ Use a set to get unique characters then use an & operator to get common occurances first"""
        sets = [set(line) for line in groups]
        duplicates = sets[0]
        
        for this_set in sets[1:]:
            duplicates &= this_set
        
        # head of the list is our badge
        return duplicates.pop()
        
    def part_one(self):
        """ Return the sum of priorities """
        
        total_sum = 0
        for line in self._get_puzzle_data():
            duplicates = self._split_ransack(line.strip())
            total_sum +=  sum([self._get_priority(x) for x in duplicates])
            
        return total_sum
        
    def part_two(self):
        """ Return the sum of 3 groupings """
        
        total_sum = 0
        group = []
        for line in self._get_puzzle_data():
            group.append(line.strip())
            
            if len(group) >= 3:    
                this_badge = self._group_ransacks_and_get_badge(group)
                total_sum +=  self._get_priority(this_badge)
                group.clear()
            
        return total_sum
    
    
    def test_part_one(self):
        """ Test Part One Solution Against Test Data """
        return self.part_one() == 157
        
    def test_part_two(self):
        """ Test Part Two Solution Against Test Data """
        return self.part_two() == 70