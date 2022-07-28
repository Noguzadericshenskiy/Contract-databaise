from tkinter import Label, Entry, Button, Toplevel, messagebox, Listbox

from GUI.utils_gui.setups_win import bg_contract_color, color_bg_btn_activ
from modules import get_all_type_contract_bd, add_type_contract_bd


class TypeAdd(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Создание типа контракта')
        self.grid()
        self.resizable(width=False, height=False)
        self.configure(bg=bg_contract_color, pady=30, padx=30)

        self.lis = []
        self.name_lbl = Label(self, text='Тип контракта', padx=10, pady=10,
                              bg=bg_contract_color)
        self.name_lbl.grid(row=1, column=0, sticky='e')
        self.name_entry = Entry(self, width=30, justify='right')
        self.name_entry.grid(row=1, column=1,)

        self.list_lbl = Label(self, text='Типы', padx=10, pady=10,
                              bg=bg_contract_color)
        self.list_lbl.grid(row=2, column=0)

        self.list_box = Listbox(self,)
        self.list_box.grid(row=3, column=0)

        self.send_btn = Button(self, text='Добавить и закрыть окно',
                               activebackground=color_bg_btn_activ, bg=bg_contract_color, command=self.check)
        self.send_btn.grid(row=2, column=1, sticky='e')

        for i in get_all_type_contract_bd():
            self.lis.append(i.type_contract)
            self.list_box.insert('0', i.type_contract)

    def check(self):
        """Проверка введенных в форму данных и запись"""
        if self.name_entry.get() in self.lis:
            messagebox.showerror('Ошибка ввода', """
                                \n Такой тип договора уже есть в базе!
                                \n """, )

        elif len(self.name_entry.get()) < 4:
            messagebox.showerror('Ошибка ввода', """
                                \n Тип договора должен быть больше 4 символов!
                                \n """)
        else:
            add_type_contract_bd(self.name_entry.get())
            messagebox.showinfo("showinfo", 'Поздравляю, ваши данные успешно сохранены')
            self.destroy()
