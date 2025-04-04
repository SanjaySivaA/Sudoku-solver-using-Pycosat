import pycosat
from sudoku import Sudoku

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
        out_string = ''
        for row in range(9):
            for column in range(9):
                out_string += str(solution[row][column])
        out_string += '\n'
        out_file.write(out_string)

    # for array in solution:
    #     print(array)
    # print()