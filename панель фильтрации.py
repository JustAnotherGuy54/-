import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Фильтрация ")
root.geometry("1000x600")
# Создаем список годов и режиссеров
year_label=tk.Label(root,text='выбери год')
years = ['','1969-1999', '2022-2025', '2017-2021', '2001-2010', '2011-2015']
director = ['','Майкл Кертис', 'Орсон Уэллс', 'Джон Стёрджес', 'Альфред Хичкок', 'Стэнли Кубрик']
country=['','США','Великобритания','Новая Зеландия','Италия','Россия','Польша','Южная Корея','Канада','Тайланд']
category=['','6','12','16','18']
studio=['','Warner Bros','RKO Pictures','Mirisch Corporation,United Artists','Shamley Productions, Paramount Pictures','Horizon Pictures,Columbia Pictures','Bryna Productions ,Columbia Pitures','Universal Pictures',
'Paramount Pictures','Disney','А24','Sony Pictures','Сolumbia','20th Century Studios','Blumhouse','Universal Pictures','Netflix','Paramount'
'Barunson E&A, CJ Entartainment','Walt Disney Pictures','Warner Bros. Pictures','DreamWorks Pictures','Amblin Partners'
,'Netflix Animation','Pixar Animation Studios','Marvel Studios','Exile Entertainment','The Kennedy/Marshall Company','Dune Entertainment','DreamWorks Pictures','Warner Bros. Pictures','Blind Wink Productions'
'20th Century Fox','Marvel Studios','Marvel Studios','Lucasfilm','DreamWorks Pictures','DreamWorks Animation','Nickelodeon Movies','20th Century Fox','Artisan Entertainment'
'New Line Cinema','Walt Disney Pictures','Legendary Pictures','Warner Bros. Pictures','Warner Bros. Pictures','20th Century Fox'
'Red Granite Pictures','Marvel Studios','Lionsgate']
# Создаем Label для отображения текста
label= tk.Label(root, text= "Фильтры:",font="Arial 17")

label.place(relx=0.85,rely=0.11)
label_year = tk.Label(root, text="Год выпуска")
label_year.place(relx=0.85,rely=0.16)
# Создаем Combobox для выбора года

year_var = tk.StringVar(root)
year_var.set(years[0])  # Устанавливаем начальное значение
year_dropdown = ttk.Combobox(root, textvariable=year_var, values=years)
year_dropdown.place(relx=0.85, rely=0.19)

label_director =tk.Label(root,text="Режиссер")
label_director.place(relx=0.85,rely=0.23)
# Создаем Combobox для выбора режиссера
director_var = tk.StringVar(root)
director_var.set(director[0])
director_dropdown = ttk.Combobox(root, textvariable=director_var, values=director)
director_dropdown.place(relx=0.85, rely=0.26)


label_country=tk.Label(root,text="Страна")
label_country.place(relx=0.85,rely=0.29)
country_var =tk.StringVar(root)
country_var.set(country[0])
country_dropdown = ttk.Combobox(root,textvariable=country_var,values=country)
country_dropdown.place(relx=0.85,rely=0.32)

label_category =tk.Label(root,text="Возрастная категория")
label_category.place(relx=0.85,rely=0.36)
category_var = tk.StringVar(root)
category_var.set(category[0])
category_dropdown = ttk.Combobox(root, textvariable= category_var, values=director)
category_dropdown.place(relx=0.85,rely=0.39)

label_studio =tk.Label(root,text="Студия")
label_studio.place(relx=0.85,rely=0.43)
studio_var =tk.StringVar(root)
studio_var.set(category[0])
studio_dropdown = ttk.Combobox(root,textvariable =studio_var,value=studio)
studio_dropdown.place(relx=0.85,rely=0.46)
# Функции для обработки выбора года и режиссера , страны , студии,возрастной категории
def on_select_year(event):
    selected_year = year_var.get()
    print("Выбран год:", selected_year)

def on_select_director(event):
    selected_director = director_var.get()
    print("Выбери режиссера:", selected_director)
def on_select_country(event):
    selected_country = country_var.get()
    print("Выбери страну",selected_country)

def on_select_category(event):
    selected_category =category_var.get()
    print("Выбери возврастную категорию",selected_category)
def on_select_studio(event):
    selected_studio =studio_var.get()
    print("выбери студию",selected_studio)
btn =tk.Button(root,text=" Применить",font="Arial 12")
btn.place(relx=0.85,rely=0.51)
# Привязываем функции к событиям выбора года и режиссера
year_dropdown.bind("<<ComboboxSelected>>", on_select_year)
director_dropdown.bind("<<ComboboxSelected>>", on_select_director)
country_dropdown.bind("<<ComboboxSelected>>",on_select_country)
category_dropdown.bind("<<ComboboxSelected>>",on_select_category)
studio_dropdown.bind("<<ComboboxSelected>>",on_select_studio)
root.mainloop()