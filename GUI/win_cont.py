import tkinter as tk
import datetime

import logging

from tkinter import ttk, Menu, Button, Label, Entry, Tk, Frame, LabelFrame, Text, Scrollbar, END
from tkinter.ttk import Combobox
from tkinter import filedialog as fd
from tkcalendar import DateEntry

from modules import *
from hendlers_gui import tuple_contract, tuple_additional, tuple_responsible
from utils_gui.setups_win import *
from add_additional_pop import WinAddAdditional
from win_add_contract import ContractAdd
from win_responsible_pop import ResponsibleAdd
from add_firm_pop import FirmAdd
from add_type_pop import TypeAdd
from update_contract_pop import ContractUpdate

log = logging.getLogger("main")
logging.basicConfig(level=logging.INFO)


class WinContracts(Tk):
    def __init__(self):
        super().__init__()
        self.title('База данных договоров')
        self.minsize(1024, 800)
        self.maxsize(1920, 1080)
        # self.geometry('1920x1080')
        self.bold_font = "bold"
        self._main_menu()
        self.select_date = FilterContract()


    def _main_menu(self):
        self.main_menu = Menu(self, background="#67dbb8")
        self.config(menu=self.main_menu)

        self.contract_menu = Menu(self.main_menu, tearoff=0, background=color_bg_menu)
        self.contract_menu.add_command(label="Показать все контракты")
        self.contract_menu.add_command(label="Найти по номеру")
        self.contract_menu.add_command(label="Добавить новый договор", command=self.add_contract)
        self.contract_menu.add_command(label="Найти договор")
        self.contract_menu.add_command(label="Изменить договор", command=self.update_contract)

        self.contract_44_menu = Menu(self.main_menu, tearoff=0, background=color_bg_menu)
        self.contract_44_menu.add_command(label="Показать все контракты")
        self.contract_44_menu.add_command(label="Найти по номеру")
        self.contract_44_menu.add_command(label="Добавить новый договор", command=self.add_contract)
        self.contract_44_menu.add_command(label="Найти договор")
        self.contract_44_menu.add_command(label="Изменить договор", command=self.update_contract)

        self.user_menu = Menu(self.main_menu, tearoff=0, background=color_bg_menu)
        self.user_menu.add_command(label="Добавить контрагента", command=self.add_company)
        self.user_menu.add_command(label="Добавить ответственного", command=self.add_responsible)
        self.user_menu.add_command(label="Добавить тип договора", command=self.add_type)
        self.user_menu.add_command(label="")
        self.user_menu.add_command(label="")

        self.record_menu = Menu(self.main_menu, tearoff=0, background=color_bg_menu)
        self.record_menu.add_command(label="Просто  отчет 1")
        self.record_menu.add_command(label="Просто  отчет 2")
        self.record_menu.add_command(label="Просто  отчет 3")
        self.record_menu.add_command(label="Просто  отчет 4")
        self.record_menu.add_command(label="Просто отчет n")

        self.admin_menu = Menu(self.main_menu, tearoff=0, background=color_bg_menu)
        self.admin_menu.add_command(label="Создать нового пользователя")
        self.admin_menu.add_command(label="Сбросить пароль пользователя")
        self.admin_menu.add_command(label="Удалить пользователя")
        self.admin_menu.add_command(label="Создать новую БД", command=self.create_bd)
        self.admin_menu.add_command(label="Указать путь до БД", command=self.get_dir_bd)

        self.quit_menu = Menu(self.main_menu, tearoff=0, background='#f05e0a', activebackground='#de2137')
        self.quit_menu.add_command(label="Завершить работу", command=self.quit_app)

        self.main_menu.add_cascade(label="Договоры", menu=self.contract_menu)
        self.main_menu.add_cascade(label="Договоры 44", menu=self.contract_44_menu)
        # self.main_menu.add_cascade(label="Договоры", menu=self.contract_menu)
        # self.main_menu.add_cascade(label="Договоры СМСП", menu=self.contract_SMSP_menu)
        self.main_menu.add_cascade(label="User menu ", menu=self.user_menu)
        self.main_menu.add_cascade(label="Отчеты", menu=self.record_menu)
        self.main_menu.add_cascade(label="Admin menu", menu=self.admin_menu)
        self.main_menu.add_cascade(label="Exit", menu=self.quit_menu)

    def get_dir_bd(self):
        # Получаем директорию с файлом или бд
        # функцию можно вынести наружу метода
        path = fd.askdirectory()
        print(path)

    def create_bd(self):
        path_bd = fd.askdirectory()
        print(path_bd)

    @staticmethod
    def add_contract():
        ContractAdd()

    def update_contract(self):
        ...

    @staticmethod
    def add_responsible():
        ResponsibleAdd()

    @staticmethod
    def add_company():
        FirmAdd()

    @staticmethod
    def add_type():
        TypeAdd()

    def quit_app(self):
        self.quit()


