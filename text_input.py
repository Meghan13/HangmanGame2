import pygame
import constants
import pygame_textinput


class TextInput:

    # textInput variables
    text_color = pygame.Color(constants.WHITE)
    input_box_pos = (400, 450)
    box_height = 50
    box_width = 50
    guess_made = False

    def __init__(self, screen, new_text_color = text_color, new_input_box_pos = input_box_pos, new_box_height = box_height,
                 new_box_width = box_width):
        self.textinput = pygame_textinput.TextInput(text_color=new_text_color, font_size=70, max_string_length=1,
                                                    cursor_color=constants.WHITE)
        self.input_box = pygame.Rect(new_input_box_pos, (new_box_width, new_box_height))
        self.screen = screen
        self.text_input_is_active = True
        self.user_guess = ""

    def update(self, events):
        self.textinput.input_string = self.textinput.input_string.upper()
        pygame.draw.rect(self.screen, pygame.Color(constants.BROWN), self.input_box)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # Handles clicking on input_box
                if self.input_box.collidepoint(x, y):
                    self.screen.blit(self.textinput.get_surface(), self.input_box_pos)
                    self.textinput.update(events)
                    self.text_input_is_active = True

                # Handles toggling of active input box
                elif not self.input_box.collidepoint(x, y):
                    self.textinput.cursor_visible = False
                    self.text_input_is_active = False
                    self.textinput.update(events)

            # Handles entry of user_guess upon pressing enter/return key
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.text_input_is_active:
                self.user_guess = self.textinput.input_string
                self.guess_made = True
                self.textinput.input_string = ""
                self.textinput.update(events)

        if self.text_input_is_active:
            self.textinput.update(events)
        self.screen.blit(self.textinput.get_surface(), self.input_box_pos)

    def get_text_input(self):
        return self.textinput



