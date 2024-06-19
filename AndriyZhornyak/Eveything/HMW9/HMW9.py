#Task1
import random 
number = (random.randint(1, 100))
count = 0
while count <= 9:
    ask = float(input("Guess the number: "))
    count+=1
    if ask == number:
        print("Congratulate,you guessed the number:", number)
        break
    elif ask > number:
           print("The number number is lower")
    elif ask < number:
           print("The number number is higher")
#  Task PYGAME
import pygame

FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

WHITE_COLOR = (255, 255, 255)	
ORANGE_COLOR = (255, 150, 100)

COORD_X=0
COORD_Y=0
WIDTH_RECTANGLE=40
HEIGHT_RECTANGLE=60
DELTA_STEP=5
 
pygame.init()

gameDisplay=pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))

pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(10)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()

    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and COORD_X>DELTA_STEP:
        COORD_X=COORD_X-DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X<WIDTH_DISPLAY-WIDTH_RECTANGLE-DELTA_STEP:
        COORD_X=COORD_X+DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y>DELTA_STEP:
        COORD_Y=COORD_Y-DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y<HEIGHT_DISPLAY-HEIGHT_RECTANGLE-DELTA_STEP:
        COORD_Y=COORD_Y+DELTA_STEP

    gameDisplay.fill((0,0,0)) 

    pygame.draw.rect(gameDisplay, (ORANGE_COLOR), [COORD_X, 
                                        COORD_Y, 
                                        WIDTH_RECTANGLE, 
                                        HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
 Task OWM   
import tkinter as tk
import requests

API_KEY = 'ef2206ff5da67de63306d0b143e20872' 


HEIGHT = 500
WIDTH = 600


def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = round((weather['main']['temp']-32)/1.8, 2)
        final_str = f'City: {name} \nConditions: {description} \nTemperature : {temperature} C' 
    except:
        final_str = '''Oops!!! There was a problem\n retrieving that information.'''

    return final_str




def get_weather(city):
    weather_key = API_KEY
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    respons
    format_response(weather)e = requests.get(url, params)
    weather = response.json()

    label['text'] = format_response(weather)




root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather APP")
canvas.pack()



frame = tk.Frame(root, bg="#87cefa", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 18))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 12), 
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='#90c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 18))
label.place(relx=0, rely=0, relwidth=1, relheight=1)
