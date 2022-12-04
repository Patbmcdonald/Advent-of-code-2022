from aoc.helper import read_lines_to_list
from aoc.solution import BaseSolution

class DayTwoSolution(BaseSolution):
    
    def __init__(self):
        self.move_types = dict({
                            "Rock" : ["A","X"],
                            "Paper" : ["B","Y"],
                            "Scissors" : ["C","Z"],
                            })
        
    def get_puzzle_day(self):
        return "day2"
        
    def _get_one_round_score(self, opp_move:str, my_move:str):
        """ get Round score """
    
        my_shape_score = 0
        if my_move in self.move_types["Rock"]:
            my_shape_score = 1
        elif my_move in self.move_types["Paper"]:
            my_shape_score = 2
        elif my_move in self.move_types["Scissors"]:
            my_shape_score = 3
            
        # Draw
        if ((opp_move in self.move_types["Rock"] and my_move in self.move_types["Rock"]) or
            (opp_move in self.move_types["Paper"] and my_move in self.move_types["Paper"]) or
            (opp_move in self.move_types["Scissors"] and my_move in self.move_types["Scissors"])):
            return my_shape_score + 3 
        
        # Lost
        if ((opp_move in self.move_types["Paper"] and my_move in self.move_types["Rock"]) or
            (opp_move in self.move_types["Scissors"] and my_move in self.move_types["Paper"]) or
            (opp_move in self.move_types["Rock"] and my_move in self.move_types["Scissors"])):
            return my_shape_score + 0
        
        # won
        if ((my_move in self.move_types["Paper"] and opp_move in self.move_types["Rock"]) or
            (my_move in self.move_types["Scissors"] and opp_move in self.move_types["Paper"]) or
            (my_move in self.move_types["Rock"] and opp_move in self.move_types["Scissors"])):
            return my_shape_score + 6
    
    def _get_move_change(self, opp_move:str, my_move:str):
        """X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"""
    
        if my_move in self.move_types["Rock"]: # Lost
            if opp_move in self.move_types["Rock"]:
                return self.move_types["Scissors"][1]
            elif opp_move in self.move_types["Scissors"]:
                return self.move_types["Paper"][1]
            elif opp_move in self.move_types["Paper"]:
                return self.move_types["Rock"][1]

        elif my_move in self.move_types["Paper"]: # Draw
            if opp_move in self.move_types["Rock"]:
                return self.move_types["Rock"][1]
            elif opp_move in self.move_types["Scissors"]:
                return self.move_types["Scissors"][1]
            elif opp_move in self.move_types["Paper"]:
                return self.move_types["Paper"][1]

        elif my_move in self.move_types["Scissors"]: # Win
            if opp_move in self.move_types["Rock"]:
                return self.move_types["Paper"][1]
            elif opp_move in self.move_types["Scissors"]:
                return self.move_types["Rock"][1]
            elif opp_move in self.move_types["Paper"]:
                return self.move_types["Scissors"][1]

    def part_one(self):
        """ Return total round score """
        
        total_score = 0
        for line in self._get_puzzle_data():
            this_line = line.strip()
            moves = this_line.split(" ")
            
            total_score += self._get_one_round_score(moves[0], moves[1])
            
        return total_score
        
    def part_two(self):
        """ Return total round score when I adjust my move """
        
        total_score = 0
        for line in self._get_puzzle_data():
            this_line = line.strip()
            moves = this_line.split(" ")
            
            # Adjust My Move
            new_move = self._get_move_change(moves[0], moves[1])
            
            total_score += self._get_one_round_score(moves[0], new_move)
            
        return total_score
    
    def test_part_one(self):
        """ Test Part One Solution Against Test Data """
        return self.part_one() == 15
        
    def test_part_two(self):
        """ Test Part Two Solution Against Test Data """
        return self.part_two() == 12