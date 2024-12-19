import sys
import pygame
import random


# Функция для отображения текста
def draw_text(text, font, color, surface, x, y):
    text_surface = font.render(text, True,(245, 250, 255) )
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)
# Отображаем текст на экране
