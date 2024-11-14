from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import Button
import pandas
import random

db = pandas.read_excel('./тестю.xlsx', sheet_name='Фильмы')
list = db.values.tolist()
def filter_genre(genre):
    df = db[db['Жанр'].isin([genre])]
    list_data = df.values.tolist()
    update_treeview(list_data)

def update_treeview(data):
    for item in tree.get_children():
        tree.delete(item)
    for row in data:
        tree.insert("", END, values=row)

def on_double_click(event):
    def deletefilm():
       index = tree.index(selected_item)
       db.at[index, 'Бан'] = 1
       update_treeview(db.values.tolist())
        
    def lovefilm():
       index = tree.index(selected_item)
       db.at[index, 'Нравится'] = 1  # Обновляем столбец 'Нравится' на 1
       update_treeview(db.values.tolist())

    movieinfo = Tk()
    movieinfo.title("Информация о фильме")
    movieinfo.geometry('600x600')
    label_font = ("Arial", 11, "bold")
    entry_font = ("Arial", 11)
    label_bg = '#FFCF9D'
    entry_bg = '#f7f1f1'
    movieinfoC = Canvas(movieinfo, width=600, height=600, bg='#FFB26F')
    movieinfoC.pack(fill='both', expand=True)
    # placeholder = PhotoImage(file="placeholder.png")
    # placeholder1 = logo.subsample(3,3)
    # movieinfoC.create_image(160, 35, image=placeholder)
    selected_item = tree.selection()[0] 
    item_values = tree.item(selected_item, 'values')
    btn_recommend = Button(movieinfo, text='Нравится', command=lovefilm, width=10, padx=30, pady=10, activebackground='#805962', bg='lime')
    btn_recommend.place(x=450, y=500)
    
    btn_blocklist = Button(movieinfo, text='Не нравится', command=deletefilm, width=10, padx=30, pady=10, activebackground='#805962', bg='red')
    btn_blocklist.place(x=450, y=450)


