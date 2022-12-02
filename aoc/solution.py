from abc import abstractmethod

class BaseSolution:
    
    @abstractmethod
    def part_one(self):
        pass 
        
    @abstractmethod
    def part_two(self):
        pass
    
    def run(self):
        """Run the solution"""
        
        print("Running Part One Solution")
        self.part_one()
        print("Running Part Two Solution")
        self.part_two()