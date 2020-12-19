import pygame
import gallows
import constants
import text_input
import random

pygame.init()

#Screen size
WIDTH = 900
HEIGHT = 600

#Title Screen
font = pygame.font.Font("ALGER.TTF", 32)
title = font.render("Welcome to Hangman!", True, constants.WHITE, constants.DARK_BROWN)
text_rect = title.get_rect()
text_rect.center = (450, 50)
enter_letter = font.render("Please Enter a Letter", True, constants.WHITE, constants.BLACK)
enter_letter_rect = enter_letter.get_rect()
enter_letter_rect.center = (450, 400)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
screen.fill(pygame.Color(constants.BLACK))

words = []

def build_word_list():
    word_bank = open("word_bank.txt", "r")
    for line in word_bank:
        if line != "" and [0] != '#':
            words.append(line)

def get_random_word():
    word = random.choice(words)
    return word



def dashes_for_word(word):
    start = (200, 320)
    space = 100
    for element in range (0, len(word)-1):
        pygame.draw.line(screen, pygame.Color(constants.WHITE), start, (start[0] + 50, start[1]), 2)
        start = (start[0] + space, start[1])


def score(wins, losses):
    font2 = pygame.font.Font("ALGER.TTF", 18)
    player_score = font2.render("Wins & Losses", True, constants.WHITE, constants.DARK_BROWN)
    player_score_rect = player_score.get_rect()
    player_score_rect.center = (50, 50)
    screen.blit(player_score, player_score_rect.center)


def letters_guessed(player_guess):
    title_pos = (700, 50)
    font2 = pygame.font.Font("ALGER.TTF", 18)
    # Title
    letters_title = font2.render("Letters Guessed", True, constants.WHITE, constants.DARK_BROWN)
    letters_title_rect = letters_title.get_rect()
    letters_title_rect.center = title_pos

    # Guessed Letters
    player_letters_guessed = font2.render(player_guess, True, constants.WHITE, constants.BLACK)
    letters_guessed_rect = player_letters_guessed.get_rect()
    letters_guessed_rect.center = (title_pos[0], title_pos[1] + 50)

    # Display
    screen.blit(letters_title, letters_title_rect.center)
    screen.blit(player_letters_guessed, letters_guessed_rect.center)


# Script is running
running = True

gallows = gallows.Gallows()
text_input = text_input.TextInput(screen)
build_word_list()
random_word = get_random_word()
dashes_for_word(random_word)
print(random_word)

while running:

    screen.blit(title, text_rect)
    screen.blit(enter_letter, enter_letter_rect)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()
        gallows.draw(screen)

        player_guess = "a"

        score(1, 1)
        letters_guessed(player_guess)
        pygame.display.update()

    text_input.update(events)
    pygame.display.update()
    # print(text_input.user_guess)  # Debugging user entry
    clock.tick(30)
