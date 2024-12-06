import pygame
import sys
from button import button
from draw_text import draw_text

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)
in_vbr=True

# Параметры экрана
screen_width =800  # Начальная ширина экрана
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
in_menu = True


col=0
strok=0
mini=0
maxi=0
def vbr():
    global in_vbr, col, strok
    buttons = []
    screen.fill(BLACK)
    text = ['5x5', '5x6', '6x6', '6x7', '7x7', '7x8', '8x8']
    text1 =['1x19','1x4','10x20']
    button_rect = button(screen, 250, 90, 100, 100, RED, text1[0])
    buttons.append([button_rect, text1[0], RED])
    button_rect = button(screen, 370, 90, 100, 100, LIGHT_BLUE, text1[1])
    buttons.append([button_rect, text1[1], LIGHT_BLUE])
    button_rect = button(screen, 490, 90, 100, 100, LIGHT_BLUE, text1[2])
    buttons.append([button_rect, text1[2], LIGHT_BLUE])
    x = 250
    y = 300
    for i in text:
        x += 120
        if x == 250 + 120 * 3:
            x = 250
            y += 120
        button_rect = button(screen, x, y, 100, 100, LIGHT_BLUE, i)
        buttons.append([button_rect, i,LIGHT_BLUE])
    pygame.display.flip()
    while in_vbr:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, (button_rect, text_button, color) in enumerate(buttons):
                    if button_rect.collidepoint(mouse_pos):  # Проверка, нажата ли кнопка
                        if text_button in text1:
                            buttons[0][2]=LIGHT_BLUE
                            buttons[1][2]=LIGHT_BLUE
                            buttons[2][2]=LIGHT_BLUE
                            buttons[i][2] = RED
                        for text_maciv in text:
                            if text_button == text_maciv:# Проверяем соответствие текста
                                for i, (button_rect1, text_button1, color1) in enumerate(buttons):
                                    if color1==RED:
                                        text_button1=text_button1.split('x')
                                        mini=int(text_button1[0])
                                        maxi=int(text_button1[1])
                                col = int(text_button[0])
                                strok = int(text_button[2])
                                print(col,strok,mini,maxi)
                                return [col, strok, False,mini,maxi]

        # Отрисовка всех кнопок после изменения цвета
        screen.fill(WHITE)
        draw_text("select number of numbers", font, BLACK, screen, screen_width // 2+25, 50)
        draw_text("playing fields", font, BLACK, screen, screen_width // 2+25, screen_height // 2-130)


        # Очищаем экран (или используем фон)
        for button_rect, text_button, color in buttons:
            button(screen, button_rect.x, button_rect.y, button_rect.width, button_rect.height, color, text_button)
        pygame.display.flip()
