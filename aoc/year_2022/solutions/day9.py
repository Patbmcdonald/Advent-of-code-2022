from aoc.solution import BaseSolution

DIRECTIONS = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1),
}

class DayNineSolution(BaseSolution):

    def next_position_of_tail(self, head: tuple, tail: tuple):
        """ Get Next position."""
        x_dist = head[0] - tail[0]
        y_dist = head[1] - tail[1]
        
        # Move the tail if we can move
        if abs(x_dist) > 1 or abs(y_dist) > 1:
            next_x = tail[0] + (0 if x_dist == 0 else x_dist // abs(x_dist))
            next_y = tail[1] + (0 if y_dist == 0 else y_dist // abs(y_dist))
            return (next_x, next_y)
        
        # Tail did not move
        return tail

        
    def move_ropes(self, knot_size:int):
        commands = [line.split(" ") for line in self._get_puzzle_data()]
        moves = [(DIRECTIONS[input[0]], int(input[1])) for input in commands]
        rope = [(0, 0) for _ in range(knot_size)]
        
        # Add starting position 
        tail_visited = {rope[-1]}
        
        for move, dist in moves:
            # Move in our distance 
            for _ in range(dist):
                current_rope = rope[0]
                
                # Next Move
                rope[0] = (current_rope[0] + move[0], current_rope[1] + move[1])
                
                # Move our rope by knot size
                for x in range(1, knot_size):
                    rope[x] = self.next_position_of_tail(rope[x-1], rope[x])
                    
                tail_visited.add(rope[-1])
            
        return len(tail_visited)
    
    
    def get_puzzle_day(self):
        return "day9"
    
    def part_one_expected_test_value(self):
        """ Return Part One Expected Test Answer """
        return 13
        
    def part_two_expected_test_value(self):
        """ Return Part Two Expected Test Answer """
        return 1
    
    def part_one(self):
        return self.move_ropes(2)
        
    def part_two(self):
        return self.move_ropes(10)
        