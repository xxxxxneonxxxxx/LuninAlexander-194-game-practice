import pygame
import sys
from button import *
from draw_text import *
from draw_text_input_bo import *
from input import input_us
from output import output_us

pygame.init()

# Определение цветов
Dark_grey = (33, 36, 43)
BLACK = (0, 0, 0)
GREEN = (12, 157, 88)
Dark_grey_button = (24, 23, 28)
BLUE = (0, 0, 255)
Grey = (60, 63, 69)

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
active_box = None


def menu():
    running = True
    global active_box
    show_yes_button = False
    success_message = ""
    while running:
        buttons = []
        screen.fill(Dark_grey)
        draw_text("Game Menu", font, BLACK, screen, screen_width // 2, 50)
        draw_text("login", font, BLACK, screen, screen_width // 2 - 145, screen_height // 2 - 40)
        draw_text("password", font, BLACK, screen, screen_width // 2 - 170, screen_height // 2 + 20)

        for field, rect in input_boxes.items():
            draw_text_input_box(
                screen, rect, texts[field], active_box == field
            )

        confirm_button = pygame.Rect(
            screen_width // 2 - 75, screen_height // 2 + 70, 150, 40
        )
        pygame.draw.rect(screen, GREEN, confirm_button)
        draw_text("Confirm", font, Dark_grey, screen, confirm_button.centerx, confirm_button.centery)

        if success_message:
            draw_text(
                success_message,
                font,
                Dark_grey_button if "no!" in success_message else GREEN,
                screen,
                screen_width // 2,
                screen_height // 2 + 140,
            )
        if show_yes_button:
            button_yes = button(screen, 230, 580, 125, 50, Grey, "YES")
            buttons.append([button_yes, 'yes'])
        if show_yes_button:
            button_yes = button(screen, 450, 580, 125, 50, Grey, "NO")
            buttons.append([button_yes, 'no'])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                active_box = None
                for field, rect in input_boxes.items():
                    if rect.collidepoint(event.pos):
                        active_box = field
                        break
                for button_rect, ind in buttons:
                    if button_rect.collidepoint(mouse_pos):
                        if ind == "yes":
                            try:
                                a = input_us({"message": "add_user", "nickname": texts["nickname"],
                                              "password": texts['password']})
                            except:
                                "error: add_user"
                            if a == "Failed to add user":
                                break
                            return [False, texts["nickname"]]
                        else:
                            show_yes_button = False
                            success_message = 'enter existing user'
                            buttons = []
                            screen.fill(Dark_grey)
                            texts["nickname"] = ''
                            texts['password'] = ''
                if confirm_button.collidepoint(event.pos):
                    try:
                        a = output_us(
                            {'message': "READ_PROV", 'nickname': texts["nickname"], "password": texts["password"]})
                    except:
                        "error: READ_PROV"
                    if a['message'] == "ok":

                        return [False, texts["nickname"]]
                    else:
                        success_message = "want to add an account"
                        show_yes_button = True
            if event.type == pygame.KEYDOWN and active_box:
                if event.key == pygame.K_BACKSPACE:
                    texts[active_box] = texts[active_box][:-1]
                else:
                    texts[active_box] += event.unicode

        pygame.display.flip()
