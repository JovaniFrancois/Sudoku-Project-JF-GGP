import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched = value

    def draw(self, cell_size):
        x = self.col * cell_size
        y = self.row * cell_size

        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, cell_size, cell_size))

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_size, cell_size), 3)

        font = pygame.font.SysFont(None, 40)
        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + cell_size/3, y + cell_size/4))
        elif self.sketched != 0:
            text = font.render(str(self.sketched), True, (100, 100, 100))
            self.screen.blit(text, (x + 5, y + 5))
