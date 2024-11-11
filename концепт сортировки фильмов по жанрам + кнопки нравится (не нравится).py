import tkinter as tk
from tkinter import messagebox



def show_movies(genre):
    # Словарь с жанрами и соответствующими фильмами
    movies = {
        "Фантастика": ["Cтеклянный город", "Гравитация", "Мстители: Война бесконечности", "Черная пантера", "Звездные войны: Пробуждение силы", "Начало", "Аватар", "Мстители", "Голодные игры", "Тор", "Человек-паук: Возвращение домой"],
        "Драма": ["Касабланка","Гражданин Кейн","Помни моя имя","Звездный вояджер","Паразиты","Джокер","Власть Пса","Боевой конь","Забытые песни"],
        "Комедия": ["Доктор Стрейнджлав", "Ночь в музеи пробуждение", "Последний пират"],
        "Ужасы": ["Новое поколение","Ведьма из Блэр: Курсовая с того света"],
        "Приключения": ["Лоуренс Аравийский","Хроники времени","Жизнь Пи"],
        "Боевик": ["Черная вдова","Тёмный рыцарь"],
        "Биографический": ["Человек на луне","Зеленная книга","Волк с Уолл-стрит"],
        "Фэнтази": ["Сердце дракона","Властелин колец: Братство кольца","Пираты Карибского моря: Проклятие Черной жемчужины"],
        "Мультфильм":["Кролик Джоао","Душа","Шрек","Би Муви","Рога и копыта","Роботы"],
        "Триллер": ["Тень на горизонте","Скрытая угроза"],
        "Военный": ["1917",],
        "Детектив": ["Психо", "Малхолланд Драйв"],
        "Криминал": ["Крестный отец"],
        "Вестерн": ["Великолепная семерка"],
        "Семейнный":["Кристофер Робин"]
    }
    
    # Получаем список фильмов для выбранного жанра
    selected_movies = movies.get(genre, [])
    
    # Очищаем список перед отображением новых фильмов
    movie_listbox.delete(0, tk.END)
    
    # Обновляем список с выбранными фильмами
    movie_listbox.insert(tk.END, f"Выбранный жанр: \n{genre}")
    for movie in selected_movies:
        movie_listbox.insert(tk.END, movie)

def like_movie():
    selected_index = movie_listbox.curselection()
    if selected_index:
        movie = movie_listbox.get(selected_index)
        messagebox.showinfo("Нравится", f"Вы выбрали: {movie}") 
    else:
        messagebox.showwarning("Предупреждение", "Сначала выберите фильм!")

def dislike_movie():
    selected_index = movie_listbox.curselection()
    if selected_index:
        movie = movie_listbox.get(selected_index)
        messagebox.showinfo("Не нравится", f"Вы выбрали: {movie}")
    else:
        messagebox.showwarning("Предупреждение", "Сначала выберите фильм!")

root = tk.Tk()
root.title("Выбор жанра")
root.geometry("720x480")

welcome_label = tk.Label(root, text="Привет, ты попал в Фильмотеку! Что посмотрим?", font=("Arial", 18))
welcome_label.pack(pady=10)

genre_frame = tk.Frame(root)
genre_frame.pack(side=tk.LEFT, padx=10, pady=10)

genres = ["Фантастика", "Драма", "Комедия", "Ужасы", "Приключения", "Боевик", "Фэнтази", "Биографический", "Мультфильм", "Триллер", "Военный", "Детектив", "Криминал", "Вестерн","Семейнный"]

for genre in genres:
    button = tk.Button(genre_frame, text=genre, command=lambda g=genre: show_movies(g))
    button.pack(fill=tk.X, padx=10, pady=10)

text_frame = tk.Frame(root)
text_frame.pack(side=tk.LEFT, padx=20, pady=20)

# Создаем Listbox для отображения фильмов
movie_listbox = tk.Listbox(text_frame, font=("Arial", 16), width=80, height=20)
movie_listbox.pack()

# Кнопки "Нравится" и "Не нравится"
like_button = tk.Button(text_frame, text="Нравится", command=like_movie, bg='green', fg='white')
like_button.pack(pady=3)

dislike_button = tk.Button(text_frame, text="Не нравится", command=dislike_movie, bg='red', fg='white')
dislike_button.pack(pady=3)


root.geometry("1000x600")
root.mainloop()

    