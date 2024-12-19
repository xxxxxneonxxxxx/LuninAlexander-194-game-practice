import sys
import pygame
import random
def button(screen, x, y, width, height, color, text):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.Font(None, 30)
    text_surface = font.render(text, True, (245, 250, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)
    return rect
