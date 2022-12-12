from math import floor,lcm
from math import lcm
from aoc.solution import BaseSolution

MONKEYS = {}

class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = []
        self.operations = None
        self.mod_number = 1
        self.true_monkey = -1
        self.false_monkey = -1
        self.inspections = 0
        
    def add_item(self, item):
        """ Add a item to our list of items. """
        self.items.append(item)
        
    def run_round(self , mod=-1):
        """ Run a round. """
        
        for item in self.items:
            
            worry = (floor(self._run_item_operation(item) / 3)
                    if mod  == -1  
                    else self._run_item_operation(item) % mod)
            
            next_monkey_id = (self.true_monkey 
                            if worry % self.mod_number == 0
                            else self.false_monkey)
            
            # Add item to our next monket
            MONKEYS[next_monkey_id].add_item(worry)
            
            # increase inspections
            self.inspections += 1
            
        self.items = []
            
            
            
    def _run_item_operation(self, power_value) -> int:
        """Run the monkey operation"""
        x = int(self.operations[0].replace("old", str(power_value)))
        y = int(self.operations[2].replace("old", str(power_value)))
        sign = self.operations[1]
        
        if sign == "+":
            return x + y
        elif sign == "-":
            return x - y
        elif sign == "*":
            return x * y
        else:
            return x / y
        
    def __repr__(self) -> str:  
        return f"Monkey {self.id}, Items: {self.items}, mod_number: {self.mod_number}, true_monkey: {self.true_monkey}, false_monkey: {self.false_monkey}"   

    def __str__(self) -> str:
        return f"Monkey {self.id}, Items: {self.items}, mod_number: {self.mod_number}, true_monkey: {self.true_monkey}, false_monkey: {self.false_monkey}"   
    
class DayElevenSolution(BaseSolution):

    def get_puzzle_day(self):
        return "day11"
    
    def part_one_expected_test_value(self):
        """ Return Part One Expected Test Answer """
        return 10605
        
    def part_two_expected_test_value(self):
        """ Return Part Two Expected Test Answer """
        return 2713310158
    
    def parse_monkeys(self):
        """ Parse Monkeys"""
        current_monkey = None
        for line in self._get_puzzle_data():
            if line.startswith("Monkey"):
                current_monkey = Monkey(line.split(" ")[1].replace(":",""))
            elif line.startswith("  Starting items:"):
                current_monkey.items = [ line.strip() for line in line.replace("  Starting items:","").split(",")]
            elif line.startswith("  Test:"):
                current_monkey.mod_number = int(line.replace("  Test: divisible by ",""))
            elif line.startswith("    If true:"):
                current_monkey.true_monkey  = line.replace("    If true: throw to monkey ","")
            elif line.startswith("    If false:"):            
                current_monkey.false_monkey = line.replace("    If false: throw to monkey ","")
            elif line.startswith("  Operation:"):
                current_monkey.operations = line.split(" = ")[1].split(" ")
            else:
                MONKEYS[current_monkey.id] = current_monkey
                print(f"Added Monkey: {current_monkey}")
                
    def part_one(self):
        
        self.parse_monkeys()
        
        for _ in range(20):
            for monkey_id in MONKEYS.keys():
                MONKEYS[monkey_id].run_round()

        top_two= sorted([MONKEYS[monkey_id].inspections for monkey_id in MONKEYS.keys()])[-2:]

        return top_two[0] * top_two[1]

    def part_two(self):
        self.parse_monkeys()
        
        # Find LCM since all the numbers are prime 
        mod = lcm(*[MONKEYS[monkey_id].mod_number for monkey_id in MONKEYS.keys()])
        
        for _ in range(10000):
            for monkey_id in MONKEYS.keys():
                MONKEYS[monkey_id].run_round(mod=mod)

        top_two= sorted([MONKEYS[monkey_id].inspections for monkey_id in MONKEYS.keys()])[-2:]

        return top_two[0] * top_two[1]
        