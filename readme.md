## Приложение "Погода"
Это простое приложение для отображения погоды, которое получает данные о погоде из API OpenWeatherMap и выводит их в графическом интерфейсе, построенном с помощью Tkinter. Пользователи могут вводить название города и код страны, чтобы получить текущую информацию о погоде.

## Предварительные требования
1. Python 3.x
2. Библиотека Tkinter
3. Библиотека Requests
4. API-ключ OpenWeatherMap
5. Тема sv_ttk для Tkinter, папку с темой можете найти в репозитории. Для установки темы нужно также ввести комманду pip install sv-ttk в терминале.

## Использование
1. Запустите скрипт.
2. Введите название города и код страны (разделенные запятой) в поле ввода.
3. Нажмите кнопку "Запрос погоды".
Информация о погоде для указанного местоположения будет отображена в окне приложения.

## Функциональность
Получает данные о погоде в реальном времени из API OpenWeatherMap.
Отображает температуру, влажность, скорость ветра, описание погоды, время восхода и заката.
Предоставляет сообщения об ошибках при неверных вводах или проблемах с получением данных.