class FilterContract(Frame):
    def __init__(self):
        super().__init__()
        self.grid(row=1, column=0, columnspan=2, sticky='we', )
        self.configure(bg=bg_contract_color, height=50, width=1920, )

        self.date_start_lbl = Label(self, bg=bg_contract_color, text='Начало периода', justify='right', pady=5)
        self.date_start_lbl.grid(row=1, column=0, padx=5, sticky='e')
        self.date_start_entry = DateEntry(self, width=12, background='darkblue', year=2020,
                                          foreground='white', borderwidth=2, locale='ru_RU')
        self.date_start_entry.grid(row=1, column=1, )


        self.date_end_lbl = Label(self, bg=bg_contract_color, text='Конец периода', justify='right', pady=5)
        self.date_end_lbl.grid(row=2, column=0, padx=5, sticky='e')
        self.date_end_entry = DateEntry(self, width=12, background='darkblue',
                                        foreground='white', borderwidth=2, locale='ru_RU')
        self.date_end_entry.grid(row=2, column=1)

        self.number_lbl = Label(self, bg=bg_contract_color, text='Номер', justify="right", pady=5)
        self.number_lbl.grid(row=1, column=2, padx=5, sticky='e')
        self.number_entry = Entry(self, width=12, borderwidth=2, )
        self.number_entry.grid(row=1, column=3, sticky='we')

        self.responsible_lbl = Label(self, bg=bg_contract_color, text='Ответственный', justify='right', pady=5)
        self.responsible_lbl.grid(row=2, column=2, padx=5, sticky='e')
        self.responsible_entry = Combobox(self, values=tuple_responsible())
        self.responsible_entry.current()
        # self.responsible_entry.current(1)
        self.responsible_entry.grid(row=2, column=3)

        self.search_lbl = Label(self, bg=bg_contract_color, text='Контекстный поиск', justify='right', pady=5)
        self.search_lbl.grid(row=1, column=4, padx=5, sticky='e')
        self.search_entry = Entry(self, width=20, borderwidth=2, )
        self.search_entry.grid(row=1, column=5, )


        self.search_btn = Button(self, text='Показать', activebackground=color_bg_btn_activ,
                                 command=self.search_contract)
        self.search_btn.grid(row=1, rowspan=2, column=6, ipadx=10, ipady=2, padx=20)

        self.contract_frame = ContractTableFrame()

    def search_contract(self):
        """
        Получает параметры фильтра договоров и передает их в виде кортежа
        (table, date_in, date_out, number, responsible, context)
        """
        table = 'table_contract'
        date_in = self.date_start_entry.get_date().strftime('%Y-%m-%d')
        date_out = self.date_end_entry.get_date().strftime('%Y-%m-%d')
        number = self.number_entry.get()
        responsible = self.responsible_entry.get()
        context = self.search_entry.get()
        parameters_contract = (table, date_in, date_out, number, responsible, context)
        self.contract_frame.clear_all_records()
        self.contract_frame.out_table_contract(parameters_contract)
        # log.info(d)
        # log.info(self.data_end_entry.get_date())



    def int_data(self):
        ...
        # self.contract_frame = ContractTableFrame(data)


