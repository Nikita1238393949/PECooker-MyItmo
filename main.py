import threading
import time
import tkinter as tk
from datetime import datetime, timedelta  # Добавлен импорт timedelta
from tkinter import messagebox
from tkinter import ttk

import requests


refresh_token = None
access_token = None
connection_label = None
refresh_button = None
bot_token = 'TOKEN'
chat_id = 1358241692
# Словарь для управления потоками мониторинга
monitoring_threads = {}


# Функция для отправки запроса на запись на занятие
def sign_for_lesson(lesson_id):
    url = "https://my.itmo.ru/api/sport/my_sport/sign_for_lesson"
    headers = {'Authorization': f'Bearer {access_token}'}
    data = [lesson_id]
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка при записи на занятие: {response.text}")
        return None

# Функция для отправки сообщения в телеграм
def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    return response.json()


# Функция мониторинга занятий
def monitor_lessons(lesson_id, stop_event):
    while not stop_event.is_set():
        response_data = sign_for_lesson(lesson_id)
        if response_data and response_data.get("error_code") == 0:
            send_telegram_message(bot_token, chat_id,
                                  f"Вы успешно записаны на занятие {lesson_id}! credits: @googleadsusd")
            stop_event.set()
        elif response_data:
            print(f"Попытка записи на занятие {lesson_id} не удалась, пытаемся снова...")
        time.sleep(10)


def start_monitoring():
    if not lessons_list.selection():
        messagebox.showwarning("Внимание", "Не выбрано ни одного занятия.")
        return

    selected_item = lessons_list.selection()[0]
    lesson_id = lessons_list.item(selected_item)['values'][0]

    if lesson_id not in monitoring_threads:
        stop_event = threading.Event()
        thread = threading.Thread(target=monitor_lessons, args=(lesson_id, stop_event), daemon=True)
        monitoring_threads[lesson_id] = (thread, stop_event)
        thread.start()
        update_active_monitorings()
        messagebox.showinfo("Мониторинг", f"Мониторинг для занятия {lesson_id} запущен.")
    else:
        messagebox.showwarning("Внимание", f"Мониторинг для занятия {lesson_id} уже запущен.")


def stop_monitoring(lesson_id):
    if lesson_id in monitoring_threads:
        thread, stop_event = monitoring_threads[lesson_id]
        stop_event.set()
        thread.join()
        del monitoring_threads[lesson_id]
        messagebox.showinfo("Мониторинг", f"Мониторинг для занятия {lesson_id} остановлен.")
        update_active_monitorings()


def get_schedule(date_start, date_end, token):
    url = f"https://my.itmo.ru/api/sport/my_sport/schedule/available?date_start={date_start}&date_end={date_end}"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else {}


# Функция для получения лимитов с API
def get_limits(token):
    url = "https://my.itmo.ru/api/sport/my_sport/schedule/available/limits"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response.json()['result'] if response.status_code == 200 else {}


# Функция для обновления списка занятий
def update_lessons(date, data, limits):
    for item in lessons_list.get_children():
        lessons_list.delete(item)

    for day_info in data.get("result", []):
        if day_info["date"] == date:
            for lesson in day_info.get("lessons", []):
                lesson_id = str(lesson["id"])

                lesson_limit_info = None
                for section_limits in limits.values():
                    if lesson_id in section_limits:
                        lesson_limit_info = section_limits[lesson_id]
                        break
                if lesson_limit_info is None:
                    lesson_limit_info = {"limit": "Н/Д", "available": "Н/Д"}

                date_format = "%Y-%m-%dT%H:%M:%S%z"

                start_time = datetime.strptime(lesson["date"], date_format)
                end_time = datetime.strptime(lesson["date_end"], date_format)

                start_time_formatted = start_time.strftime("%H:%M")
                end_time_formatted = end_time.strftime("%H:%M")

                lessons_list.insert("", "end", values=(
                    lesson_id,
                    lesson["section_name"],
                    lesson["lesson_level_name"],
                    start_time_formatted,
                    end_time_formatted,
                    lesson["room_name"],
                    lesson["teacher_fio"].split()[0],
                    f"{lesson_limit_info['limit']} (Доступно: {lesson_limit_info['available']})"
                ))


