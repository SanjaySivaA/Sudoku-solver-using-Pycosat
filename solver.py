import pycosat
import numpy as np

with open('p.txt', 'r') as file:
    line = file.readline().replace('\n', '')
    puzzle = list(line)

grid = np.array(puzzle).reshape(9, 9)
print(grid)