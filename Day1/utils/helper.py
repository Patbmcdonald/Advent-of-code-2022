def read_lines_to_list(input_name:str) -> list:
    """ Read Lines from inputed file location """
    lines = []
    for line in open(input_name, 'r').readlines():
        lines.append(line.strip())
        
    return lines