# Функция для обновления данных
def refresh_data():
    selected_date = date_combobox.get()
    if not access_token or not selected_date:
        messagebox.showerror("Ошибка", "Введите refresh token и выберите дату")
        return

    data = get_schedule(selected_date, selected_date, access_token)
    limits = get_limits(access_token)
    update_lessons(selected_date, data, limits)


# Функция для обновления access_token используя refresh_token
def refresh_access_token():
    global refresh_token, access_token
    token_url = 'https://id.itmo.ru/auth/realms/itmo/protocol/openid-connect/token'
    data = {
        'client_id': 'student-personal-cabinet',
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        response_data = response.json()
        access_token = response_data['access_token']
        refresh_token = response_data.get('refresh_token', refresh_token)
        connection_label.config(text='Связь Есть', fg='green')
        date_combobox.config(state="readonly")
    else:
        connection_label.config(text='Связи Нет', fg='red')
        date_combobox.config(state="disabled")  # Сделать кнопку "Обновить" неактивной
        messagebox.showerror("Ошибка", f"Ошибка при обновлении токена: {response.text}")


# Функция для установки связи
def establish_connection():
    global refresh_token
    refresh_token = refresh_token_entry.get()
    if not refresh_token:
        messagebox.showerror("Ошибка", "Введите refresh token.")
        return
    refresh_access_token()
    threading.Thread(target=token_refresh_schedule, daemon=True).start()


# Функция расписания автоматического обновления токена
def token_refresh_schedule():
    while True:
        threading.Event().wait(1740)
        refresh_access_token()


# Основное окно
root = tk.Tk()
root.title("Digital Fusion V0.9 Pre-Release: @googleadsusd")

button_frame = ttk.Frame(root)
button_frame.pack(fill='x', padx=5, pady=5)

refresh_token_label = ttk.Label(button_frame, text="Введите refresh_token:")
refresh_token_label.pack(side='left', padx=5)

refresh_token_entry = ttk.Entry(button_frame, width=20)
refresh_token_entry.pack(side='left', padx=5)

connect_button = ttk.Button(button_frame, text="Установить связь", command=establish_connection)
connect_button.pack(side='left', padx=5)

connection_label = tk.Label(button_frame, text='Связи Нет', fg='red')
connection_label.pack(side='left', padx=5)

start_monitoring_button = ttk.Button(button_frame, text="Запустить мониторинг", command=start_monitoring)
start_monitoring_button.pack(side='left', padx=5)

columns = ("ID", "Название секции", "Уровень", "Начало", "Конец", "Аудитория", "Преподаватель", "Лимиты")
lessons_list = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    lessons_list.heading(col, text=col)
    if col in ["Начало", "Конец"]:
        lessons_list.column(col, width=20)
    elif col == "ID":
        lessons_list.column(col, width=30)
    else:
        lessons_list.column(col, width=100)

lessons_list.pack(expand=True, fill="both", padx=5, pady=5)

today = datetime.now()
two_weeks_later = today + timedelta(days=14)

date_list = [today + timedelta(days=i) for i in range((two_weeks_later - today).days + 1)]

dates = [date.strftime("%Y-%m-%d") for date in date_list]

date_combobox = ttk.Combobox(root, values=dates)
date_combobox.pack()
date_combobox.config(state="disabled")
date_combobox.bind('<<ComboboxSelected>>', lambda event: refresh_data())

monitoring_frame = ttk.LabelFrame(root, text="Активные мониторинги")
monitoring_frame.pack(fill="x", padx=5, pady=5)


# Функция для обновления отображения активных мониторингов
def update_active_monitorings():
    for widget in monitoring_frame.winfo_children():
        widget.destroy()

    for lesson_id, (thread, _) in monitoring_threads.items():
        if thread.is_alive():
            label = ttk.Label(monitoring_frame, text=f"Мониторинг {lesson_id}")
            label.pack(side="top", fill="x")
            stop_button = ttk.Button(label, text="Остановить", command=lambda lid=lesson_id: stop_monitoring(lid))
            stop_button.pack(side="right")


update_active_monitorings()

root.mainloop()
