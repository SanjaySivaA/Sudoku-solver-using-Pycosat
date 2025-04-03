# # import pycosat
# import numpy as np

# with open('p.txt', 'r') as file:
#     line = file.readline().replace('\n', '')
#     puzzle = list(line)

# grid = np.array(puzzle).reshape(9, 9)

# constructor = list()

# constraint1 = list()
# for i in range(1, 10):
#     for j in range(1, 10):
#         for x in range(1, 10):
#             constructor.append(100*i+10*j+x)
#         constraint1.append(constructor)
#         constructor = []

# constraint2 = list()
# for i in range(1, 10):
#     for j in range(1, 10):
#         for selected_x in range(1, 10):
#             for x in range(1, 10):
#                 if x == selected_x:
#                     constructor.append(100*i+10*j+x)
#                 else:
#                     constructor.append(-(100*i+10*j+x))
#             constraint2.append(constructor)
#             constructor = []

# constraint3 = list()
# for row in range(1, 10):
#     for number in range(1, 10):
#         for column in range(1, 10):
#             constructor.append(100*row+10*column+number)
#         constraint3.append(constructor)
#         constructor = []

#         for current_col in range(1, 10):
#                 for next_col in range(current_col + 1, 10):
#                     constraint3.append([-(100*row+10*current_col+number), -(100*row+10*next_col+number)])


import pycosat

# Encode a variable as a unique number
def var(r, c, v):
    return r * 100 + c * 10 + v

# 1. Each cell contains at least one value.
def at_least_one_number():
    clauses = []
    for r in range(1, 10):
        for c in range(1, 10):
            clauses.append([var(r, c, v) for v in range(1, 10)])
    return clauses

# 2. Each cell contains at most one value.
def at_most_one_number():
    clauses = []
    for r in range(1, 10):
        for c in range(1, 10):
            for v1 in range(1, 10):
                for v2 in range(v1 + 1, 10):
                    clauses.append([-var(r, c, v1), -var(r, c, v2)])
    return clauses

# 3. Each row contains all values.
def row_constraints():
    constraint3 = list()
    constructor = []
    for row in range(1, 10):
        for number in range(1, 10):
            for column in range(1, 10):
                constructor.append(100*row+10*column+number)
            constraint3.append(constructor)
            constructor = []

            for current_col in range(1, 10):
                    for next_col in range(current_col + 1, 10):
                        constraint3.append([-(100*row+10*current_col+number), -(100*row+10*next_col+number)])
    return constraint3

# 4. Each column contains all values.
def column_constraints():
    clauses = []
    for c in range(1, 10):
        for v in range(1, 10):
            clauses.append([var(r, c, v) for r in range(1, 10)])  # At least once
            for r1 in range(1, 10):
                for r2 in range(r1 + 1, 10):
                    clauses.append([-var(r1, c, v), -var(r2, c, v)])  # At most once
    return clauses

# 5. Each 3x3 block contains all values.
def block_constraints():
    clauses = []
    for br in range(0, 3):  # Block row index
        for bc in range(0, 3):  # Block column index
            for v in range(1, 10):
                block_cells = [var(r, c, v) for r in range(1 + 3 * br, 4 + 3 * br)
                                               for c in range(1 + 3 * bc, 4 + 3 * bc)]
                clauses.append(block_cells)  # At least once
                for i in range(len(block_cells)):
                    for j in range(i + 1, len(block_cells)):
                        clauses.append([-block_cells[i], -block_cells[j]])  # At most once
    return clauses

# 6. Initial puzzle constraints (set the given numbers in the Sudoku)
def initial_constraints(puzzle):
    clauses = []
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] != 0:
                clauses.append([var(r + 1, c + 1, puzzle[r][c])])
    return clauses

# Solve the Sudoku using PycoSAT
def solve_sudoku(puzzle):
    clauses = (
        at_least_one_number()
        + at_most_one_number()
        + row_constraints()
        + column_constraints()
        + block_constraints()
        + initial_constraints(puzzle)
    )
    
    solution = pycosat.solve(clauses)
    
    if solution == "UNSAT":
        return None
    
    grid = [[0] * 9 for _ in range(9)]
    
    for val in solution:
        if val > 0:
            r, c, v = val // 100, (val // 10) % 10, val % 10
            grid[r - 1][c - 1] = v
    
    return grid

# Example Sudoku puzzle (0 represents empty cells)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve and print the solution
solution = solve_sudoku(puzzle)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found")
