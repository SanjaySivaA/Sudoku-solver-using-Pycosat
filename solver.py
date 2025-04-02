import pycosat
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