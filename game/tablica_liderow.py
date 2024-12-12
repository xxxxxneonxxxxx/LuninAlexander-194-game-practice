import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 50
FONT_SIZE = 24
TABLE_START_X, TABLE_START_Y = 50, 150
CELL_WIDTH, CELL_HEIGHT = 200, 40
ROWS = 10
COLUMNS = 3

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Настройка экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Таблица лидеров")

# Шрифт
font = pygame.font.Font(None, FONT_SIZE)

# Размеры матрицы для переключения
matrix_sizes = [(5, 5), (5, 6), (6, 6), (6, 7), (7, 7), (7, 8), (8, 8)]
current_size_index = 0


# Функция для отрисовки текста
def draw_text(surface, text, x, y, color=BLACK, center=False):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


# Функция для создания кнопок
def create_button(x, y, width, height, text, color=LIGHT_BLUE):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, DARK_BLUE, rect, 2)  # Рамка
    draw_text(screen, text, x + width // 2, y + height // 2, BLACK, center=True)
    return rect


# Генерация данных для таблицы
def generate_leaderboard_data(rows, cols):
    return [[f"R{r + 1}C{c + 1}" for c in range(cols)] for r in range(rows)]


# Главная функция
def main():
    global current_size_index

    clock = pygame.time.Clock()
    running = True

    # Кнопки для переключения размеров
    buttons = []
    for i, size in enumerate(matrix_sizes):
        x = 10 + i * (BUTTON_WIDTH + 10)
        y = 10
        buttons.append((create_button(x, y, BUTTON_WIDTH, BUTTON_HEIGHT, f"{size[0]}x{size[1]}"), size))

    # Данные таблицы
    leaderboard_data = generate_leaderboard_data(ROWS, COLUMNS)

    while running:
        screen.fill(WHITE)

        # Отрисовка заголовка
        draw_text(screen,
                  f"Текущий размер: {matrix_sizes[current_size_index][0]}x{matrix_sizes[current_size_index][1]}",
                  SCREEN_WIDTH // 2, 80, BLACK, center=True)

        # Отрисовка таблицы лидеров
        for row in range(ROWS):
            for col in range(COLUMNS):
                x = TABLE_START_X + col * CELL_WIDTH
                y = TABLE_START_Y + row * CELL_HEIGHT
                cell_rect = pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT)
                pygame.draw.rect(screen, LIGHT_BLUE, cell_rect)
                pygame.draw.rect(screen, DARK_BLUE, cell_rect, 2)
                draw_text(screen, leaderboard_data[row][col], x + CELL_WIDTH // 2, y + CELL_HEIGHT // 2, BLACK,
                          center=True)

        # Отрисовка кнопок
        for button, size in buttons:
            pygame.draw.rect(screen, DARK_BLUE if matrix_sizes[current_size_index] == size else LIGHT_BLUE, button)
            draw_text(screen, f"{size[0]}x{size[1]}", button.centerx, button.centery, BLACK, center=True)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, (button, size) in enumerate(buttons):
                    if button.collidepoint(mouse_pos):
                        current_size_index = i
                        leaderboard_data = generate_leaderboard_data(ROWS, COLUMNS)  # Обновить данные таблицы

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
