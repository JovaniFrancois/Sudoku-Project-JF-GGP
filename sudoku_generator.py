import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
	def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0]*row_length for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else '.' for num in row))
 
	def valid_in_row(self, row, num):
        return num not in self.board[row]

	def valid_in_col(self, col, num):
        return all(self.board[r][col] != num for r in range(self.row_length))

	 def valid_in_box(self, row_start, col_start, num):
        for r in range(row_start, row_start + self.box_length):
            for c in range(col_start, col_start + self.box_length):
                if self.board[r][c] == num:
                    return False
        return True

	def is_valid(self, row, col, num):
        if num in self.board[row]:
            return False
        if any(self.board[r][col] == num for r in range(self.row_length)):
            return False
        box_start_row = (row // self.box_length) * self.box_length
        box_start_col = (col // self.box_length) * self.box_length
        for r in range(box_start_row, box_start_row + self.box_length):
            for c in range(box_start_col, box_start_col + self.box_length):
                if self.board[r][c] == num:
                    return False
        return True



        box_start_row = (row // self.box_length) * self.box_length
        box_start_col = (col // self.box_length) * self.box_length
        for r in range(box_start_row, box_start_row + self.box_length):
            for c in range(box_start_col, box_start_col + self.box_length):
                if self.board[r][c] == num:
                    return False

        return True

    def fill_box(self, row_start, col_start):
        numbers = list(range(1, self.row_length + 1))
        random.shuffle(numbers)
        for r in range(row_start, row_start + self.box_length):
            for c in range(col_start, col_start + self.box_length):
                self.board[r][c] = numbers.pop()

    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)


    def remove_cells(self):
        count = self.removed_cells
        while count > 0:
            r = random.randint(0, self.row_length - 1)
            c = random.randint(0, self.row_length - 1)
            if self.board[r][c] != 0:
                self.board[r][c] = 0
                count -= 1

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()

    return board
