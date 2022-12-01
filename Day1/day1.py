from utils.helper import read_lines_to_list


def _build_calorie_map() -> dict:
    """ Build a dictionary of calories and their associated totals."""
    
    totals = {}
    current_index = 1
    
    for line in read_lines_to_list('inputs/input.txt'):
        this_line = line.strip()
        
        if len(this_line) == 0:
            current_index += 1
            continue
            
        if totals.get(current_index) is None:
            totals[current_index] = int(this_line)
        else:
            totals[current_index] = totals[current_index]  + int(this_line)
            
    return totals
    
def part1():
    """ Return the top elf calories """
    calorie_mapping_per_elf = _build_calorie_map()
    
    # Sort Map by Values and return top 1 
    top_elf_index = sorted(calorie_mapping_per_elf, key=calorie_mapping_per_elf.get, reverse=True)[:1]
    
    print("Top Elf Calories Total: {}".format(calorie_mapping_per_elf[top_elf_index[0]]))
    
def part2():
    """ Return the sum of the top 3 elf calories """

    calorie_mapping_per_elf = _build_calorie_map()
    
    # Sort Map by Values and return top 1 
    top_elf_3_elfs = sorted(calorie_mapping_per_elf, key=calorie_mapping_per_elf.get, reverse=True)[:3]
    
    total_sum_of_calories = 0
    
    for index in top_elf_3_elfs:
        total_sum_of_calories+= calorie_mapping_per_elf[index]
        
    print("Top 3 Elf Total: {}".format(total_sum_of_calories))
    
if __name__=="__main__":
    print("Part 1")
    part1()
    print("Part 2")
    part2()