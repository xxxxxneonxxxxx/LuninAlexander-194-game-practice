import sys
import pygame

WHITE = (255, 255, 255)
BLACK = (245, 250, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)

font = pygame.font.Font(None, 36)


def draw_text(text, font, color, surface, x, y):
    text_surface = font.render(text, True, (245, 250, 255))
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)


def draw_button(surface, x, y, width, height, color, initial_text=""):
    text = initial_text
    input_active = False
    running = True
    BLACK = (245, 250, 255)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if x <= event.pos[0] <= x + width and y <= event.pos[1] <= y + height:
                    input_active = True
                else:
                    input_active = False

            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        # Рисуем кнопку
        pygame.draw.rect(surface, color, (x, y, width, height))
        pygame.draw.rect(surface, BLACK, (x, y, width, height), 2)

        draw_text(text, font, BLACK, surface, x + width // 2, y + height // 2)

        pygame.display.flip()
    return text
