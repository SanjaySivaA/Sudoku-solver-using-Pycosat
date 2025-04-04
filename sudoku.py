class Sudoku:
    def __init__(self,  puzzle_string):
        
        self.puzzle = self.initialise_puzzle(puzzle_string)

        self.variable_constraint = self.constraint6()
    
    def initialise_puzzle(self, puzzle_string):
        puzzle = list(puzzle_string)
        constructor = list()
        result = list()
        i = 0
        while i < len(puzzle):
            for _ in range(9):
                constructor.append(puzzle[i])
                i += 1
            result.append(constructor)
            constructor = list()
        return result
    
    def constraint6(self):
        constraint6 = list()
        for row in range(9):
            for column in range(9):
                if self.puzzle[row][column] != '.':
                    constraint6.append([100*(row+1)+10*(column+1)+int(self.puzzle[row][column])])
        return constraint6
    
    def format_pycosat_solution(self, solution):
        grid = [[0] * 9 for _ in range(9)]
        for value in solution:
            if value > 0:
                row = value // 100
                column = (value // 10) % 10
                number = value % 10
                grid[row - 1][column - 1] = number
        return grid