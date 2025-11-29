class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected = None
        self.size = 9
        self.cell_width = width // self.size
        self.cell_height = height // self.size

      if difficulty == "easy":
            self.removed = 30
        elif difficulty == "medium":
            self.removed = 40
        else:
            self.removed = 50

        self.sudoku_generator = SudokuGenerator(self.size, self.removed)
        self.sudoku_generator.fill_values()
        self.solution = [row[:] for row in self.sudoku_generator.get_board()]
        self.sudoku_generator.remove_cells()
        board_values = self.sudoku_generator.get_board()

        self.cells = [[Cell(board_values[r][c], r, c, screen,
                            c * self.cell_width, r * self.cell_height,
                            self.cell_width, self.cell_height) for c in range(self.size)] for r in range(self.size)]

    def draw(self):
        for i in range(self.size + 1):
            thick = 4 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i*self.cell_height), (self.width, i*self.cell_height), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i*self.cell_width, 0), (i*self.cell_width, self.height), thick)

        for row in self.cells:
            for cell in row:
                cell.draw()

    def select(self, row, col):
        if self.selected:
            self.cells[self.selected[0]][self.selected[1]].selected = False
        self.selected = (row, col)
        self.cells[row][col].selected = True

    def click(self, x, y):
        if x < self.width and y < self.height:
            row = y // self.cell_height
            col = x // self.cell_width
            return (row, col)
        return None

    def clear(self):
        if not self.selected:
            return
        row, col = self.selected
        cell = self.cells[row][col]
        if not cell.original:
            cell.set_cell_value(0)
            cell.set_sketched_value(0)

    def sketch(self, value):
        if not self.selected:
            return
        row, col = self.selected
        cell = self.cells[row][col]
        if not cell.original:
            cell.set_sketched_value(value)

    def place_number(self, value):
        if not self.selected:
            return False
        row, col = self.selected
        cell = self.cells[row][col]
        if not cell.original and self.solution[row][col] == value:
            cell.set_cell_value(value)
            cell.set_sketched_value(0)
            return True
        else:
            return False

    def reset_to_original(self):
        for row in self.cells:
            for cell in row:
                if not cell.original:
                    cell.set_cell_value(0)
                    cell.set_sketched_value(0)

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def check_board(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.cells[r][c].value != self.solution[r][c]:
                    return False
        return True
