import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename, asksaveasfilename #сохранить как, открыть как
from tkinter.messagebox import showerror #показ ошибок
from tkinter import messagebox #уведомления
from settings import *
import codecs

app = tkinter.Tk()
text = tkinter.Text(app,width=WIDTH - 100, height=HEIGHT - 15, wrap = 'word')

class FunctionEd:
    def __init__(self):
        self.file_name = tkinter.NONE

    def new_file(self):
        self.file_name = 'text'
        text.delete('1.0', tkinter.END)

    def save_file(self):
        data = text.get('1.0', tkinter.END)
        output = open(self.file_name, 'w', encoding='utf-8')
        output.write(data)
        output.close()

    def open_file(self):
        inp = askopenfilename()
        if inp is None:
            return
        with codecs.open(inp, encoding='utf-8') as f:
            data = f.read()
            text.delete('1.0', tkinter.END)
            text.insert('1.0', data)
    def save_as_file(self):
        output = asksaveasfile(mode='w', defaultextension='txt')
        data = text.get('1.0', tkinter.END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title='Ошибка!', message='Ошибка при сохранении файла.')

    def get_info(self):
        messagebox.showinfo('Справка', "Информация о нашем приложении! Спасибо, что его используете.")



    
