from math_file import chis
from buttons import button
from draw_text import draw_text
import sys
import pygame
import random

# Инициализация Pygame
pygame.init()  # Инициализация всех модулей Pygame
screen = pygame.display.set_mode((800, 800),
                                 pygame.RESIZABLE)  # Устанавливаем начальный размер окна и делаем его изменяемым
pygame.display.set_caption("Game")  # Устанавливаем заголовок окна

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)  # Светло-голубой цвет для кнопок
font = pygame.font.Font(None, 36)  # Шрифт для отображения текста
screen_width = 800  # Начальная ширина экрана
screen_height = 600  # Начальная высота экрана

# Функция для отображения меню
def draw_menu():
    screen.fill(BLACK)  # Заполняем экран черным цветом
    button(screen, screen_width // 2 - 50, screen_height // 2 - 20, 100, 40, LIGHT_BLUE,
           'Play')  # Кнопка "Play" в центре экрана
    draw_text('Menu', font, WHITE, screen, screen_width // 2, screen_height // 2 - 60)  # Текст "Menu" над кнопкой
    pygame.display.update()  # Обновляем экран

# Основной цикл меню
def menu():
    global in_menu  # Указываем, что будем менять глобальную переменную in_menu
    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Корректный выход из программы
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Проверка нажатия на кнопку "Play"
                if screen_width // 2 - 50 <= event.pos[0] <= screen_width // 2 + 50 and screen_height // 2 - 20 <= \
                        event.pos[1] <= screen_height // 2 + 20:
                    in_menu = False  # Переход в игровой режим

        draw_menu()  # Отображаем меню


# Глобальная переменная для хранения сгенерированных чисел
generated_numbers = []
in_menu=True

# Цвета
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)

