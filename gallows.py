import pygame
import constants


class Gallows:

    def __init__(self):
        pass

    def draw(self, screen):
        BASE_POS = (350, 250)
        MIDDLE = (400, 250)
        TOP_POS = (400, 110)
        BEAM_WIDTH = 4

        # base
        pygame.draw.line(screen, pygame.Color(constants.BROWN), BASE_POS, (BASE_POS[0] + 200, BASE_POS[1]), BEAM_WIDTH)

        # stand
        pygame.draw.line(screen, pygame.Color(constants.BROWN), MIDDLE, (MIDDLE[0], TOP_POS[1]), BEAM_WIDTH)

        # top
        pygame.draw.line(screen, pygame.Color(constants.BROWN), TOP_POS, (TOP_POS[0] + 75, TOP_POS[1]), BEAM_WIDTH)

        # support
        pygame.draw.line(screen, pygame.Color(constants.BROWN), (TOP_POS[0], TOP_POS[1] + 25), (TOP_POS[0] + 25, TOP_POS[1]),
                         BEAM_WIDTH - 1)

        # rope
        pygame.draw.line(screen, pygame.Color(constants.WHITE), (TOP_POS[0] + 75, TOP_POS[1]), (TOP_POS[0] + 75, TOP_POS[1] + 20),
                         BEAM_WIDTH - 2)