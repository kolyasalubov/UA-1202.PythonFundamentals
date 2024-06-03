import pygame
import random

FPS = 60

WIDTH_DISPLAY = 850
HEIGHT_DISPLAY = 400

BLACK = (0, 0, 0)

pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))

pygame.display.set_caption("Guess the number")
clock = pygame.time.Clock()

pygame.display.update()

font = pygame.font.SysFont("Arial", 50)

user_input = ""
input_active = True

running = True

random_number = random.randint(1, 100)
attempts = 10


def check_user_input(user_number):
    user_number = int(user_number)
    if user_number > random_number:
        return f"{user_input} > the number. Press any key to continue"
    elif user_number < random_number:
        return f"{user_input} < the number. Press any key to continue"
    elif user_number == random_number:
        return "The number is correct. Congratulations!"


def print_text(text):
    gameDisplay.fill(BLACK)
    text_surf = font.render(text, True, (255, 0, 0))
    gameDisplay.blit(text_surf, text_surf.get_rect(center=gameDisplay.get_rect().center))
    pygame.display.flip()


print_text("Input text from 1 to 100: ")

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            user_input = ""

        if attempts == 0:
            input_active = False
            print_text("No attempts left. Close the game and try again")

        elif event.type == pygame.KEYDOWN and input_active:

            if event.key == pygame.K_RETURN:
                input_active = True
                print_text(check_user_input(user_input))
                user_input = ""
                attempts -= 1
                print(attempts)

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
                print_text("Input text from 1 to 100: " + user_input)
            else:
                user_input += event.unicode
                print_text("Input text from 1 to 100: " + user_input)

pygame.quit()
exit()
