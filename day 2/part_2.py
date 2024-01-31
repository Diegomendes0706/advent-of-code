import text
from part_1 import extract_numbers

text_data = text.text()

moves = {}
games = text_data.split("\n")
total = 0

for game in games:
    game_data = game.split(";")
    name = game_data[0].split(":")[0]
    game_data[0] = game_data[0].removeprefix(name + ": ")
    moves[name] = game_data
    reds = []
    blues = []
    greens = []

    for cube in moves[name]:
        colors = cube.split(",")

        for color in colors:
            if "red" in color: 
                reds.append(extract_numbers(color))
            elif "blue" in color:
                blues.append(extract_numbers(color))
            else:
                greens.append(extract_numbers(color))
    
    total += (max(reds) * max(blues) * max(greens))

print(total)
