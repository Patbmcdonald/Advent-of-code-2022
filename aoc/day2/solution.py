from aoc.helper import read_lines_to_list
from aoc.solution import BaseSolution

class DayTwoSolution(BaseSolution):
    """ --- Day 2: Rock Paper Scissors ---
    The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

    Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

    Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

    The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

    The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. 
    The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

    For example, suppose you were given the following strategy guide:

    A Y
    B X
    C Z
    
    This strategy guide predicts and recommends the following:

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
    In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
    """
    
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