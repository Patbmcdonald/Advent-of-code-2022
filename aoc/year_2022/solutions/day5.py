from aoc.solution import BaseSolution

class DayFiveSolution(BaseSolution):
    
    def get_puzzle_day(self):
        return "day5"
    
    def _parse_input(self):
        input_reader = self._get_puzzle_input_reader()

        # get the crates on the ship
        crates = []
        line = ' '
        
        # Parse the puzzle file, we need to split
        #        [D]      
        #    [N] [C]    
        #    [Z] [M] [P]
        #    1   2   3 
        #
        # move 1 from 2 to 1
        
        while line:

            # get the line
            line = input_reader.readline().rstrip()

            # check for empty line
            if not line:
                break
            
            # split the line by groups of 3 
            line = list(line[1::4])
            
            crates.append(line)

        # restructure the crates
        tmp = [[] for _ in range(len(crates[-1]))]
        
        for line in crates[:-1]:
            for idx in range(len(line)):
                element = line[idx]
                if element != ' ':
                    tmp[idx].append(element)
        # reverse to build the stack           
        crates = [list(reversed(stack)) for stack in tmp]

        # get the commands
        instructions = []
        # Read the rest 
        for line in input_reader.readlines():
            line = line.rstrip()
            instructions.append(list(int(ele) for ele in line.split()[1::2]))
    
        return crates, instructions

        
        
    def part_one_expected_test_value(self):
        """ Return Part One Expected Test Answer """
        return "CMZ"
        
    def part_two_expected_test_value(self):
        """ Return Part Two Expected Test Answer """
        return "MCD"
    
    def part_one(self):
        
        crates, instructions = self._parse_input()
        
        # go through the instructions
        for number, source, target in instructions:

            # extend the target
            crates[target-1].extend(reversed(crates[source-1][-number:]))

            # delete the source
            crates[source-1] = crates[source-1][:-number]

        final_answer = "".join(ele[-1] for ele in crates)

        return final_answer
        
    def part_two(self):
        crates, instructions = self._parse_input()
        
        # go through the instructions
        for number, source, target in instructions:

            # extend the target not reversed
            crates[target-1].extend(crates[source-1][-number:])

            # delete the source
            crates[source-1] = crates[source-1][:-number]

        # Get the top of each stack
        final_answer = "".join(ele[-1] for ele in crates)

        return final_answer
        