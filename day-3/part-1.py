from text import text_file 

symbols = "-/@=$%*&#+"
numbers = "1234567890"
tf = text_file()
i_numbers = {}
i_symbols = {}
lines = tf.split("\n")

for line in range(len(lines)):
    i_numbers[line] = [i for i, n in enumerate(lines[line]) if n in numbers]
    i_symbols[line] = [i for i, n in enumerate(lines[line]) if n in symbols]
    
    for place in i_numbers:
        if i_symbols[line]:
            beside = i_symbols[line][place-1] == place-1  or i_symbols[line][place+1] == place+1
        print(lines[line], beside)
    