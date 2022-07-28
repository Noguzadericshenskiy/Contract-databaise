import logging
from tkinter import Label, Entry, Text, Toplevel, Button
from tkinter.ttk import Combobox
from tkcalendar import DateEntry

from utils_gui.setups_win import bg_contract_color, color_bg_btn_activ
from hendlers_gui import tuple_responsible, types_contract


log = logging.getLogger("update_contract_pop")
logging.basicConfig(level=logging.INFO)


class ContractUpdate(Toplevel):
    """
    Класс вывода окна обновления данных о договоре
    Рисуем окно и получаем данные о договоре от родителя
    2 кнопки сохранить и выход
    (возможно добавление еще одной, пока думают)
    """
    def __init__(self, param):
        super().__init__()
        self.title('Изменение договора')
        self.grid()
        self.resizable(width=False, height=False)
        self.configure(bg=bg_contract_color, pady=30, padx=30)
        self.contract = param
        self.types_contract = types_contract()

        self.firm_lbl = Label(self, bg=bg_contract_color, text='Контрагент', justify='right')
        self.firm_lbl.grid(row=1, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.firm_entry = Entry(self, justify='left')
        self.firm_entry.grid(row=1, column=1, columnspan=3, sticky='we', ipadx='10')

        self.num_contract_lbl = Label(self, bg=bg_contract_color, text='Номер договора', justify='right')
        self.num_contract_lbl.grid(row=2, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.num_contract_entry = Entry(self, justify='right')
        self.num_contract_entry.grid(row=2, column=1, columnspan=1, sticky='we', ipadx='10')

        self.num_contract_in_lbl = Label(self, bg=bg_contract_color, text='Входящий номер', justify='right')
        self.num_contract_in_lbl.grid(row=3, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.num_contract_in_entry = Entry(self, justify='right')
        self.num_contract_in_entry.grid(row=3, column=1, columnspan=1, sticky='we', ipadx='10')

        self.sum_lbl = Label(self, bg=bg_contract_color, text='Сумма', justify='right')
        self.sum_lbl.grid(row=4, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.sum_entry = Entry(self, justify='right')
        self.sum_entry.grid(row=4, column=1, columnspan=1, sticky='we', ipadx='10')

        self.date_lbl = Label(self, bg=bg_contract_color, text='Дата заключения', justify='right')
        self.date_lbl.grid(row=5, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.date_entry = DateEntry(self, width=12, background='darkblue', date_pattern='yyyy-mm-dd',
                                          foreground='white', borderwidth=2, locale='ru_RU')
        self.date_entry.grid(row=5, column=1, columnspan=1, sticky='we', ipadx='10')
        self.date_entry.delete(0, "end")

        self.date_start_lbl = Label(self, bg=bg_contract_color, text='Дата начала', justify='right')
        self.date_start_lbl.grid(row=6, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.date_start_entry = DateEntry(self, width=12, background='darkblue', date_pattern='yyyy-mm-dd',
                                          foreground='white', borderwidth=2, locale='ru_RU')
        self.date_start_entry.grid(row=6, column=1, columnspan=1, sticky='we', ipadx='10')
        self.date_start_entry.delete(0, "end")

        self.date_end_lbl = Label(self, bg=bg_contract_color, text='Дата завершения', justify='right')
        self.date_end_lbl.grid(row=7, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.date_end_entry = DateEntry(self, width=12, background='darkblue', date_pattern='yyyy-mm-dd',
                                          foreground='white', borderwidth=2, locale='ru_RU')
        self.date_end_entry.grid(row=7, column=1, columnspan=1, sticky='we', ipadx='10')
        self.date_end_entry.delete(0, "end")

        self.responsible_lbl = Label(self, bg=bg_contract_color, text='Ответственный', justify='right')
        self.responsible_lbl.grid(row=8, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.responsible_entry = Combobox(self, values=tuple_responsible(), justify='right')
        self.responsible_entry.grid(row=8, column=1, columnspan=1, sticky='we', ipadx='10')

        self.type_contract_lbl = Label(self, bg=bg_contract_color, text='Тип договора', justify='right')
        self.type_contract_lbl.grid(row=9, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.type_contract_entry = Combobox(self, values=self.get_types_contract(), justify='right')
        self.type_contract_entry.grid(row=9, column=1, columnspan=1, sticky='we', ipadx='10')

        self.subject_contract_lbl = Label(self, bg=bg_contract_color, text='Предмет договора', justify='right')
        self.subject_contract_lbl.grid(row=2, column=2, sticky='e', ipadx='10', ipady='5', padx='20')
        self.subject_contract_entry = Text(self, height=5)
        self.subject_contract_entry.grid(row=3, column=2, rowspan=3, sticky='we', ipadx='10', padx='20')
        self.subject_contract_entry.configure(width=73)

        self.comment_lbl = Label(self, bg=bg_contract_color, text='Комментарий', justify='right')
        self.comment_lbl.grid(row=6, column=2, sticky='e', ipadx='10', ipady='5', padx='20')
        self.comment_entry = Text(self, height=5)
        self.comment_entry.grid(row=7, column=2, rowspan=3, sticky='we', ipadx='10', padx='20')
        self.comment_entry.configure(width=73)

        self.add_additional_btn = Button(self, text='Сохранить изменения',
                                         activebackground=color_bg_btn_activ, command=self.update)
        self.add_additional_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=20, sticky='wn')

        self.add_additional_btn = Button(self, text='Выход без сохранения',
                                         activebackground=color_bg_btn_activ, command=self.close_win)
        self.add_additional_btn.grid(row=11, column=3, columnspan=2, padx=10, pady=20, sticky='wn')

        self.num_contract_entry.insert(0, param[0])
        self.num_contract_in_entry.insert(0, param[1])
        self.firm_entry.insert(0, param[2])
        self.date_entry.set_date(param[4])
        self.date_start_entry.set_date(param[3])
        self.sum_entry.insert(0, param[6])
        self.subject_contract_entry.insert('1.0', param[7])
        self.type_contract_entry.set(param[8])
        self.responsible_entry.set(param[9])
        self.comment_entry.insert('1.0', param[10])
        try:
            self.date_end_entry.set_date(param[5])
        except ValueError:
            log.info(f'date_end_entry={self.date_end_entry.set_date(param[5])}')
            self.date_end_entry.delete(0, "end")
        # , date_pattern='yyyy/MM/dd'


    def get_types_contract(self):
        types = tuple(type_i.type_contract for type_i in self.types_contract)
        return types

    def close_win(self):

        self.destroy()

    def update(self):
        par = self.get_param()
        log.info(f"param {par}")


    def get_param(self):
        firm = self.firm_entry.get()
        num_contract = self.num_contract_entry.get()
        num_contract_in = self.num_contract_in_entry.get()
        summ = self.sum_entry.get()
        date_start = self.date_start_entry.get_date().strftime('%Y-%m-%d')
        date = self.date_entry.get_date().strftime('%Y-%m-%d')
        date_end = self.date_end_entry.get_date().strftime('%Y-%m-%d')
        responsible = self.responsible_entry.get()
        type_con = self.type_contract_entry.get()
        subject = self.subject_contract_entry.get("1.0", "end")
        comment = self.comment_entry.get("1.0", "end")

        data = (self.contract[11],
                firm,
                num_contract,
                num_contract_in,
                summ,
                date_start,
                date,
                date_end,
                responsible,
                type_con,
                subject,
                comment
                )

        return data