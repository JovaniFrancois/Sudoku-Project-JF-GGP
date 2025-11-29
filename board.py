import pygame

class Board:
    def __init__(self, width, height, screen, generator):
        self.width = width
        self.height = height
        self.screen = screen
        self.size = 9
        self.cell_size = width // self.size

        generator.fill_values()
        self.solution = [row[:] for row in generator.get_board()]
        generator.remove_cells()
        board_values = generator.get_board()

        self.cells = [
            [Cell(board_values[r][c], r, c, screen) for c in range(self.size)]
            for r in range(self.size) ]

        for r in range(self.size):
            for c in range(self.size):
                self.cells[r][c].original = (board_values[r][c] != 0)

        self.selected = None

    def draw(self):
        for i in range(10):
            thick = 3 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0),
                             (0, i * self.cell_size),
                             (self.width, i * self.cell_size), thick)
            pygame.draw.line(self.screen, (0, 0, 0),
                             (i * self.cell_size, 0),
                             (i * self.cell_size, self.height), thick)

        for row in self.cells:
            for cell in row:
                cell.draw(self.cell_size)

    def click(self, x, y):
        if x < self.width and y < self.height:
            return (y // self.cell_size, x // self.cell_size)
        return None

    def select(self, row, col):
        if self.selected:
            r, c = self.selected
            self.cells[r][c].selected = False

        self.selected = (row, col)
        self.cells[row][col].selected = True

    def place_number(self, num):
        if not self.selected:
            return False

        r, c = self.selected
        cell = self.cells[r][c]

        if not cell.original:
            cell.set_cell_value(num)
            return True

        return False
