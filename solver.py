# import pycosat
import numpy as np

with open('p.txt', 'r') as file:
    line = file.readline().replace('\n', '')
    puzzle = list(line)

grid = np.array(puzzle).reshape(9, 9)

constructor = list()

constraint1 = list()
for i in range(1, 10):
    for j in range(1, 10):
        for x in range(1, 10):
            constructor.append(100*i+10*j+x)
        constraint1.append(constructor)
        constructor = []

constraint2 = list()
for i in range(1, 10):
    for j in range(1, 10):
        for selected_x in range(1, 10):
            for x in range(1, 10):
                if x == selected_x:
                    constructor.append(100*i+10*j+x)
                else:
                    constructor.append(-(100*i+10*j+x))
            constraint2.append(constructor)
            constructor = []

constraint3 = list()
for row in range(1, 10):
    for number in range(1, 10):
        for column in range(1, 10):
            constructor.append(100*row+10*column+number)
        constraint3.append(constructor)
        constructor = []

        for current_col in range(1, 10):
                for next_col in range(current_col + 1, 10):
                    constraint3.append([-(100*row+10*current_col+number), -(100*row+10*next_col+number)])

constraint4 = list()
for column in range(1, 10):
    for number in range(1, 10):
        for row in range(1, 10):
            constructor.append(100*row+10*column+number)
        constraint4.append(constructor)
        constructor = []

        for current_row in range(1, 10):
                for next_row in range(current_row + 1, 10):
                    constraint4.append([-(100*current_row+10*column+number), -(100*next_row+10*column+number)])

constraint6 = list()
for row in range(9):
    for column in range(9):
        if grid[row][column] != '.':
            constraint6.append([100*(row+1)+10*(column+1)+int(grid[row][column])])

puz = list(grid)
print(puz)