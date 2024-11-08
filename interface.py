from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import Button
# import maindb

def addfilm():
   newfilm = Toplevel(window)
   newfilm.title("Добавление нового фильма")
   newfilm.geometry('600x600')
   addfcan = Canvas(newfilm, width=600, height=600, bg='#9c6a75')
   addfcan.pack(fill='both', expand=True)
   addfcan.create_text(300,35, text='Введите данные о фильме в каждую из ячеек\nа затем нажмите отправить.', font=font2)
   nameLabel = Label(addfcan,text='Название:', width = 15,padx=10).place(x=30, y=70)
   nameEntry = Entry(addfcan).place(x=170,y=70)
   genreLabel = Label(addfcan,text='Жанр:', width = 15,padx=10).place(x=30, y=100)
   genreEntry = ttk.Combobox(addfcan, values=['Драма','Комедия', 'Фантиастика', 'Ужасы', 'Приключения', 'Боевик']).place(x=170,y=100)
   yearLabel = Label(addfcan,text='Год создания:', width = 15,padx=10).place(x=30, y=130)
   yearEntry = Entry(addfcan).place(x=170, y=130)
   ageLabel = Label(addfcan, text='Возрастная категория:', width = 15, padx=10).place(x=30,y=160)
   ageentry = Entry(addfcan).place(x=170, y=160)
   studioLabel = Label(addfcan, text='Студия:', width = 15, padx=10).place(x=30,y=190)
   studioEntry = Entry(addfcan).place(x=170,y=190)
   longLabel = Label(addfcan, text='Длительность:', width = 15, padx=10).place(x=30,y=220)
   longEntry = Entry(addfcan).place(x=170,y=220)
   contLabel = Label(addfcan, text='Продолжения:', width = 15, padx=10).place(x=30,y=250)
   contEntry = Entry(addfcan).place(x=170,y=250)
   prodLabel = Label(addfcan, text='Режисер:', width = 15, padx=10).place(x=30,y=280)
   prodEntry = Entry(addfcan).place(x=170,y=280)
   countryLabel = Label(addfcan, text='Страна:', width = 15, padx=10).place(x=30,y=310)
   countryEntry = Entry(addfcan).place(x=170,y=310)
   rateLabel = Label(addfcan, text='Рейтинг:', width = 15, padx=10).place(x=30,y=340)
   rateEntry = Entry(addfcan).place(x=170,y=340)
window = Tk()
window.title("Filmoteka")
window.geometry('1000x600')

c = Canvas( width=1000, height=600, bg='#241c1e')
c.pack(fill='both', expand=True)

font1 = font.Font(family="Arial", size=25, weight="bold", slant="italic")
font2 = font.Font(family="Arial", size=12, weight="bold", slant="roman")

c.create_polygon(0,70, 1000,70, 1000,0, 0,0, fill='#9c6a75', width=5)
c.create_polygon(0,70, 150,70, 150,600, 0,600, fill='#9c6a75', width=5)
c.create_polygon(1000,70, 800,70, 800,600, 1000,600, fill='#9c6a75', width=5)

c.create_text(650, 35, text="Привет! Что посмотрим сегодня?", font=font1, fill="#242424")
c.create_text(70, 95, text="Быстрый поиск\nпо жанрам", font=font2, fill="#242424")
c.create_text(870, 95, text="Настраиваемый\nпоиск", font=font2, fill="#242424")


c.create_line(0, 70, 1000, 70, fill='#d4264f', width=5)
c.create_line(150, 70, 150, 600, fill='#d4264f', width=5)
c.create_line(800, 70, 800, 600, fill='#d4264f', width=5)

logo = PhotoImage(file="logo.png")
logo1 = logo.subsample(13,13)
c.create_image(160, 35, image=logo1)

#Добавление фильма
btn = Button(c, text='Добавить фильм', command=addfilm,padx=30, pady=10,activebackground='#805962', bg='#9e6f79')
btn.place(x=820,y=550)
# tab_control = ttk.Notebook(window)
#
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)
# tab3 = ttk.Frame(tab_control)
#
# tab_control.add(tab1, text='Главная страница')
# tab_control.add(tab2, text='Рекомендации')
# tab_control.add(tab3, text='Ваши фильмы')
#
# lbl1 = Label(tab1, text='Главная страница')
# lbl1.grid(column=0, row=0)
#
# # def clicked():
# #     messagebox.showinfo('Заголовок', 'Текст')
# #
# # btn = Button(window, text='Клик', command=clicked)
# # btn.grid(column=0, row=0)
# # window.mainloop()
#
# lbl2 = Label(tab2, text='Рекомендации')
# lbl2.grid(column=0, row=100)
#
# lbl3 = Label(tab3, text='Рекмоендации')
# lbl3.grid(column=0, row=100)
#
#
# tab_control.pack(expand=1, fill='both')
window.mainloop()
