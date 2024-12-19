import pygame
import sys
from button import button
from draw_text import draw_text

pygame.init()

Dark_grey = (33, 36, 43)
BLACK = (0, 0, 0)
Green = (12, 157, 88)
Dark_grey_buttun = (24, 23, 28)
BLUE = (0, 0, 255)
Grey = (60, 63, 69)
font = pygame.font.Font(None, 36)
in_vbr = True

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
in_menu = True

col = 0
strok = 0
mini = 0
maxi = 0


def vbr():
    global in_vbr, col, strok
    buttons = []
    screen.fill(BLACK)
    text = ['5x5', '5x6', '6x6', '6x7', '7x7', '7x8', '8x8']
    text1 = ['1x19', '1x4', '10x20']
    button_rect = button(screen, 250, 90, 100, 100, Dark_grey_buttun, text1[0])
    buttons.append([button_rect, text1[0], Dark_grey_buttun])
    button_rect = button(screen, 370, 90, 100, 100, Grey, text1[1])
    buttons.append([button_rect, text1[1], Grey])
    button_rect = button(screen, 290, 700, 250, 50, Grey, 'Таблица лидеров')
    buttons.append([button_rect, 'Таблица лидеров', Grey])
    button_rect = button(screen, 490, 90, 100, 100, Grey, text1[2])
    buttons.append([button_rect, text1[2], Grey])
    x = 250
    y = 300
    for i in text:
        x += 120
        if x == 250 + 120 * 3:
            x = 250
            y += 120
        button_rect = button(screen, x, y, 100, 100, Grey, i)
        buttons.append([button_rect, i, Grey])
    pygame.display.flip()
    while in_vbr:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, (button_rect, text_button, color) in enumerate(buttons):
                    if button_rect.collidepoint(mouse_pos):
                        if text_button == "Таблица лидеров":
                            return [True]
                        # Проверка, нажата ли кнопка
                        if text_button in text1:
                            buttons[0][2] = Grey
                            buttons[1][2] = Grey
                            buttons[2][2] = Grey
                            buttons[i][2] = Dark_grey_buttun
                        for text_maciv in text:
                            if text_button == text_maciv:  # Проверяем соответствие текста
                                for i, (button_rect1, text_button1, color1) in enumerate(buttons):

                                    if color1 == Dark_grey_buttun:
                                        text_button1 = text_button1.split('x')
                                        mini = int(text_button1[0])
                                        maxi = int(text_button1[1])
                                col = int(text_button[0])
                                strok = int(text_button[2])
                                print(col, strok, mini, maxi)
                                return [col, strok, False, mini, maxi]

        # Отрисовка всех кнопок после изменения цвета
        screen.fill(Dark_grey)
        draw_text("select number of numbers", font, BLACK, screen, screen_width // 2 + 25, 50)
        draw_text("playing fields", font, BLACK, screen, screen_width // 2 + 25, screen_height // 2 - 130)

        for button_rect, text_button, color in buttons:
            button(screen, button_rect.x, button_rect.y, button_rect.width, button_rect.height, color, text_button)
        pygame.display.flip()
