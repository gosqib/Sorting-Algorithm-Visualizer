# doThis take in algorithm type

from typing import Any, Callable, List, Tuple, Union
import pygame
pygame.init()

SCREEN_RESOLUTION = [1500, 780]
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_RESOLUTION
DISPLAY = pygame.display.set_mode(SCREEN_RESOLUTION)

Position = Tuple[int, int]

BUTTON_FONT = pygame.font.SysFont("Times New Roman", 16)

# Colours
Colour = Tuple[int, int, int]
WHITE: Colour   = (255, 255, 255)
BLACK: Colour   = (0, 0, 0)
BROWN: Colour   = (150, 75, 0)
BLUE: Colour    = (0, 0, 255)
YELLOW: Colour  = (255, 255, 0)
RED: Colour     = (255, 0, 0)
GREEN: Colour   = (0, 255, 0)

pygame.display.set_caption("does stuff")

# bar should be on left side
# should be buttons each with same font
# multiplelines of diff font

# Textbox takes in; text, position
# returns to screen

# MultipleLines takes in; list of strings, position of first string
# Button takes in; msg, msgXcoo, msgYcoo, butX, butY, stanCol, hovCol, action

class Text:
    def __init__(self, text: str, colour: Colour, pos: Position, font_size: int) -> None:
        font = pygame.font.SysFont("Times New Roman", font_size)
        self._text = font.render(text, True, colour)
        self._pos = pos

    def display(self) -> object:
        return DISPLAY.blit(self._text, self._pos)



class MultipleLine:
    def __init__(self, texts: List[str], colour: Colour, start_pos: Position, font_size: int, gap: int = 20):
        _x, _y = start_pos
        self._boxes = [
            Text(text, colour, (_x, _y + iter * gap), font_size)
            for iter, text in enumerate(texts)
        ]

    # nbo return cause loop
    def display(self) -> None:
        for text in self._boxes:
            text.display()

class Button:
    def __init__(self, msg: str, font_size: int) -> None:
        self._msg = msg # shouold be msg instead
        self._font_size = font_size

    def text_object(self) -> Tuple[object, object]:
        text_style = pygame.font.SysFont("Times New Roman", self._font_size)
        text_surface = text_style.render(self._msg, True, (0, 0, 0))
        return text_surface, text_surface.get_rect()

    def button(self, msg_x: int, msg_y: int, but_wid: int, but_hei: int, rest_col: Colour, hov_col: Colour, action: Callable=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # tracks mouse info
        if msg_x + but_wid > mouse[0] > msg_x and msg_y + but_hei > mouse[1] > msg_y:
            pygame.draw.rect(
                DISPLAY, 
                hov_col, 
                (msg_x, msg_y, but_wid, but_hei) )

            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(DISPLAY, rest_col, (msg_x, msg_y, but_wid, but_hei) )

        #Textbox takes in msgX, msgY
        # find location of text, button gets put behind text location
        textSurf, textRect = self.text_object()
        textRect.center = msg_x + (but_wid / 2), msg_y + (but_hei / 2)
        DISPLAY.blit(textSurf, textRect)

    