# Главная функция игры
def game():
    global screen, in_menu
    buttons = []

    def recalculate_sums(matrix):
        """Пересчитывает суммы строк и столбцов."""
        row_sums = [sum(row) for row in matrix]
        col_sums = [sum(col) for col in zip(*matrix)]
        return row_sums, col_sums

    # Инициализация данных
    generated_numbers = chis(5, 5, 1, 19)
    for i in range(len(generated_numbers)):
        print(generated_numbers[i])
    generated_matrix = generated_numbers[2]
    required_row_sums = generated_numbers[1][0]
    required_col_sums = generated_numbers[0][0]


    # Пересчет начальных сумм строк и столбцов
    sum_strok, sum_stolb = recalculate_sums(generated_matrix)

    button_width = 50
    button_height = 50
    x_offset = 100
    y_offset = 100

    # Создание кнопок чисел
    for row_index, row in enumerate(generated_matrix):
        for col_index, value in enumerate(row):
            button_x = x_offset + col_index * (button_width + 10)
            button_y = y_offset + row_index * (button_height + 10)
            button_rect = button(screen, button_x, button_y, button_width, button_height, LIGHT_BLUE, str(value))
            buttons.append([button_rect, button_x, button_y, 'value', row_index, col_index, LIGHT_BLUE, str(value)])

    # Создание кнопок сумм строк
    for row_index, row_sum in enumerate(sum_strok):
        button_x_left = x_offset - (button_width + 10)
        button_y = y_offset + row_index * (button_height + 10)
        button_rect_left = button(screen, button_x_left, button_y, button_width, button_height, LIGHT_BLUE, str(row_sum))
        buttons.append([button_rect_left, button_x_left, button_y, 'row_sum', row_index, 'left', LIGHT_BLUE, str(row_sum)])

        button_x_right = x_offset + len(generated_matrix[0]) * (button_width + 10)
        button_rect_right = button(screen, button_x_right, button_y, button_width, button_height, LIGHT_BLUE, str(row_sum))
        buttons.append([button_rect_right, button_x_right, button_y, 'row_sum', row_index, 'right', LIGHT_BLUE, str(row_sum)])

    # Создание кнопок сумм столбцов
    for col_index, col_sum in enumerate(sum_stolb):
        button_x = x_offset + col_index * (button_width + 10)
        button_y_top = y_offset - (button_height + 10)
        button_rect_top = button(screen, button_x, button_y_top, button_width, button_height, LIGHT_BLUE, str(col_sum))
        buttons.append([button_rect_top, button_x, button_y_top, 'col_sum', col_index, 'top', LIGHT_BLUE, str(col_sum)])

        button_y_bottom = y_offset + len(generated_matrix) * (button_height + 10)
        button_rect_bottom = button(screen, button_x, button_y_bottom, button_width, button_height, LIGHT_BLUE, str(col_sum))
        buttons.append([button_rect_bottom, button_x, button_y_bottom, 'col_sum', col_index, 'bottom', LIGHT_BLUE, str(col_sum)])

    pygame.display.flip()

    # Главный игровой цикл
    while not in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, (button_rect, x, y, index_type, index, position, color, text) in enumerate(buttons):
                    if button_rect.collidepoint(mouse_pos):
                        if color == RED and index_type == "value":
                            buttons[i][6] = LIGHT_BLUE
                        if color == LIGHT_BLUE and index_type == "value":
                            buttons[i][6] = RED
                        if index_type == 'value':
                            row = index
                            col = position
                            current_value = generated_matrix[row][col]
                            generated_matrix[row][col] = 0 if current_value != 0 else int(text)

                            # Пересчитываем суммы строк и столбцов
                            sum_strok, sum_stolb = recalculate_sums(generated_matrix)

                        elif index_type == 'row_sum' or index_type == 'col_sum':
                            # Обработка нажатия на кнопки сумм
                            if index_type == 'required_sum_row' or index_type == 'required_sum_col':
                                # Удаляем кнопку из списка
                                buttons.pop(i)
                                break  # Прерываем цикл, так как список изменился

                        if index_type == 'row_sum':  # Если нажата кнопка суммы строки
                            if position == 'left' or position == 'right':
                                row_index = index
                                # Вычисляем необходимую сумму для победы
                                required_sum = generated_numbers[4][0][row_index]
                                # Определяем координаты для новой кнопки
                                if position == 'left':
                                    new_button_x = button_rect.x - (button_width + 10)
                                if position == "right":
                                    new_button_x = button_rect.x + (button_width + 10)
                                new_button_y = button_rect.y

                                # Проверяем, существует ли уже кнопка с такой суммой
                                existing_button = next(
                                    (btn for btn in buttons if btn[3] == 'required_sum_row' and btn[4] == row_index),
                                    None
                                )
                                if not existing_button:
                                    # Создаём кнопку с необходимой суммой
                                    new_button_rect = button(screen, new_button_x, new_button_y, button_width,
                                                             button_height,
                                                             LIGHT_BLUE, str(required_sum))
                                    buttons.append(
                                        [new_button_rect, new_button_x, new_button_y, 'required_sum_row', row_index,
                                         position, LIGHT_BLUE, str(required_sum)])

                        elif index_type == 'col_sum':  # Если нажата кнопка суммы столбца
                            if position == 'top' or position == 'bottom':
                                col_index = index
                                # Вычисляем необходимую сумму для победы
                                required_sum = generated_numbers[3][0][col_index]
                                # Определяем координаты для новой кнопки
                                if position == 'top':
                                    new_button_x = button_rect.x
                                    new_button_y = button_rect.y - (button_height + 10)
                                else:
                                    new_button_x = button_rect.x
                                    new_button_y = button_rect.y + (button_height + 10)

                                # Проверяем, существует ли уже кнопка с такой суммой
                                existing_button = next(
                                    (btn for btn in buttons if btn[3] == 'required_sum_col' and btn[4] == col_index),
                                    None
                                )

                                if not existing_button:
                                    # Создаём кнопку с необходимой суммой
                                    new_button_rect = button(screen, new_button_x, new_button_y, button_width,
                                                             button_height,
                                                             LIGHT_BLUE, str(required_sum))
                                    buttons.append(
                                        [new_button_rect, new_button_x, new_button_y, 'required_sum_col', col_index,
                                         position, LIGHT_BLUE, str(required_sum)])

        # Проверяем, если все суммы строк и столбцов равны необходимым суммам
        row_sums_match = all(
            sum(generated_matrix[row]) == generated_numbers[4][0][row] for row in range(len(generated_matrix))
        )
        col_sums_match = all(
            sum(generated_matrix[row][col] for row in range(len(generated_matrix))) == generated_numbers[3][0][col]
            for col in range(len(generated_matrix[0]))
        )

        # Если суммы строк и столбцов совпадают с необходимыми, выходим в меню
        if row_sums_match and col_sums_match:
            print("Условия выполнены, выход в меню.")
            # Здесь вызывается функция для перехода в меню или завершения игры
            in_menu = True  # или используйте вызов функции для выхода в меню

        # Обновление экрана
        screen.fill(WHITE)
        for button_rect, x, y, index_type, index, position, color, text in buttons:
            if index_type == 'row_sum':
                label = str(sum_strok[index])
            elif index_type == 'col_sum':
                label = str(sum_stolb[index])
            else:
                label = text
            button(screen, x, y, button_width, button_height, color, label)
        pygame.display.flip()


# Основной цикл программы
running = True
in_menu = True

while running:
    while True:
        if in_menu:
            menu()
        else:
            game()
pygame.quit()  # Завершение работы Pygame

