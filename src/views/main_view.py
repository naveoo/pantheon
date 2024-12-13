from settings.config import *
import pygame
from pygame.locals import *

def initialize_window():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(NAME)
    return screen

def main_view():
    screen = initialize_window()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.display.flip()
    pygame.quit()