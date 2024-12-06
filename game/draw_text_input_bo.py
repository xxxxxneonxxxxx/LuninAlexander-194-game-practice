import sys
import pygame
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
GRAY = (200, 200, 200)


def draw_text_input_box(surface, rect, text, active):
    font = pygame.font.Font(None, 36)  # Шрифт для отображения текста

    color = LIGHT_BLUE if active else GRAY
    pygame.draw.rect(surface, color, rect, 2)
    txt_surface = font.render(text, True, BLACK)
    surface.blit(txt_surface, (rect.x + 5, rect.y + 5))