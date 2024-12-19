from input import input_us
import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 50
FONT_SIZE = 28
TABLE_START_X, TABLE_START_Y = 50, 150
CELL_WIDTH, CELL_HEIGHT = 200, 40
ROWS = 10
COLUMNS = 2

# Цвета
Dark_grey = (33,36,43)
WHITE = (235,250,255)
Dark_grey_button = (24, 23, 28)
DARK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (12, 157, 88)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Таблица лидеров")

font = pygame.font.Font(None, FONT_SIZE)

matrix_sizes = [(5, 5), (5, 6), (6, 6), (6, 7), (7, 7), (7, 8), (8, 8)]
current_size_index = 0


def draw_text(surface, text, x, y, color=WHITE, center=False):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


def create_button(x, y, width, height, text, color=Dark_grey_button):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, DARK, rect, 2)  # Рамка
    draw_text(screen, text, x + width // 2, y + height // 2, WHITE, center=True)
    return rect


def generate_leaderboard_data(rows, cols,tip):
    try: a = input_us({"message": "SORT_TIME", "tip": tip})
    except:
        "error: SORT_TIME"
    table=[]
    a=a['table']
    print(a)

    for r in a.keys():
        print(r)
        table.append([r,a[r][0]])
    while len(table)<10:
        table.append([None,None])
    print(table)
    return table

def table():
    global current_size_index

    clock = pygame.time.Clock()
    running = True

    default_size = (5, 5)
    if default_size in matrix_sizes:
        current_size_index = matrix_sizes.index(default_size)
    else:
        raise ValueError(f"Размер {default_size} отсутствует в списке matrix_sizes!")

    buttons = []
    for i, size in enumerate(matrix_sizes):
        x = 10 + i * (BUTTON_WIDTH + 10)
        y = 10
        buttons.append((create_button(x, y, BUTTON_WIDTH, BUTTON_HEIGHT, f"{size[0]}x{size[1]}"), size))

    leaderboard_data = generate_leaderboard_data(ROWS, COLUMNS,
                                                 f"{matrix_sizes[current_size_index][0]}x{matrix_sizes[current_size_index][1]}")
    buttons.append((create_button(200,555, 100, 40, 'exit'), "exit"))
    while running:
        screen.fill(Dark_grey)
        draw_text(screen,
                  f"Текущий размер: {matrix_sizes[current_size_index][0]}x{matrix_sizes[current_size_index][1]}",
                  SCREEN_WIDTH // 2, 80, WHITE, center=True)
        for row in range(ROWS):
            for col in range(COLUMNS):
                x = TABLE_START_X + col * CELL_WIDTH
                y = TABLE_START_Y + row * CELL_HEIGHT
                cell_rect = pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT)
                pygame.draw.rect(screen, Dark_grey_button, cell_rect)
                pygame.draw.rect(screen, DARK, cell_rect, 2)
                draw_text(screen,
                          leaderboard_data[row][col] if row < len(leaderboard_data) and col < len(
                              leaderboard_data[row]) else '',
                          x + CELL_WIDTH // 2, y + CELL_HEIGHT // 2, WHITE,
                          center=True)

        for button, size in buttons:
            if size == "exit":
                pygame.draw.rect(screen, Dark_grey_button, button)  # Рисуем кнопку
                pygame.draw.rect(screen, DARK, button, 2)  # Рисуем рамку
                draw_text(screen, "Exit", button.centerx, button.centery, WHITE, center=True)  # Текст "exit"
            else:
                # Если кнопка для выбора размера таблицы, рисуем размер
                pygame.draw.rect(screen, DARK if matrix_sizes[current_size_index] == size else Dark_grey_button, button)
                draw_text(screen, f"{size[0]}x{size[1]}", button.centerx, button.centery, WHITE, center=True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, (button, size) in enumerate(buttons):
                    if button.collidepoint(mouse_pos):
                        if size == "exit":
                            return "back"
                        current_size_index = i
                        leaderboard_data = generate_leaderboard_data(ROWS, COLUMNS,f"{size[0]}x{size[1]}")
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

