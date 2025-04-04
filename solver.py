# Github repository: https://github.com/SanjaySivaA/Sudoku-solver-using-Pycosat

import pycosat
from sudoku import Sudoku

constructor = list()

constraint1 = list()
for row in range(1, 10):
    for column in range(1, 10):
        for number in range(1, 10):
            constructor.append(100*row+10*column+number)
        constraint1.append(constructor)
        constructor = []

constraint2 = list()
for row in range(1, 10):
    for column in range(1, 10):
        for selected_number in range(1, 10):
            for number in range(1, 10):
                if number == selected_number:
                    constructor.append(100*row+10*column+number)
                else:
                    constructor.append(-(100*row+10*column+number))
            constraint2.append(constructor)
            constructor = []

constraint3 = list()
for row in range(1, 10):
    for number in range(1, 10):
        for column in range(1, 10):
            constructor.append(100*row+10*column+number)
        constraint3.append(constructor)
        constructor = []

constraint4 = list()
for column in range(1, 10):
    for number in range(1, 10):
        for row in range(1, 10):
            constructor.append(100*row+10*column+number)
        constraint4.append(constructor)
        constructor = []

constraint5 = list()
for row_group in range(0, 3):
    for column_group in range(0, 3):
        for number in range(1, 10):
            for row in range(1 + 3*row_group, 4 + 3*row_group):
                for column in range(1 + 3*column_group, 4 + 3*column_group):
                    constructor += [100*row+10*column+number]
            constraint5.append(constructor)

            for i in range(len(constructor)):
                    for j in range(i + 1, len(constructor)):
                        constraint5.append([-constructor[i], -constructor[j]])

            constructor = []

fixed_constraints = constraint1 + constraint2 + constraint3 + constraint4 + constraint5

with open('p.txt', 'r') as file:
    lines = file.readlines()

with open('output.txt', 'w') as out_file:
    pass

for line in lines:
    puzzle = Sudoku(line.replace('\n', ''))

    clauses  = fixed_constraints + puzzle.variable_constraint

    pycosat_solution = pycosat.solve(clauses)
    solution = puzzle.format_pycosat_solution(pycosat_solution)
    
    with open('output.txt', 'a') as out_file:
        if solution == None:
            out_string ='No solution'
        else:
            out_string = ''
            for row in range(9):
                for column in range(9):
                    out_string += str(solution[row][column])
        out_string += '\n'
        out_file.write(out_string)

    # for array in solution:
    #     print(array)
    # print()