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
        if line != "" and line[0] != '#':
            words.append(line)

def get_random_word():
    word = random.choice(words)
    return word.upper()



def dashes_for_word(word):
    if len(word) >= 8:
        start = (80, 320)
    elif 6 < len(word) < 8:
        start = (150, 320)
    else:
        start = (250, 320)

    space = 100
    for element in range (0, len(word)):
        pygame.draw.line(screen, pygame.Color(constants.WHITE), start, (start[0] + 50, start[1]), 2)
        start = (start[0] + space, start[1])


def score(wins, losses):
    font2 = pygame.font.Font("ALGER.TTF", 18)
    player_score = font2.render("Wins & Losses", True, constants.WHITE, constants.DARK_BROWN)
    player_score_rect = player_score.get_rect()
    player_score_rect.center = (50, 50)
    screen.blit(player_score, player_score_rect.center)


def letters_guessed(player_guess, random_word, wrong_letters):
    title_pos = (700, 50)
    font2 = pygame.font.Font("ALGER.TTF", 18)
    # Title
    letters_title = font2.render("Letters Guessed", True, constants.WHITE, constants.DARK_BROWN)
    letters_title_rect = letters_title.get_rect()
    letters_title_rect.center = title_pos
    wrong_letters_to_print = ""

    if player_guess in random_word:
        pass # TODO: Add letters to dashes

    elif player_guess in wrong_letters:
        pass

    else:
        wrong_letters.append(player_guess)
        for place in range(len(wrong_letters)):
            # TODO: fencepost case. When max wrong guesses don't add extra space
            wrong_letters_to_print = wrong_letters_to_print + wrong_letters[place] + " "

        # Guessed Wrong Letters
        player_letters_guessed = font2.render(str(wrong_letters_to_print), True, constants.WHITE, constants.BLACK)
        letters_guessed_rect = player_letters_guessed.get_rect()
        letters_guessed_rect.center = (title_pos[0], title_pos[1] + 50)
        # Display
        screen.blit(player_letters_guessed, letters_guessed_rect.center)

    screen.blit(letters_title, letters_title_rect.center)


# Script is running
running = True

gallows = gallows.Gallows()
text_input = text_input.TextInput(screen)
build_word_list()
random_word = get_random_word()
dashes_for_word(random_word)
print(random_word)
wrong_letters = []
guess_made = False

while running:

    screen.blit(title, text_rect)
    screen.blit(enter_letter, enter_letter_rect)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()
        gallows.draw(screen)
        score(1, 1)

        pygame.display.update()

    if text_input.guess_made:
        letters_guessed(text_input.user_guess, random_word, wrong_letters)
        text_input.guess_made = False
        text_input.textinput.input_string = ""

    text_input.update(events)
    pygame.display.update()
    # print(text_input.user_guess)  # Debugging user entry
    clock.tick(30)
