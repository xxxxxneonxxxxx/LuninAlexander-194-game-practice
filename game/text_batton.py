import sys
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)


def draw_text(text, font, color, surface, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)


def draw_button(surface, x, y, width, height, color, initial_text=""):
    text = initial_text  # Текст, который вводится
    input_active = False  # Флаг активности поля ввода
    running = True
    BLACK = (0, 0, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Проверяем, нажата ли кнопка
                if x <= event.pos[0] <= x + width and y <= event.pos[1] <= y + height:
                    input_active = True  # Активируем ввод текста
                else:
                    input_active = False  # Отключаем ввод текста

            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:  # Если нажали Enter, заканчиваем ввод
                    running = False
                elif event.key == pygame.K_BACKSPACE:  # Удаляем последний символ
                    text = text[:-1]
                else:
                    text += event.unicode  # Добавляем введенный символ

        # Рисуем кнопку
        pygame.draw.rect(surface, color, (x, y, width, height))
        pygame.draw.rect(surface, BLACK, (x, y, width, height), 2)  # Обводка кнопки

        # Рисуем текст внутри кнопки
        draw_text(text, font, BLACK, surface, x + width // 2, y + height // 2)

        pygame.display.flip()  # Обновляем экран

    return text
