from math_file import chis
from button import button
from mune import menu
from vbr_chis import vbr
from datetime import datetime
from input import input_us
from draw_text import draw_text
from tablica_liderow import table

import pygame
import sys

pygame.init()  #
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption("Game")

Dark_grey = (33, 36, 43)
BLACK = (0, 0, 0)
GREEN = (12, 157, 88)
Dark_grey_button = (24, 23, 28)
BLUE = (0, 0, 255)
BLACK_grey = (24, 23, 28)
Grey = (60, 63, 68)
font = pygame.font.Font(None, 36)
screen_width = 800
screen_height = 800
generated_numbers = []
in_menu = True


def finich(buttons, button_width, button_height, sum_strok, sum_stolb, user_name, a, h):
    global screen, in_vbr, col, strok, mini, maxi
    col = a[0]
    strok = a[1]
    if (col == 8 or col == 7) and (strok == 8):
        buttons.append([
            button(screen, 630, 700, 100, 100, Grey, "выход"), 650, 650, 'exit_button', "", '', Grey, "выход"
        ])
        buttons.append([
            button(screen, 0, 700, 100, 100, Grey, "заного"), 50, 650, 'return', "", '', Grey, "заного"
        ])
    else:
        buttons.append([
            button(screen, 630, 650, 100, 100, Grey, "выход"), 650, 650, 'exit_button', "", '', Grey, "выход"
        ])
        buttons.append([
            button(screen, 0, 650, 100, 100, Grey, "заного"), 50, 650, 'return', "", '', Grey, "заного"
        ])

    while True:
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
                        if index_type == "return":
                            print(1)
                            col, strok, mini, maxi = a[0], a[1], a[3], a[4]
                            game(user_name, a, h)
                        if index_type == 'exit_button':
                            return True
        screen.fill(Dark_grey)

        for button_rect, x, y, index_type, index, position, color, text in buttons:
            if index_type in ['return', 'exit_button']:
                button(screen, x, y, 100, 100, color, text)
            else:
                if index_type == 'required_sum_row':
                    label = str(sum_strok[index])
                elif index_type == 'required_sum_col':
                    label = str(sum_stolb[index])
                else:
                    label = text
                button(screen, x, y, button_width, button_height, color, label)
        if (col == 8 or col == 7) and (strok == 8):
            draw_text("ВЫ ВЫЙГРАЛИ", font, (255, 255, 255), screen, 400, 750)
        else:
            draw_text("ВЫ ВЫЙГРАЛИ", font, (255, 255, 255), screen, 400, 700)
        pygame.display.flip()


