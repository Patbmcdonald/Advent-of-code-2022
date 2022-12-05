

def read_lines_to_list(input_name:str) -> list:
    """ Read Lines from inputed file location """
    lines = []

    for line in open(input_name, 'r').readlines():
        lines.append(line.rstrip())
        
    return lines


def get_reader(input_name:str) -> list:
    """ Read Lines from inputed file location """
    return open(input_name, 'r')



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'