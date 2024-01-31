import re
import text

def extract_numbers(input_string):
    numbers = re.findall(r'\d+', input_string)
    if numbers:
        return int(''.join(numbers))
    

def check_max(list, max):
    return all (x <= max for x in list)

def get_ids(text):
    moves = {}
    games = text.split("\n")
    total = 0

    for game in games:
        set = game.split(";")
        name = set[0].split(":")[0]
        set[0] = set[0].removeprefix(name+": ")
        moves[name] = set
        reds = []
        blues = []
        greens = []

        for cube in moves[name]:
            colors = cube.split(",")

            for color in colors:
                if "red" in color:
                    if extract_numbers(color) > 12: 
                        moves[name] = False
                elif "blue" in color:
                    if extract_numbers(color) > 14: 
                        moves[name] = False
                else:
                    if extract_numbers(color) > 13: 
                        moves[name] = False
                        
        if moves[name] is not False:
            total += extract_numbers(name)
    return total






print(get_ids(text.text()))