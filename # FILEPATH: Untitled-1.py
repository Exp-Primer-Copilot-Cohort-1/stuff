# FILEPATH: Untitled-1

import random

class SkipListMinesweeper:
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.board = [[0] * size for _ in range(size)]
        self.mines = set()

    def generate_mines(self):
        while len(self.mines) < self.num_mines:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            self.mines.add((row, col))

    def calculate_adjacent_mines(self, row, col):
        count = 0
        for i in range(max(0, row - 1), min(row + 2, self.size)):
            for j in range(max(0, col - 1), min(col + 2, self.size)):
                if (i, j) in self.mines:
                    count += 1
        return count

    def reveal_cell(self, row, col):
        if (row, col) in self.mines:
            return False
        count = self.calculate_adjacent_mines(row, col)
        self.board[row][col] = count
        return True

    def print_board(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))

class SkipListMinesweeper:
    def __init__(self, rows, cols, num_mines):
        self.rows = int(input("Enter the number of rows: "))
        self.cols = int(input("Enter the number of columns: "))
        self.mines = int(input("Enter the number of mines: "))
        self.board = [[0] * cols for _ in range(rows)]
        self.mines = set()
    # Rest of the class definition...