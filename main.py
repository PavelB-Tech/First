import sys
import pygame
from settings import Settings


def run_game():
    # initialize the game
    pygame.init()
    fg_settings = Settings()
    screen = pygame.display.set_mode((fg_settings.screen_width, fg_settings.screen_height))
    pygame.display.set_caption('First Game')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(fg_settings.bg_color)
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
