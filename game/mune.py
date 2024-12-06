import pygame
import sys
from CRUD import *
from button import *
from draw_text import *
from draw_text_input_bo import *

pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
GRAY = (200, 200, 200)

font = pygame.font.Font(None, 36)

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Game Menu")

input_boxes = {
    "nickname": pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 60, 200, 40),
    "password": pygame.Rect(screen_width // 2 - 100, screen_height // 2, 200, 40),
}
texts = {"nickname": "", "password": ""}
active_box = None  # Текущая активная зона ввода

def menu():
    running = True
    global active_box
    show_yes_button = False  # Флаг для отображения кнопки "yes"
    success_message = ""
    while running:
        buttons=[]
        screen.fill(WHITE)
        draw_text("Game Menu", font, BLACK, screen, screen_width // 2, 50)
        draw_text("login", font, BLACK, screen, screen_width // 2-145, screen_height // 2 -40)
        draw_text("password", font, BLACK, screen, screen_width // 2-170, screen_height // 2 +20)

        # Отображение полей ввода
        for field, rect in input_boxes.items():
            draw_text_input_box(
                screen, rect, texts[field], active_box == field
            )

        # Отображение кнопки подтверждения
        confirm_button = pygame.Rect(
            screen_width // 2 - 75, screen_height // 2 + 70, 150, 40
        )
        pygame.draw.rect(screen, GREEN, confirm_button)
        draw_text("Confirm", font, WHITE, screen, confirm_button.centerx, confirm_button.centery)

        # Отображение сообщения успеха или ошибки
        if success_message:
            draw_text(
                success_message,
                font,
                RED if "no!" in success_message else GREEN,
                screen,
                screen_width // 2,
                screen_height // 2 + 140,
            )

        # Отображение кнопки "yes", если она активна
        if show_yes_button:
            button_yes=button(screen,230,580,125,50,LIGHT_BLUE,"YES")
            buttons.append([button_yes,'yes'])
        if show_yes_button:
            button_yes=button(screen,450,580,125,50,LIGHT_BLUE,"NO")
            buttons.append([button_yes,'no'])
        pygame.display.flip()
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Проверяем, активны ли поля ввода
                active_box = None
                for field, rect in input_boxes.items():
                    if rect.collidepoint(event.pos):
                        active_box = field
                        break
                for button_rect,ind in buttons:
                    if button_rect.collidepoint(mouse_pos):
                        if ind=="yes":
                            add_user(texts["nickname"],texts['password'])
                            print(PRINT_TABLE_USERS())
                            return [False,texts["nickname"]]
                        else:
                            show_yes_button=False
                            success_message='enter existing user'
                            buttons=[]
                            screen.fill(WHITE)
                            texts["nickname"]=''
                            texts['password']=''
                # Проверяем нажатие на кнопку подтверждения
                if confirm_button.collidepoint(event.pos):
                    if not READ_PROV(texts["nickname"], texts["password"]):
                        success_message = "want to add an account"
                        show_yes_button = True  # Включаем отображение кнопки "yes"
                    else:
                        return [False,texts["nickname"]]
                # Обработка нажатия на кнопку "yes"
            if event.type == pygame.KEYDOWN and active_box:
                # Ввод текста
                if event.key == pygame.K_BACKSPACE:
                    texts[active_box] = texts[active_box][:-1]
                else:
                    texts[active_box] += event.unicode

        pygame.display.flip()

