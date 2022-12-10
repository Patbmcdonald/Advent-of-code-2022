from aoc.solution import BaseSolution

class DayTenSolution(BaseSolution):

    def get_puzzle_day(self):
        return "day10"
    
    def part_one_expected_test_value(self):
        """ Return Part One Expected Test Answer """
        return 13140
        
    def part_two_expected_test_value(self):
        """ Return Part Two Expected Test Answer """
        return 0
    
    
    def _solve_fib(self, array, position, skip_number) -> int:
        if position >= len(array):
            return 0
        
        return (position * array[position - 1] + self._solve_fib(array, position + skip_number, skip_number))
    
    def part_one(self):
        commands = [x.replace('\n', '').split() for x in self._get_puzzle_input_reader().readlines()]
        x_register = 1
        cycle_count = 0
        register_at_x_cycle_count = {}
        
        for command in commands:
            name = command[0]
            for run_number in range(2 if name == 'addx' else 1):
                cycle_count += 1
                if name == 'addx' and run_number == 1:
                    x_register += int(command[1])
                    
                register_at_x_cycle_count[cycle_count] = x_register

        return self._solve_fib(register_at_x_cycle_count, 20, 40)
        
    def part_two(self):
        cmds = [x.replace('\n', '').split() for x in self._get_puzzle_input_reader().readlines()]
        cycle_count = 0
        x_register = 1
        current_pos = 0
        rows = ''      
        for command in cmds:
            name = command[0]
            for run_number in range(2 if name == 'addx' else 1):
                cycle_count += 1
                current_pos = cycle_count-1
                middle = x_register
                if name == 'addx' and run_number == 1:
                    x_register += int(command[1]) 
                if abs((current_pos % 40) - middle) <= 1:
                    rows += '#'
                else:
                    rows += '.'
                if cycle_count in (40, 80, 120, 160, 200, 240):
                    print(rows)
                    rows = ''
        return 0
        