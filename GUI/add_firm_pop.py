from tkinter import Label, Entry, Button, Checkbutton, Toplevel, messagebox, BooleanVar

from GUI.utils_gui.setups_win import bg_contract_color, color_bg_btn_activ
from modules import check_company_db, add_company_db


class FirmAdd(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Добавление нового контрагента')
        self.grid()
        self.resizable(width=False, height=False)
        self.configure(bg=bg_contract_color, pady=30, padx=30)

        self.flag = BooleanVar()

        self.name_lbl = Label(self, text='Наименование', padx=10, pady=10,
                              bg=bg_contract_color)
        self.name_lbl.grid(row=1, column=0, sticky='e')
        self.name_entry = Entry(self, width=80, justify='right')
        self.name_entry.grid(row=1, column=1,)

        self.full_name_lbl = Label(self, text='Полное наименование',
                                   padx=10, pady=10, bg=bg_contract_color)
        self.full_name_lbl.grid(row=2, column=0)
        self.full_name_entry = Entry(self, width=80, justify='right')
        self.full_name_entry.grid(row=2, column=1,)

        self.inn_lbl = Label(self, text='ИНН', padx=10, pady=10,bg=bg_contract_color)
        self.inn_lbl.grid(row=3, column=0, sticky='e')
        self.inn_entry = Entry(self, justify='right')
        self.inn_entry.grid(row=3, column=1, sticky='w')

        self.smp_entry = Checkbutton(self, text="Принадлежность к МСП",
                                     padx=10, pady=10,
                                     bg=bg_contract_color,
                                     activebackground=color_bg_btn_activ,
                                     activeforeground='#720cf7',
                                     offvalue=False, onvalue=True,
                                     relief="sunken",
                                     font='12', variable=self.flag,)
        self.smp_entry.grid(row=4, column=1, sticky='w')

        self.send_btn = Button(self, text='Сохранить и закрыть',
                               activebackground=color_bg_btn_activ,
                               bg='#ac72f7', command=self.check)
        self.send_btn.grid(row=5, column=1, sticky='e')

    def check(self):
        """Проверка введенных в форму данных"""
        name = self.name_entry.get()
        full_name = self.full_name_entry.get()
        inn = self.inn_entry.get()

        if not inn.isdigit():
            messagebox.showerror('Ошибка ввода', """
                    \n     ИНН введен неверно!
                    \n ИНН не должен быть пустым.
                    \n ИНН должен состоять из цифр. 
                    \n """)

        elif (len(name) < 7) or (len(full_name) < 7):
            messagebox.showerror('Ошибка ввода', """
                    \n Название организации не может быть менее 7 символов, 
                    \n Полное название, не может быть менее 7 символов,
                    """)

        elif not check_company_db(int(inn), name):
            messagebox.showerror('Ошибка', """
                    \n Запись, не уникальная!
                    \n В базе уже существует компания 
                    \nс таким ИНН или названием""")

        else:
            add_company_db(name, full_name, int(inn), self.flag.get())
            messagebox.showinfo("showinfo", 'Поздравляю, ваши данные успешно сохранены')
            self.destroy()
