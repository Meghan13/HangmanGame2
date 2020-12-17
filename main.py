import pygame
import gallows
import constants

pygame.init()

WIDTH = 900
HEIGHT = 600

font = pygame.font.Font("ALGER.TTF", 32)
TITLE = font.render("Welcome to Hangman!", True, constants.WHITE, constants.DARK_BROWN)
text_rect = TITLE.get_rect()
text_rect.center = (450, 50)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
screen.fill(pygame.Color(0, 0, 0))

# Script is running
running = True

gallows = gallows.Gallows()

while running:

    screen.blit(TITLE, text_rect)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()
        gallows.draw(screen)
        pygame.display.update()
