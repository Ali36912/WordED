# -*- coding: utf8 -*-
import tkinter
from tkinter import *
from settings import *
from function_ed import *

function = FunctionEd()


app.title(APP_NAME) #имя нашего приложения
app.minsize(width=WIDTH, height=HEIGHT) #минимальные размеры открытия
app.maxsize(width=WIDTH, height=HEIGHT) #максимальные размеры открытия


scrol = Scrollbar(app, orient = VERTICAL, command = text.yview) #скрол
scrol.pack(side = 'right', fill = 'y') #расположения
text.configure(yscrollcommand= scrol.set) #совмещения скрола и текста
text.pack()                               #расположение текста
#меню бар
menuBar = tkinter.Menu(app)             
#выплывающее окно у "Файла"
app_menu = tkinter.Menu(menuBar)   
#выплывающее окно доп.функций в разделе "Файл"
app_menu_dop = tkinter.Menu(app_menu)    
app_menu.add_command(label = 'Новый файл', command=function.new_file)
app_menu.add_command(label = 'Открыть файл', command=function.open_file)
app_menu.add_command(label = 'Сохранить', command=function.save_file)
app_menu.add_command(label = 'Сохранить как', command=function.save_as_file)
app_menu.add_cascade(label = 'Дополнительно', menu = app_menu_dop)
#Выплывающее меню для "Справка"
app_menu_dop.add_command(label = 'Информация')

app_menu_inf = tkinter.Menu(menuBar)
app_menu_inf.add_command(label = 'Приветствие')
app_menu_inf.add_command(label = 'Справочник по сочетаниям клавиш')
app_menu_inf.add_command(label = 'Сообщить о проблеме')
app_menu_inf.add_command(label = 'О программе', command=function.get_info)


#Сам меню бар
menuBar.add_cascade(label='Файл', menu = app_menu)
menuBar.add_cascade(label='Справка', menu = app_menu_inf)  
menuBar.add_cascade(label='Вид')          
menuBar.add_cascade(label='Выход', command=app.quit)

app.config(menu=menuBar)                              #публикуем наше меню


app.mainloop() #бесконечный цикл приложения