def game(user_name, a, h):
    global screen, in_vbr, col, strok, mini, maxi
    buttons = []
    types = str(col) + 'X' + str(strok)

    def recalculate_sums(matrix):
        row_sums = [sum(row) for row in matrix]
        col_sums = [sum(col) for col in zip(*matrix)]
        return row_sums, col_sums

    def update_colors(current_sum_row, current_sum_col):
        current_sum_row1 = [sum(row) for row in generated_matrix]
        current_sum_col1 = [sum(col) for col in zip(*generated_matrix)]
        for button_index, (_, _, _, btn_type, btn_index, _, _, btn_text) in enumerate(buttons):
            if btn_type == "row_sum" and btn_index <= len(current_sum_row):
                buttons[button_index][6] = GREEN if current_sum_row[btn_index] == current_sum_row1[
                    btn_index] else Grey
            elif btn_type == "col_sum" and btn_index <= len(current_sum_col):
                buttons[button_index][6] = GREEN if current_sum_col[btn_index] == current_sum_col1[
                    btn_index] else Grey

    generated_numbers = chis(col, strok, mini, maxi)
    generated_matrix = generated_numbers[2]
    current_sum_row = generated_numbers[4][0]
    current_sum_col = generated_numbers[3][0]

    sum_strok, sum_stolb = recalculate_sums(generated_matrix)
    if (col == 6 or col == 5) and (strok == 5 or strok == 6):
        button_width = 55
        button_height = 55
        x_offset = 220
        y_offset = 230
    if (col == 6 or col == 7) and (strok == 7):
        button_width = 55
        button_height = 55
        x_offset = 160
        y_offset = 200
    if (col == 8 or col == 7) and (strok == 8):
        button_width = 55
        button_height = 55
        x_offset = 155
        y_offset = 150
    button_rect_left = button(screen, 10, 10, button_width, button_height, Grey, "выход ")
    buttons.append(
        [button_rect_left, 10, 10, 'exit', "", '', Grey, "выход"])
    for row_index, row in enumerate(generated_matrix):
        for col_index, value in enumerate(row):
            button_x = x_offset + col_index * (button_width + 10)
            button_y = y_offset + row_index * (button_height + 10)
            button_rect = button(screen, button_x, button_y, button_width, button_height, Grey, str(value))
            buttons.append([button_rect, button_x, button_y, 'value', row_index, col_index, Grey, str(value)])
    for row_index, row_sum in enumerate(generated_numbers[4][0]):
        button_x_left = x_offset - (button_width + 10)
        button_y = y_offset + row_index * (button_height + 10)
        button_rect_left = button(screen, button_x_left, button_y, button_width, button_height, Grey,
                                  str(row_sum))
        buttons.append(
            [button_rect_left, button_x_left, button_y, 'row_sum', row_index, 'left', Grey, str(row_sum)])
        button_x_right = x_offset + len(generated_matrix[0]) * (button_width + 10)
        button_rect_right = button(screen, button_x_right, button_y, button_width, button_height, Grey,
                                   str(row_sum))
        buttons.append(
            [button_rect_right, button_x_right, button_y, 'row_sum', row_index, 'right', Grey, str(row_sum)])
    for col_index, col_sum in enumerate(generated_numbers[3][0]):
        button_x = x_offset + col_index * (button_width + 10)
        button_y_top = y_offset - (button_height + 10)
        button_rect_top = button(screen, button_x, button_y_top, button_width, button_height, Grey, str(col_sum))
        buttons.append([button_rect_top, button_x, button_y_top, 'col_sum', col_index, 'top', Grey, str(col_sum)])
        button_y_bottom = y_offset + len(generated_matrix) * (button_height + 10)
        button_rect_bottom = button(screen, button_x, button_y_bottom, button_width, button_height, Grey,
                                    str(col_sum))
        buttons.append(
            [button_rect_bottom, button_x, button_y_bottom, 'col_sum', col_index, 'bottom', Grey, str(col_sum)])
    update_colors(current_sum_row, current_sum_col)

    pygame.display.flip()
    start_time = (datetime.now())
    while not in_vbr:
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
                        if index_type == "exit":
                            in_vbr = True
                        if color == Dark_grey_button and index_type == "value":
                            buttons[i][6] = Grey
                        if color == Grey and index_type == "value":
                            buttons[i][6] = Dark_grey_button
                        if index_type == 'value':
                            row = index
                            col = position
                            current_value = generated_matrix[row][col]
                            generated_matrix[row][col] = 0 if current_value != 0 else int(text)
                            sum_strok, sum_stolb = recalculate_sums(generated_matrix)
                        elif index_type == 'required_sum_row' or index_type == 'required_sum_col':
                            buttons.pop(i)
                            break

                        if index_type == 'row_sum':  # Если нажата кнопка суммы строки
                            if position == 'left' or position == 'right':
                                row_index = index
                                required_sum = sum_strok[row_index]
                                if position == 'left':
                                    new_button_x = button_rect.x - (button_width + 10)
                                if position == "right":
                                    new_button_x = button_rect.x + (button_width + 10)
                                new_button_y = button_rect.y
                                existing_button = next(
                                    (btn for btn in buttons if btn[3] == 'required_sum_row' and btn[4] == row_index),
                                    None
                                )
                                if not existing_button:
                                    new_button_rect = button(screen, new_button_x, new_button_y, button_width,
                                                             button_height,
                                                             Grey, str(required_sum))
                                    buttons.append(
                                        [new_button_rect, new_button_x, new_button_y, 'required_sum_row', row_index,
                                         position, Grey, str(required_sum)])

                        elif index_type == 'col_sum':
                            if position == 'top' or position == 'bottom':
                                col_index = index
                                required_sum = sum_stolb[col_index]
                                if position == 'top':
                                    new_button_x = button_rect.x
                                    new_button_y = button_rect.y - (button_height + 10)
                                else:
                                    new_button_x = button_rect.x
                                    new_button_y = button_rect.y + (button_height + 10)
                                existing_button = next(
                                    (btn for btn in buttons if btn[3] == 'required_sum_col' and btn[4] == col_index),
                                    None
                                )

                                if not existing_button:
                                    new_button_rect = button(screen, new_button_x, new_button_y, button_width,
                                                             button_height,
                                                             Grey, str(required_sum))
                                    buttons.append(
                                        [new_button_rect, new_button_x, new_button_y, 'required_sum_col', col_index,
                                         position, Grey, str(required_sum)])
                    if index_type == "col_sum" or index_type == "row_sum":
                        update_colors(current_sum_row, current_sum_col)

        row_sums_match = all(
            sum(generated_matrix[row]) == generated_numbers[4][0][row] for row in range(len(generated_matrix))
        )
        col_sums_match = all(
            sum(generated_matrix[row][col] for row in range(len(generated_matrix))) == generated_numbers[3][0][col]
            for col in range(len(generated_matrix[0]))
        )
        if row_sums_match and col_sums_match:
            end_time = datetime.now()
            time_delta = (end_time - start_time)
            time_baza = str(time_delta).split(".")[0]
            try:
                input_us({
                    'message': 'add_time',
                    'user_name': user_name,
                    'time_baza': time_baza,
                    'type': types
                })
            except Exception as e:
                print(f"Ошибка при добавлении времени: {str(e)}")
            if finich(buttons, button_width, button_height, sum_strok, sum_stolb, user_name, a, h):
                in_vbr = True
            else:
                game(user_name, a, h)

        screen.fill(Dark_grey)
        for button_rect, x, y, index_type, index, position, color, text in buttons:
            if index_type == 'required_sum_row':
                label = str(sum_strok[index])
            elif index_type == 'required_sum_col':
                label = str(sum_stolb[index])
            else:
                label = text
            button(screen, x, y, button_width, button_height, color, label)
        pygame.display.flip()


