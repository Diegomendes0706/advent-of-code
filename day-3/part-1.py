from text import text_file 
import re


def get_numbers(x):
    return re.findall(r'\d+', x)



symbols = "-/@=$%*&#+"
numbers = "1234567890"
tf = text_file()
i_numbers = {}
i_symbols = {}
lines = tf.split("\n")

part_numbers = []

for i, line in enumerate(lines):
    i_numbers[i] = [index for index, n in enumerate(line) if n in numbers]
    i_symbols[i] = [index for index, n in enumerate(line) if n in symbols]

    for j in i_numbers[i]:
        if (j+1) in i_symbols[i] or (j-1) in i_symbols[i]:
            part_numbers.append(int(line[j]))


print(part_numbers) 