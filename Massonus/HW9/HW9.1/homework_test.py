import pygame
import random

FPS = 60

WIDTH_DISPLAY = 700
HEIGHT_DISPLAY = 400

BLACK = (0, 0, 0)

pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))

pygame.display.set_caption("Homework test")
clock = pygame.time.Clock()

pygame.display.update()

font = pygame.font.SysFont("Arial", 50)

user_input = ""
input_active = True

running = True

random_number = random.randint(1, 100)


def check_user_input(user_number):
    user_number = int(user_number)
    if user_number > random_number:
        return "The number is too high"
    elif user_number < random_number:
        return "The number is too low"
    elif user_number == random_number:
        return "The number is correct. Congratulations!"


while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            user_input = ""

        elif event.type == pygame.KEYDOWN and input_active:

            if event.key == pygame.K_RETURN:
                input_active = False

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]

            else:
                user_input += event.unicode

    gameDisplay.fill(BLACK)
    text_surf = font.render("Input number from 1 to 100: " + user_input, True, (255, 0, 0))
    gameDisplay.blit(text_surf, text_surf.get_rect(center=gameDisplay.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()
