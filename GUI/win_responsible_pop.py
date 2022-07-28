import re
import logging

from tkinter import Button, Label, Entry, Toplevel, messagebox

from utils_gui.setups_win import bg_contract_color, color_bg_btn_activ
from modules import add_responsible_bd, check_responsible_db

log = logging.getLogger("main")
logging.basicConfig(level=logging.INFO)


class ResponsibleAdd(Toplevel):
    def __init__(self):
        super().__init__()
        self.configure(bg=bg_contract_color, width=400, padx=20, pady=20)
        self.title('Создание нового ответственного')
        self.input_data()

    def input_data(self):
        self.name_lbl = Label(self, bg=bg_contract_color, text='Введите ФИО в формате <Фамилия И.О.>', justify='right')
        self.name_lbl.grid(row=1, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.name = Entry(self, justify='right')
        self.name.grid(row=1, column=1, columnspan=3, sticky='we', ipadx='10')
        self.update_btn = Button(self, text='Сохранить данные', activebackground=color_bg_btn_activ,
                                 command=self.check)
        self.update_btn.grid(row=2, column=1, padx=10, pady=20, sticky='wn')


    def check(self):

        pattern = r'[а-яА-Яё]{3,}\s[а-яА-Яё]\.[а-яА-Яё]\.'

        if not re.search(pattern, self.name.get()):
            messagebox.showerror('Ошибка ввода', """
            \nВвод неверный, попробуйте еще раз. 
            \n
            \n ФИО должно быть в формате: 
            \n      Фамилия И.О.""")

        elif check_responsible_db(self.name.get()):
            messagebox.showerror('Ошибка', """
            \n Запись, не уникальная!
            \nТакие ФИО уже есть в базе.""")

        else:
            add_responsible_bd(self.name.get())
            messagebox.showinfo("showinfo", 'Поздравляю, ваши данные успешно сохранены', )
            self.destroy()