class ContractTableFrame(LabelFrame):
    """
        Класс выводит таблицу договоров переопределяется в соответствии с выбором таблицы договоров
        Возможно добавлю сюда виджеты из верхнего фрейма.
        """
    def __init__(self, dates=None):
        super().__init__()
        self.dates = dates
        self.values_contract = tuple()
        self.grid(row=2, column=0, columnspan=2, sticky='wn')
        self.configure(bg=bg_contract_color, height='500', text='Информация о договорах')

        # self.scroll_y = Scrollbar(self)
        # self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.table = ttk.Treeview(self,
                                  show="headings",
                                  selectmode="browse",
                                  columns=heads_contract,
                                  displaycolumns=columns_contract,
                                  # yscrollcommand=self.scroll_y.set,
                                  )

        self.table.column('#0', width=0)
        self.table.column('№ договора', width=120, anchor='center')
        self.table.column('№(входящий)', width=120, anchor='e')
        self.table.column('Контрагент', width=300, anchor='e')
        self.table.column('Предмет договора', width=250, anchor='e')
        self.table.column('comment', width=300, anchor='e')
        self.table.column('Дата начала', width=120, anchor='center')
        self.table.column('Дата закл', width=120, anchor='center')
        self.table.column('Дата окончания', width=120, anchor='center')
        self.table.column('Сумма', width=150, anchor='e')
        self.table.column('Ответственный', width=150, anchor='center')
        self.table.column('Тип договора', width=150, anchor='e')

        for header in heads_contract:
            self.table.heading(header, text=header, anchor=tk.CENTER)

        self.scroll_table = Scrollbar(self, command=self.table.yview)
        self.table.configure(yscrollcommand=self.scroll_table.set)
        self.scroll_table.pack(side=tk.RIGHT, fill=tk.Y)

        self.table.pack(ipady=100)
        self.table.bind('<<TreeviewSelect>>', self.select_records)

        self.info_contract = InfoContractFrame()

        self.additional_table = AdditionalTableFrame()

    def out_table_contract(self, parameters):
        """
        Получает кортеж с параметрами для поиска, и выводит результат в виде таблицы
        параметры кортежа.

        :param (table имя таблицы, date_in дата начала, date_out дата завершения, number номер (любой),
        responsible ответственный, context строка для поиска по нескольким полям
        )
        """
        self.table.tag_configure("oddrow", background='white')
        self.table.tag_configure("evenrow", background='lightblue')
        count = 0
        contracts = get_contract_bd(param=parameters)

        for contract in contracts:
            if count % 2 == 0:
                row = tuple_contract(contract)
                self.table.insert('', tk.END, values=row, tags=('evenrow',))
            else:
                row = tuple_contract(contract)
                self.table.insert('', tk.END, values=row, tags=('oddrow',))

            count += 1

    def select_records(self, event):
        selected = self.table.focus()
        values = self.table.item(selected, 'values')
        self.values_contract = values
        self.additional_table.update_tab(values)
        self.info_contract.output_selected_records(values)

    def clear_all_records(self):
        self.info_contract.clear_entry()
        for records in self.table.get_children():
            self.table.delete(records)


class AdditionalTableFrame(LabelFrame):
    def __init__(self, data_contract=None):
        super().__init__()
        self.grid(column=0, row=3, sticky='wn')
        self.configure(bg=bg_contract_color, text='Информация о дополнительных соглашениях')
        self.table = ttk.Treeview(self,
                                  show="headings",
                                  selectmode="browse",
                                  columns=heads_additional,
                                  displaycolumns=columns_additional)
        self.table.column('#0', width=0)
        self.table.column('№ допника', width=100)
        self.table.column('Что делает', width=250)
        self.table.column('Дата', width=120)
        self.table.column('Новая дата', width=120)
        self.table.column('Сумма', width=150)
        self.table.column('Коментарий', width=150)

        for header in heads_additional:
            self.table.heading(header, text=header, anchor=tk.CENTER)

        self.out_table_row_additional(data_contract)

        # Скроллы
        self.scroll_table = Scrollbar(self, command=self.table.yview)
        self.table.configure(yscrollcommand=self.scroll_table.set)
        self.scroll_table.pack(side=tk.RIGHT, fill=tk.Y)

        # self.table.pack(side='left', ipady='100', anchor='w')
        self.table.pack(side='left')
        self.table.bind('<<TreeviewSelect>>', self.select_records)


        self.additional_info = InfoAdditionalFrame()

    def out_table_row_additional(self, data_contract):
        self.table.tag_configure("oddrow", background='white')
        self.table.tag_configure("evenrow", background='lightblue')

        if data_contract:
            data_additional = get_additional_db('table_additional_contract', data_contract[11])
            count = 0
            for additional in data_additional:
                if count % 2 == 0:
                    row = tuple_additional(additional)
                    self.table.insert('', tk.END, values=row, tags=('evenrow',))
                else:
                    row = tuple_additional(additional)
                    self.table.insert('', tk.END, values=row, tags=('oddrow',))
                count += 1

    def update_tab(self, additionals):
        self.clear_all_records()
        self.out_table_row_additional(additionals)

    def clear_all_records(self):
        for records in self.table.get_children():
            self.table.delete(records)

    def select_records(self, event):
        selected = self.table.focus()
        values = self.table.item(selected, 'values')
        self.additional_info.output_selected_records(values)


