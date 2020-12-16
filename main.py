import pygame

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Script is running
running = True

while running:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()