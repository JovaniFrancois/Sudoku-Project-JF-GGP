import pygame
from cell import Cell
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))

def get_font(size):
    return pygame.font.SysFont("arial", size)

class Button:
    def __init__(self, pos, text, font, base_color, hover_color):
        self.x, self.y = pos
        self.text = text
        self.font = font
        self.base_color = base_color
        self.hover_color = hover_color
        self.rendered = self.font.render(self.text, True, self.base_color)
        self.rect = self.rendered.get_rect(center=(self.x, self.y))

    def update(self, screen):
        screen.blit(self.rendered, self.rect)

    def check_for_input(self, pos):
        return self.rect.collidepoint(pos)

    def change_color(self, pos):
        if self.check_for_input(pos):
            self.rendered = self.font.render(self.text, True, self.hover_color)
        else:
            self.rendered = self.font.render(self.text, True, self.base_color)

def play_game(difficulty):
    from sudoku_generator import SudokuGenerator
    from board import Board

    generator = SudokuGenerator(9, difficulty)
    generator.fill_values()
    generator.remove_cells()
    board = Board(540, 540, SCREEN, generator)

    clock = pygame.time.Clock()

    while True:
        SCREEN.fill((255, 255, 255))
        mouse_pos = pygame.mouse.get_pos()

        board.draw()

        start_x = 200
        y = 600
        for i in range(1, 10):
            x = start_x + (i - 1) * 90
            pygame.draw.rect(SCREEN, (200, 200, 200), (x, y, 80, 60))
            text = get_font(40).render(str(i), True, (0, 0, 0))
            SCREEN.blit(text, (x + 25, y + 15))

        reset_btn = Button((850, 200), "RESET", get_font(30), "black", "yellow")
        restart_btn = Button((850, 300), "RESTART", get_font(30), "black", "yellow")
        exit_btn = Button((850, 400), "EXIT", get_font(30), "black", "yellow")

        for b in [reset_btn, restart_btn, exit_btn]:
            b.change_color(mouse_pos)
            b.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell = board.click(mouse_pos[0], mouse_pos[1])
                if cell:
                    board.select(*cell)

                if reset_btn.check_for_input(mouse_pos):
                    board.reset_to_original()
                if restart_btn.check_for_input(mouse_pos):
                    return
                if exit_btn.check_for_input(mouse_pos):
                    pygame.quit()
                    exit()

            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    board.place_number(event.key - pygame.K_1 + 1)
                if event.key == pygame.K_RETURN:
                    pass

        if board.is_full():
            board.update_board()
            if board.check_board():
                game_over_screen(True)
            else:
                game_over_screen(False)
            return

        pygame.display.update()
        clock.tick(60)

def main_menu():
    pygame.display.set_caption("Welcome to Sudoku ")

    while True:
        SCREEN.fill((0, 0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(60).render("Welcome to Sudoku ", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        EASY_BUTTON = Button((640, 250), "EASY 30", get_font(50), "white", "yellow")
        MED_BUTTON = Button((640, 350), "MEDIUM 40", get_font(50), "white", "yellow")
        HARD_BUTTON = Button((640, 450), "HARD 50", get_font(50), "white", "yellow")

        for button in [EASY_BUTTON, MED_BUTTON, HARD_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    play_game(30)
                if MED_BUTTON.check_for_input(MENU_MOUSE_POS):
                    play_game(40)
                if HARD_BUTTON.check_for_input(MENU_MOUSE_POS):
                    play_game(50)

        pygame.display.update()

def game_over_screen(win):
    while True:
        SCREEN.fill((0, 0, 0))
        title = "Game Won!" if win else "Game Over!"
        color = (0, 255, 0) if win else (255, 0, 0)

        text = get_font(60).render(title, True, color)
        rect = text.get_rect(center=(640, 200))
        SCREEN.blit(text, rect)

        info = get_font(40).render("Click to return to menu", True, (255, 255, 255))
        irect = info.get_rect(center=(640, 350))
        SCREEN.blit(info, irect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.display.update()

main_menu()