col = 0
strok = 0
mini = 0
maxi = 0
running = True
in_menu = True
in_vbr = False
in_tablica_liderov = False
in_game = False

while running:
    if in_menu:  # Если флаг in_menu включен, показываем меню
        h = menu()  # Предполагается, что menu() возвращает нужные данные
        in_menu = False  # Меню выключаем
        in_vbr = True  # Переходим к выбору (vbr)
        in_tablica_liderov = False  # Таблица лидеров пока не показывается
    elif in_vbr:  # Если в режиме выбора (vbr)
        a = vbr()  # Предполагается, что vbr() возвращает список `a`
        if len(a) == 1:
            in_tablica_liderov = True  # Если `a` содержит только 1 элемент, переходим к таблице лидеров
            in_vbr = False  # Выход из режима выбора
            continue  # Пропускаем выполнение остального кода в этом цикле
        # Иначе переходим к игре
        in_vbr = a[2]  # Обновляем флаг in_vbr
        col, strok, mini, maxi = a[0], a[1], a[3], a[4]
    elif in_tablica_liderov:  # Если включен режим таблицы лидеров
        result = table()  # table() должна быть настроена для вывода таблицы лидеров
        if result == "back":  # Если ожидается команда "назад" из таблицы
            in_tablica_liderov = False  # Выход из таблицы лидеров
            in_vbr = True  # Возврат в режим выбора
        elif result == "exit":  # Если пользователь хочет выйти
            running = False  # Завершаем программу
    else:  # Условие для перехода в игру
        game(h[1], a, h)  # Передача данных из h и a
        in_vbr = True  # После игры возвращаемся в режим выбора

pygame.quit()  # Завершение работы Pygame