class InfoContractFrame(LabelFrame):
    def __init__(self, contract=None):
        super().__init__()
        self.grid(column=1, row=3, rowspan=2, sticky='wsn')
        self.configure(bg=bg_contract_color,  padx='10', pady='10',
                       text='Информация о договоре')
        self.info_contract = contract

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
        self.date_entry = Entry(self, justify='right')
        self.date_entry.grid(row=5, column=1, columnspan=1, sticky='we', ipadx='10')

        self.date_start_lbl = Label(self, bg=bg_contract_color, text='Дата начала', justify='right')
        self.date_start_lbl.grid(row=6, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.date_start_entry = Entry(self, justify='right')
        self.date_start_entry.grid(row=6, column=1, columnspan=1, sticky='we', ipadx='10')

        self.date_end_lbl = Label(self, bg=bg_contract_color, text='Дата завершения', justify='right')
        self.date_end_lbl.grid(row=7, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.date_end_entry = Entry(self, justify='right')
        self.date_end_entry.grid(row=7, column=1, columnspan=1, sticky='we', ipadx='10')

        self.responsible_lbl = Label(self, bg=bg_contract_color, text='Ответственный', justify='right')
        self.responsible_lbl.grid(row=8, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.responsible_entry = Entry(self, justify='right')
        self.responsible_entry.grid(row=8, column=1, columnspan=1, sticky='we', ipadx='10')

        self.type_contract_lbl = Label(self, bg=bg_contract_color, text='Тип договора', justify='right')
        self.type_contract_lbl.grid(row=9, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.type_contract_entry = Entry(self, justify='right')
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

        self.add_additional_btn = Button(self, text='Добавить новое доп. соглашение',
                                         activebackground=color_bg_btn_activ, command=self.add_additional)
        self.add_additional_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=20, sticky='wn')

        self.update_additional_btn = Button(self, text='Обновить данные', activebackground=color_bg_btn_activ,
                                            command=self.update_contract)
        self.update_additional_btn.grid(row=11, column=2, padx=10, pady=20, sticky='wn')

        self.output_selected_records(contract)

        # self.scroll_y = Scrollbar(self.subject_contract_entry, command=self.subject_contract_entry.yview)
        # self.subject_contract_entry.configure(yscrollcommand=self.scroll_y.set)
        # self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y, anchor='s')

    def add_additional(self):
        # self.add = WinAddAdditional(3)
        WinAddAdditional()

    def update_contract(self):
        ContractUpdate(self.info_contract)

    def output_selected_records(self, contract):
        if contract:
            self.info_contract = contract
            self.clear_entry()

            self.firm_entry.insert(0, contract[2])
            self.num_contract_entry.insert(0, contract[0])
            self.num_contract_in_entry.insert(0, contract[1])
            self.sum_entry.insert(0, contract[6])
            self.date_entry.insert(0, contract[4])
            self.date_start_entry.insert(0, contract[3])
            self.date_end_entry.insert(0, contract[5])
            self.responsible_entry.insert(0, contract[9])
            self.type_contract_entry.insert(0, contract[8])
            self.subject_contract_entry.insert("1.0", contract[7])
            self.comment_entry.insert("1.0", contract[10])

    def clear_entry(self):
        self.firm_entry.delete(0, END)
        self.num_contract_entry.delete(0, END)
        self.num_contract_in_entry.delete(0, END)
        self.sum_entry.delete(0, END)
        self.date_entry.delete(0, END)
        self.date_start_entry.delete(0, END)
        self.date_end_entry.delete(0, END)
        self.responsible_entry.delete(0, END)
        self.type_contract_entry.delete(0, END)
        self.subject_contract_entry.delete("1.0", "end")
        self.comment_entry.delete("1.0", "end")


class InfoAdditionalFrame(LabelFrame):
    def __init__(self):
        super().__init__()

        self.num_additional_id = 0

        self.grid(column=0, row=4, sticky='wens')
        self.configure(bg='#95bfc2', height='300', width='850',
                       text='Информация о дополнительном соглашении')

        self.num_additional_lbl = Label(self, bg=bg_contract_color, text='Номер', justify='right')
        self.num_additional_lbl.grid(row=1, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.num_additional_entry = Entry(self, justify='right')
        self.num_additional_entry.grid(row=1, column=1, columnspan=1, sticky='we', ipadx='10')

        self.date_additional_lbl = Label(self, bg=bg_contract_color, text='Дата', justify='right')
        self.date_additional_lbl.grid(row=2, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.date_additional_entry = Entry(self, justify='right')
        self.date_additional_entry.grid(row=2, column=1, columnspan=1, sticky='we', ipadx='10')

        self.new_date_additional_lbl = Label(self, bg=bg_contract_color, text='Новая дата', justify='right')
        self.new_date_additional_lbl.grid(row=3, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.new_date_additional_entry = Entry(self, justify='right')
        self.new_date_additional_entry.grid(row=3, column=1, columnspan=1, sticky='we', ipadx='10')

        self.sum_additional_lbl = Label(self, bg=bg_contract_color, text='Сумма', justify='right')
        self.sum_additional_lbl.grid(row=4, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.sum_additional_entry = Entry(self, justify='right')
        self.sum_additional_entry.grid(row=4, column=1, columnspan=1, sticky='we', ipadx='10')

        self.what_additional_lbl = Label(self, bg=bg_contract_color, text='Что делает', justify='right')
        self.what_additional_lbl.grid(row=1, column=2, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.what_additional_entry = Text(self, height=6, width=60)
        self.what_additional_entry.grid(row=1, column=3, rowspan=2, columnspan=2, sticky='we', ipadx='10')

        self.comment_additional_lbl = Label(self, bg=bg_contract_color, text='Коментарий', justify='right')
        self.comment_additional_lbl.grid(row=4, column=2, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.comment_additional_entry = Text(self, height=6, width=60)
        self.comment_additional_entry.grid(row=3, column=4, rowspan=2, columnspan=2, sticky='we', ipadx='10')

        self.update_additional_btn = Button(self, text='Обновить данные', activebackground=color_bg_btn_activ,
                                            command=self.update_additional)
        self.update_additional_btn.grid(row=8, column=0, columnspan=2, padx=10, pady=20, sticky='wn')

        # self.scroll_what = Scrollbar(self, command=self.table.yview)
        # self.table.configure(yscrollcommand=self.scroll_table.set)
        # self.scroll_table.pack(side=tk.RIGHT, fill=tk.Y)

    def update_additional(self):
        summ = self.sum_additional_entry
        coment = self.comment_additional_entry.get('1.0', END)
        # log.info(self.num_additional_id)

    def output_selected_records(self, additional):

        if additional:
            self.clear_entry()

            self.num_additional_entry.insert(0, additional[0])
            self.date_additional_entry.insert(0, additional[2])
            self.new_date_additional_entry.insert(0, additional[3])
            self.sum_additional_entry.insert(0, additional[4])
            self.what_additional_entry.insert("1.0", additional[1])
            self.comment_additional_entry.insert("1.0", additional[5])

    def clear_entry(self):
        self.num_additional_entry.delete(0, END)
        self.date_additional_entry.delete(0, END)
        self.new_date_additional_entry.delete(0, END)
        self.sum_additional_entry.delete(0, END)
        self.what_additional_entry.delete("1.0", END)
        self.comment_additional_entry.delete("1.0", END)






app = WinContracts()
app.mainloop()
