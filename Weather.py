from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sv_ttk
import ctypes
import requests
import time

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except Exception:
    pass

API_KEY = '9d6ac1ecc4e2a54360c7a7943a4ed855'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

root = Tk()
root.title('Weather')
root.iconbitmap(r'C:\Users\user\Desktop\курс питон записи\GPT_tasks\Weather\weather.ico')
root.config(bg='#323943')
root.geometry('500x400+1000+300')
root.resizable(False, False)

def print_weather(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        temp = weather['main']['temp']
        press = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        desc = weather['weather'][0]['description']
        sunrise_ts = weather['sys']['sunrise']
        sunset_ts = weather['sys']['sunset']
        sunrise_struct_time = time.localtime(sunrise_ts)
        sunrise = time.strftime('%H:%M', sunrise_struct_time)
        sunset_struct_time = time.localtime(sunset_ts)
        sunset = time.strftime('%H:%M', sunset_struct_time)
        return f'Location: {city}, {country}\nTemperature: {temp}°C\nHumidity: {humidity}%\n' \
               f'Wind speed: {wind}m/s\nWeather description: {desc}\nSunrise: {sunrise}\nSunset: {sunset}'
    except:
        return 'Data error...'



def get_weather():
    if not entry.get():
        messagebox.showwarning('Warning', 'Typy your request in a format: city, country_code')
    else:
        params = {
            'appid': API_KEY,
            'q': entry.get(),
            'units': 'metric',
        }
        r = requests.get(API_URL, params=params)
        weather = r.json()
        label['text'] = print_weather(weather)

top_frame = ttk.Frame(root)
top_frame.place(relx=.5, rely=.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = ttk.Entry(top_frame)
entry.place(relwidth=0.7, relheight=1)

button = ttk.Button(top_frame, text='Weather request', command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = ttk.Frame(root)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label = ttk.Label(lower_frame, anchor=NW, font='Arial 15')
label.place(relwidth=1, relheight=1)


sv_ttk.set_theme('dark')
root.mainloop()

