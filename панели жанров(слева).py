import tkinter as tk

root = tk.Tk()
root.title("Выбор жанра")
root.geometry("720x480")

genre_frame = tk.Frame(root)
genre_frame.pack(side=tk.LEFT, padx=10, pady=10)


genres = ["Фантастика", "Драма", "Комедия", "Ужасы", "Приключения","Боевик","Фэнтази","Биографический","Мультфильм","Триллер ","Военный","Детектив","Криминал","Вестерн"]

for genre in genres:
    button = tk.Button(genre_frame, text=genre)
    button.pack(fill=tk.X, padx=10,pady=10)


text_frame = tk.Frame(root)
text_frame.pack(side=tk.RIGHT, padx=20, pady=20)
root.mainloop()

