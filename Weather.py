# Импорт необходимых библиотек

from tkinter import *  # Импортируем модуль для создания графического интерфейса
from tkinter import ttk  # Импортируем ttk для стилизации виджетов
from tkinter import messagebox  # Импортируем messagebox для вывода сообщений
import sv_ttk  # Импортируем стилизацию sv_ttk
import ctypes  # Импортируем ctypes для работы с DPI
import requests  # Импортируем requests для отправки HTTP-запросов
import time  # Импортируем time для работы с временем
import APIkey  # Импортируем API ключ

# Устанавливаем DPI, если возможно
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except Exception:
    pass

# API ключ и URL для запросов о погоде
API_KEY = APIkey.API
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Создаем главное окно приложения
root = Tk()
root.title('Weather')  # Задаем название окна
root.iconbitmap(r'C:\Users\user\Desktop\курс питон записи\GPT_tasks\Weather\weather.ico')  # Задаем иконку окна
root.config(bg='#323943')  # Задаем цвет фона
root.geometry('500x400+1000+300')  # Устанавливаем размеры окна
root.resizable(False, False)  # Запрещаем изменение размеров окна

# Функция для вывода информации о погоде
def print_weather(weather):
    try:
        # Извлекаем данные о погоде из JSON-ответа
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
        # Форматируем информацию о погоде
        return f'Location: {city}, {country}\nTemperature: {temp}°C\nHumidity: {humidity}%\n' \
               f'Wind speed: {wind}m/s\nWeather description: {desc}\nSunrise: {sunrise}\nSunset: {sunset}'
    except:
        return 'Data error...'

# Функция для получения информации о погоде по запросу пользователя
def get_weather():
    if not entry.get():
        # Если пользователь не ввел город, выводим предупреждение
        messagebox.showwarning('Warning', 'Typy your request in a format: city, country_code')
    else:
        # Формируем параметры для запроса о погоде
        params = {
            'appid': API_KEY,
            'q': entry.get(),
            'units': 'metric',
        }
        # Отправляем HTTP-запрос к API о погоде
        r = requests.get(API_URL, params=params)
        weather = r.json()  # Получаем ответ в формате JSON
        label['text'] = print_weather(weather)  # Выводим информацию о погоде на экран

# Создаем верхний фрейм для ввода запроса о погоде
top_frame = ttk.Frame(root)
top_frame.place(relx=.5, rely=.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = ttk.Entry(top_frame)  # Поле для ввода запроса
entry.place(relwidth=0.7, relheight=1)

button = ttk.Button(top_frame, text='Weather request', command=get_weather)  # Кнопка для отправки запроса
button.place(relx=0.7, relwidth=0.3, relheight=1)

# Создаем нижний фрейм для отображения информации о погоде
lower_frame = ttk.Frame(root)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label = ttk.Label(lower_frame, anchor=NW, font='Arial 15')  # Метка для вывода информации о погоде
label.place(relwidth=1, relheight=1)

sv_ttk.set_theme('dark')  # Устанавливаем тему стилизации для ttk виджетов
root.mainloop()  # Запускаем главный цикл событий Tkinter