def addfilm():
   def submitFilm():
    db.loc[len(db.index)] = [nameEntry.get(), genreEntry.get(), yearEntry.get(), ageEntry.get(), studioEntry.get(), longEntry.get(), contEntry.get(), prodEntry.get(), countryEntry.get(), rateEntry.get()]
    db.to_excel('./тестю.xlsx', sheet_name='Фильмы', index=False)
    newfilm.destroy()

   newfilm = Tk()
   newfilm.title("Добавление нового фильма")
   newfilm.geometry('600x600')
   label_font = ("Arial", 11, "bold")
   entry_font = ("Arial", 11)
   label_bg = '#FFCF9D'
   entry_bg = '#f7f1f1'
   addfcan = Canvas(newfilm, width=600, height=600, bg='#FFB26F')
   addfcan.pack(fill='both', expand=True)
   addfcan.create_text(300,35, text='Введите данные о фильме в каждую из ячеек\nа затем нажмите отправить.', font=label_font)

   nameLabel = Label(addfcan, text='Название:', font=label_font, bg=label_bg, anchor="w", width=17, padx=10)
   nameLabel.place(x=30, y=70)
   nameEntry = Entry(addfcan, font=entry_font, bg=entry_bg, bd=2, relief="solid")
   nameEntry.place(x=230, y=70)
   
   genreLabel = Label(addfcan, text='Жанр:', font=label_font, bg=label_bg, anchor="w", width=17, padx=10)
   genreLabel.place(x=30, y=100)
   genreEntry = ttk.Combobox(addfcan, font=entry_font, state="normal", width=17, values=['Драма', 'Комедия', 'Фантиастика', 'Ужасы', 'Приключения', 'Боевик', ])
   genreEntry.place(x=232, y=100)
   
   yearLabel = Label(addfcan, text='Год создания:', font=label_font, bg=label_bg, anchor="w", width=17, padx=10)
   yearLabel.place(x=30, y=130)
   yearEntry = Entry(addfcan, font=entry_font, bg=entry_bg, bd=2, relief="solid")
   yearEntry.place(x=230, y=130)
   
   ageLabel = Label(addfcan, text='Возрастная категория:', font=label_font, bg=label_bg, anchor="w", width=17, padx=10)
   ageLabel.place(x=30, y=160)
   ageEntry = Entry(addfcan, font=entry_font, bg=entry_bg, bd=2, relief="solid")
   ageEntry.place(x=230, y=160)
   
   studioLabel = Label(addfcan, text='Студия:', font=label_font, bg=label_bg, anchor="w", width=17, padx=10)
   studioLabel.place(x=30, y=190)
   studioEntry = Entry(addfcan, font=entry_font, bg=entry_bg, bd=2, relief="solid")
   studioEntry.place(x=230, y=190)
   
   longLabel = Label(addfcan, text='Длительность:', font=label_font, bg=label_bg, anchor="w", width=17, padx=10)
   longLabel.place(x=30, y=220)
   longEntry = Entry(addfcan, font=entry_font, bg=entry_bg, bd=2, relief="solid")
   longEntry.place(x=230, y=220)
   
   contLabel = Label(addfcan, text='Продолжения:', font=label_font, bg=label_bg, anchor="w", width=17, padx=10)
   contLabel.place(x=30, y=250)
   contEntry = Entry(addfcan, font=entry_font, bg=entry_bg, bd=2, relief="solid")
   contEntry.place(x=230, y=250)
   
   prodLabel = Label(addfcan, text='Режисер:', font=label_font, bg=label_bg, anchor="w", width=17, padx=10)
   prodLabel.place(x=30, y=280)
   prodEntry = Entry(addfcan, font=entry_font, bg=entry_bg, bd=2, relief="solid")
   prodEntry.place(x=230, y=280)
   
   countryLabel = Label(addfcan, text='Страна:', font=label_font, bg=label_bg, anchor="w", width=17, padx=10)
   countryLabel.place(x=30, y=310)
   countryEntry = Entry(addfcan, font=entry_font, bg=entry_bg, bd=2, relief="solid")
   countryEntry.place(x=230, y=310)
   
   rateLabel = Label(addfcan, text='Рейтинг:', font=label_font, bg=label_bg, anchor="w", width=17, padx=10)
   rateLabel.place(x=30, y=340)
   rateEntry = Entry(addfcan, font=entry_font, bg=entry_bg, bd=2, relief="solid")
   rateEntry.place(x=230, y=340)
   
   btn2 = Button(addfcan, text='Добавить фильм', font=label_font, bg=label_bg, anchor="w", command=submitFilm, height=5, width=15, padx=30, pady=10, activebackground='#805962')
   btn2.pack(side='bottom')

def filter_love():
    df_love = db[db['Нравится'] == 1]
    list_data_love = df_love.values.tolist()
    random_rows = random.sample(list, 3)
    combined_list = list_data_love + random_rows
    update_treeview(combined_list)

def filter_ban():
    df = db[db['Бан'] == 1]
    list_data = df.values.tolist()
    update_treeview(list_data)

window = Tk()
window.title("Filmoteka")
window.geometry('1000x600')
c = Canvas( width=1000, height=600, bg='#241c1e')
c.pack(fill='both', expand=True)
left_frame = Frame(c, width=150, height=600, bg='#FFB26F')
left_frame.place(x=0, y=73)
#right_frame = Frame(c, width=160, height=600, bg='#9c6a75')
#right_frame.place(x=805, y=75)
center_frame = Frame(c, width=847, height=600, bg='#ffffff')
center_frame.place(x=153, y=75)

font1 = font.Font(family="Arial", size=25, weight="bold", slant="italic")
font2 = font.Font(family="Arial", size=12, weight="bold", slant="roman")

c.create_polygon(0,70, 1000,70, 1000,0, 0,0, fill='#FFB26F', width=5)
c.create_polygon(0,70, 150,70, 150,600, 0,600, fill='#FFB26F', width=5)
#c.create_polygon(1000,70, 800,70, 800,600, 1000,600, fill='#9c6a75', width=5)

