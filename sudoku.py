import pygame
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


def main_menu():
    pygame.display.set_caption("Welcome to Sudoku ")

    while True:
        SCREEN.fill((0, 0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Title
        MENU_TEXT = get_font(60).render("Welcome to Sudoku ", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Buttons
        EASY_BUTTON = Button(
            pos=(640, 250),
            text="EASY 30",
            font=get_font(50),
            base_color="white",
            hover_color="yellow"
        )

        MED_BUTTON = Button(
            pos=(640, 350),
            text="MEDIUM 40",
            font=get_font(50),
            base_color="white",
            hover_color="yellow"
        )

        HARD_BUTTON = Button(
            pos=(640, 450),
            text="HARD 50",
            font=get_font(50),
            base_color="white",
            hover_color="yellow"
        )

        for button in [EASY_BUTTON, MED_BUTTON, HARD_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(SCREEN)

        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    print("Start EASY mode")
                if MED_BUTTON.check_for_input(MENU_MOUSE_POS):
                    print("Start MEDIUM mode")
                if HARD_BUTTON.check_for_input(MENU_MOUSE_POS):
                    print("Start HARD mode")

        pygame.display.update()


main_menu()
