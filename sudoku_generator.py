import math
import random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.board

    def is_valid(self, row, col, num):
        if num in self.board[row]:
            return False

        for r in range(self.row_length):
            if self.board[r][col] == num:
                return False

        box_r = (row // self.box_length) * self.box_length
        box_c = (col // self.box_length) * self.box_length

        for r in range(box_r, box_r + self.box_length):
            for c in range(box_c, box_c + self.box_length):
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
        if col >= self.row_length:
            row += 1
            col = 0

        if row >= self.row_length:
            return True

        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == (row // self.box_length) * self.box_length:
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
