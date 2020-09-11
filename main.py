import sys
import pygame
from configparser import ConfigParser



def run_game():
    # initialize the game
    pygame.init()

    config = ConfigParser()
    config.read('src/config.ini')

    screen = pygame.display.set_mode((config.getint('window', 'width'), config.getint('window', 'height')))
    bg_color = (config.getint('window', 'bg_color_r'), config.getint('window', 'bg_color_g'),
                config.getint('window', 'bg_color_b'))

    pygame.display.set_caption('First Game')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