c.create_text(650, 35, text="Привет! Что посмотрим сегодня?", font=font1, fill="#242424")
c.create_text(70, 95, text="Быстрый поиск\nпо жанрам", font=font2, fill="#242424")
c.create_text(870, 95, text="Настраиваемый\nпоиск", font=font2, fill="#242424")


c.create_line(0, 70, 1000, 70, fill='#b57650', width=5)
c.create_line(150, 70, 150, 600, fill='#b57650', width=5)
#c.create_line(800, 70, 800, 600, fill='#d4264f', width=5)

button1 = Button(left_frame, text='Фантастика', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button1['text']))
button1.pack(side='top', pady=6, padx=15)
button2 = Button(left_frame, text='Драма', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button2['text']))
button2.pack(side='top', pady=6, padx=15)
button3 = Button(left_frame, text='Комедия', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button3['text']))
button3.pack(side='top', pady=6, padx=15)
button4 = Button(left_frame, text='Ужасы', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button4['text']))
button4.pack(side='top', pady=6, padx=15)
button5 = Button(left_frame, text='Приключения', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button5['text']))
button5.pack(side='top', pady=6, padx=15)
button6 = Button(left_frame, text='Боевик', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button6['text']))
button6.pack(side='top', pady=6, padx=15)
button7 = Button(left_frame, text='Фэнтези', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button7['text']))
button7.pack(side='top', pady=6, padx=15)
button8 = Button(left_frame, text='Биографический', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button8['text']))
button8.pack(side='top', pady=6, padx=15)
button9 = Button(left_frame, text='Мультфильм', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button9['text']))
button9.pack(side='top', pady=6, padx=15)
button10 = Button(left_frame, text='Триллер', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button10['text']))
button10.pack(side='top', pady=6, padx=15)
button11 = Button(left_frame, text='Военный', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button11['text']))
button11.pack(side='top', pady=6, padx=15)
button12 = Button(left_frame, text='Детектив', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button12['text']))
button12.pack(side='top', pady=6, padx=15)
button13 = Button(left_frame, text='Криминал', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button13['text']))
button13.pack(side='top', pady=6, padx=15)
button14 = Button(left_frame, text='Вестерн', width=15, height=1, activebackground='#805962', bg='#FFCF9D', command=lambda: filter_genre(button14['text']))
button14.pack(side='top', pady=6, padx=15)

columns = ("Название", "Жанр", "Год создания","Возрастная категория", "Студия", "Длительность", "Продолжения", "Режисер", "Страна", "Рейтинг", "Бан", "Нравится")
tree = ttk.Treeview(center_frame, height=25, columns=columns, show=["headings"], displaycolumns=["Название", "Жанр", "Год создания","Возрастная категория", "Студия", "Длительность", "Продолжения", "Режисер", "Страна", "Рейтинг", "Бан"])
tree.pack(fill='y',expand=1)
for col in columns:
   tree.heading(col, text=col)
   tree.column(col,width=int(center_frame['width'] / 11))
for i in range(len(db.index)):
   tree.insert("",END, values=list[i])

tree.bind("<Double-1>", on_double_click)

logo = PhotoImage(file="logo.png")
logo1 = logo.subsample(3,3)
c.create_image(160, 35, image=logo1)

btn = Button(c, text='Добавить фильм', command=addfilm, width=10, padx=30, pady=10,activebackground='#805962', bg='#FFCF9D')
btn.place(x=840,y=550)
btnRec = Button(c, text='Порекомендовать', command=filter_love, width=10, padx=30, pady=10,activebackground='#805962', bg='#FFCF9D')
btnRec.place(x=840,y=500)
btnBan = Button(c, text='Банлист', command=filter_ban, width=10,padx=30, pady=10,activebackground='#805962', bg='#FFCF9D')
btnBan.place(x=840,y=450)
window.mainloop()
