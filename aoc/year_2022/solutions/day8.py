from functools import reduce
from aoc.solution import BaseSolution

class DayEightSolution(BaseSolution):

    def get_puzzle_day(self):
        return "day8"
    
    def part_one_expected_test_value(self):
        """ Return Part One Expected Test Answer """
        return 21
        
    def part_two_expected_test_value(self):
        """ Return Part Two Expected Test Answer """
        return 8
    
    def part_one(self):
        
        trees = self._generate_tree()
        max_x = len(trees[0]) - 1
        max_y = len(trees) - 1
        visible_edges = 0
        
        self._print_grid(trees)
        
        # Treverse our grid skipping the outter edges
        for y in range(1, max_y):
            for x in range(1, max_x):
                current = trees[y][x]
                
                left = [trees[y][i] for i in range(0, x)]
                right = [trees[y][i] for i in range(x + 1, max_x + 1)]
                top = [trees[i][x] for i in range(0, y)]
                bottom = [trees[i][x] for i in range(y + 1, max_y + 1)]
                
                if max(left) < current:
                    visible_edges += 1
                elif max(right) < current:
                    visible_edges += 1
                elif max(top) < current:
                    visible_edges += 1
                elif max(bottom) < current:
                    visible_edges += 1
        # Add visiable edges with our outter edges  
        return visible_edges + ((max_x * 2) + (max_y * 2))
        
    def part_two(self):
        
        trees = self._generate_tree()
        max_x = len(trees[0]) - 1
        max_y = len(trees) - 1
        self._print_grid(trees)
        
        scenic_scores = []
        
        for y in range(1, max_x):
            for x in range(1, max_y):
                current = trees[y][x]
                
                left = [trees[y][i] for i in range(0, x)]
                right = [trees[y][i] for i in range(x + 1, max_x + 1)]
                top = [trees[i][x] for i in range(0, y)]
                bottom = [trees[i][x] for i in range(y + 1, max_y + 1)]

                # Search the whole tree per and calculte our score for each view
                scores = list(filter(lambda x: x > 0, [
                    self.get_blocked_view(current, reversed(left)), #reverse 
                    self.get_blocked_view(current, right),
                    self.get_blocked_view(current, reversed(top)), # Reverse
                    self.get_blocked_view(current, bottom)
                ]))

                scenic_scores.append(reduce(lambda a, b: a * b, scores))
                
        return max(scenic_scores)
    
    def _print_grid(self, tree):
        """ Print the grid. """
        for x in range(len(tree)):
            for y in range(len(tree[0])):
                print(tree[x][y],end="")
                
            print()

    def get_blocked_view(self, current, trees):
        """ Get the blocked view counts for our current tree."""
        count = 0
        for tree in trees:
            if tree < current: count += 1
            else: count += 1; break
        
        return count
    
    
    def _generate_tree(self):
        """ Generate our tree """
        
        tree = list()
        
        for line in self._get_puzzle_data():
            tree.append(list(line))
        
        return tree
