import tkinter as tk
from weather_utils import get_weather_data

HEIGHT = 100
WIDTH = 450

root = tk.Tk()


def get_weather(name):
    text1.config(text=f'Detailed status: {get_weather_data(name).get("clouds")}')
    text2.config(text=f'Wind speed: {get_weather_data(name).get("wind_speed")}, '
                      f'Wind direction: {get_weather_data(name).get("deg")}')
    text3.config(text=f'Humidity: {get_weather_data(name).get("humidity")}')
    text4.config(text=f'°C: max: {get_weather_data(name).get("temperature").get('temp_max')}, '
                      f'min: {get_weather_data(name).get("temperature").get('temp_min')}, '
                      f'avg: {get_weather_data(name).get("temperature").get('temp')}')
    text5.config(text=f'Rain: {get_weather_data(name).get("rain")}')
    text6.config(text=f'Clouds: {get_weather_data(name).get("clouds")}')

    text1.pack(padx=10, pady=10)
    text2.pack(padx=10, pady=10)
    text3.pack(padx=10, pady=10)
    text4.pack(padx=10, pady=10)
    text5.pack(padx=10, pady=10)
    text6.pack(padx=10, pady=10)


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

frame1 = tk.LabelFrame(text='Weather data', bg='gold', width=400, height=200)
frame1.pack()

text1 = tk.Label(frame1, text='', width=40, height=1, font=('Courier', 12))
text2 = tk.Label(frame1, text='', width=40, height=1, font=('Courier', 12))
text3 = tk.Label(frame1, text='', width=40, height=1, font=('Courier', 12))
text4 = tk.Label(frame1, text='', width=40, height=1, font=('Courier', 12))
text5 = tk.Label(frame1, text='', width=40, height=1, font=('Courier', 12))
text6 = tk.Label(frame1, text='', width=40, height=1, font=('Courier', 12))

root.mainloop()
