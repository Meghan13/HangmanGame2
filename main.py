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
wrong_letters_font = pygame.font.Font("ALGER.TTF", 18)
title = font.render("Welcome to Hangman!", True, constants.WHITE, constants.DARK_BROWN)
text_rect = title.get_rect()
text_rect.center = (450, 50)
letters_title_pos = (700, 50)
letters_title = wrong_letters_font.render("Letters Guessed", True, constants.WHITE, constants.DARK_BROWN)
letters_title_rect = letters_title.get_rect()
letters_title_rect.center = letters_title_pos
enter_letter = font.render("Please Enter a Letter", True, constants.WHITE, constants.BLACK)
enter_letter_rect = enter_letter.get_rect()
enter_letter_rect.center = (450, 400)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
screen.fill(pygame.Color(constants.BLACK))

words = []
# Dictionary with letter of word as key, and position in the word as array of values (handle multiples of letters).
word_dashes = {}


def build_word_list():
    word_bank = open("word_bank.txt", "r")
    for line in word_bank:
        if line != "" and line[0] != '#':
            line = line.strip()
            words.append(line)

def get_random_word():
    word = random.choice(words)
    # word = "shell"
    return word.upper()


def dashes_for_word(word):
    if len(word) >= 8:
        start = (80, 320)
    elif 6 < len(word) < 8:
        start = (150, 320)
    else:
        start = (250, 320)

    space = 100

    for element in range(len(word)):
        word_dashes[word[element]] = []
    for element in range (len(word)):
        word_dashes[word[element]].append(pygame.draw.line(screen, pygame.Color(constants.WHITE), start, (start[0] + 50, start[1]), 2))
        # print(word_dashes)
        start = (start[0] + space, start[1])


def score(wins, losses):
    font2 = pygame.font.Font("ALGER.TTF", 18)
    player_score = font2.render("Wins & Losses", True, constants.WHITE, constants.DARK_BROWN)
    player_score_rect = player_score.get_rect()
    player_score_rect.center = (50, 50)
    screen.blit(player_score, player_score_rect.center)


def letters_guessed(player_guess, random_word, wrong_letters):
    title_pos = (700, 50)
    wrong_letters_font = pygame.font.Font("ALGER.TTF", 18)
    correct_letters_font = pygame.font.Font("ALGER.TTF", 40)
    wrong_letters_to_print = ""
    correct_letter_pos = ()
    correct_multi_letters_pos = []

    if player_guess in random_word:
        # TODO: Add letters to dashes
        # print(word_dashes[player_guess])
        # Place letter at same location as corresponding dash
        if len(word_dashes[player_guess]) > 1:
            for element in range(len(word_dashes[player_guess])):
                correct_multi_letters_pos.append((word_dashes[player_guess][element][0], word_dashes[player_guess][element][1]))
            for element in range(len(correct_multi_letters_pos)):
                correct_letters_to_print = correct_letters_font.render(player_guess, True, constants.WHITE, constants.BLACK)
                correct_letters_display = correct_letters_to_print.get_rect()
                correct_letters_display.center = correct_multi_letters_pos[element]
                screen.blit(correct_letters_to_print, correct_letters_display.center)
                print(correct_multi_letters_pos[element])


        else:
            correct_letter_pos = (word_dashes[player_guess][0][0], word_dashes[player_guess][0][1])
            correct_letter_to_print = correct_letters_font.render(player_guess, True, constants.WHITE, constants.BLACK)
            correct_letter_display = correct_letter_to_print.get_rect()
            correct_letter_display.center = correct_letter_pos
            screen.blit(correct_letter_to_print, correct_letter_display.center)
        # print(correct_letter_pos)
        # print(correct_multi_letters_pos)

    elif player_guess in wrong_letters:
        pass

    else:
        wrong_letters.append(player_guess)
        for place in range(len(wrong_letters)):
            # TODO: fencepost case. When max wrong guesses don't add extra space
            wrong_letters_to_print = wrong_letters_to_print + wrong_letters[place] + " "

        # Guessed Wrong Letters
        player_letters_guessed = wrong_letters_font.render(str(wrong_letters_to_print), True, constants.WHITE, constants.BLACK)
        letters_guessed_rect = player_letters_guessed.get_rect()
        letters_guessed_rect.center = (title_pos[0], title_pos[1] + 50)
        # Display
        screen.blit(player_letters_guessed, letters_guessed_rect.center)



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

    screen.blit(letters_title, letters_title_rect.center)
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
