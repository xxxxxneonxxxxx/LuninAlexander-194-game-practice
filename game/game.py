from math_file import chis
from button import button
from draw_text import draw_text
from mune import menu
from vbr_chis import vbr
from datetime import datetime
from CRUD import *





import sqlite3
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
screen_width =800  # Начальная ширина экрана
screen_height = 800# Начальная высота экрана
# Глобальная переменная для хранения сгенерированных чисел
generated_numbers = []
in_menu=True
# Цвета
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
# Главная функция игры
def game(user_name):
    print(4123214121)
    global screen, in_vbr,col,strok,mini,maxi
    buttons = []
    def recalculate_sums(matrix):
        row_sums = [sum(row) for row in matrix]
        col_sums = [sum(col) for col in zip(*matrix)]
        return row_sums, col_sums
    # Инициализация данных
    generated_numbers = chis(col, strok, mini, maxi)
    for i in range(len(generated_numbers)):
        print(generated_numbers[i])
    generated_matrix = generated_numbers[2]
    # Пересчет начальных сумм строк и столбцов
    sum_strok, sum_stolb = recalculate_sums(generated_matrix)
    if (col ==6 or col==5) and (strok==5 or strok==6):
        button_width = 55
        button_height = 55
        x_offset = 145
        y_offset = 145
    if (col ==6 or col==7 ) and (strok==7):
        button_width = 55
        button_height = 55
        x_offset = 153
        y_offset = 155
    if (col ==8 or col==7 ) and (strok==8):
        button_width = 55
        button_height = 55
        x_offset = 148
        y_offset = 150
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
    start_time=(datetime.now())
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

                        elif index_type == 'required_sum_row' or index_type == 'required_sum_col':
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
            end_time=(datetime.now())
            timee=(end_time-start_time)
            time_baza=''
            timee=str(timee).split(":")
            for i in timee:
                if i=='0' or i=='00':
                    continue
                if i==timee[2]:
                    i=i[0]+i[1]+i[2]+i[3]+i[4]+i[5]
                if timee[1][0]=="0":
                    i=i[1]
                time_baza+=':'+i
            time_baza=time_baza[1:]
            add_time(user_name,time_baza,str(col)+"X"+str(strok))
            PRINT_TABLE_TIME()
            # Здесь вызывается функция для перехода в меню или завершения игры
            in_vbr=True

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
col=0
strok=0
mini=0
maxi=0
running = True
in_menu = True  # Флаг для определения, нужно ли показывать меню
in_vbr = False  # Флаг для определения, нужно ли показывать окно vbr

while running:
    if in_menu:  # Если флаг in_menu включен, показываем меню
        h = menu()  # Предполагается, что menu() возвращает нужные данные
        in_menu = False  # Отключаем показ меню
        in_vbr = True  # Включаем показ окна vbr после меню
    elif in_vbr:  # Если в режиме выбора (vbr)
        a = vbr()  # Предполагается, что vbr() возвращает необходимые данные
        in_vbr = a[2]  # Обновляем флаг in_vbr
        col, strok, mini, maxi = a[0], a[1], a[3], a[4]
    else:  # Если не в меню и не в выборе, запускаем игру
        game(h[1])  # Передаём нужные данные в game()
        in_vbr = True  # После игры возвращаемся в окно выбора


pygame.quit()  # Завершение работы Pygame

