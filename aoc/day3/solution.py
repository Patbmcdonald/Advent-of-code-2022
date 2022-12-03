from aoc.helper import read_lines_to_list
from aoc.solution import BaseSolution

class DayThreeSolution(BaseSolution):
    
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
            
        return list(duplicates)[0]
        
    def part_one(self):
        """ Return the sum of priorities """
        
        total_sum = 0
        for line in read_lines_to_list("./inputs/day3.txt"):
            duplicates = self._split_ransack(line.strip())
            total_sum +=  sum([self._get_priority(x) for x in duplicates])
            
        print("sum of the priorities : {}".format(total_sum))
        
    def part_two(self):
        """ Return the sum of 3 groupings """
        
        total_sum = 0
        group = []
        for line in read_lines_to_list("./inputs/day3.txt"):
            group.append(line.strip())
            
            if len(group) >= 3:    
                this_badge = self._group_ransacks_and_get_badge(group)
                total_sum +=  self._get_priority(this_badge)
                group.clear()
            
        print("sum of the priorities : {}".format(total_sum))