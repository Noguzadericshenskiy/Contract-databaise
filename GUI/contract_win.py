# import sqlite3

import tkinter as tk

import logging

from tkinter import ttk, Menu, Button, Label, Entry, Tk, Frame
from tkinter import filedialog as fd

from modules import *
from hendlers_gui import tuple_contract, tuple_additional
from utils_gui.setups_win import *


log = logging.getLogger("main")
logging.basicConfig(level=logging.INFO)


class WinContract(Tk):
    def __init__(self):
        super(WinContract, self).__init__()
        self.title('База данных договоров')
        self.minsize(1024, 800)
        self.maxsize(1920, 1080)
        self.bold_font = "bold"

        self._main_menu()
        self._put_frames()

    def _main_menu(self):
        self.main_menu = Menu(self, background="#67dbb8")
        self.config(menu=self.main_menu)

        self.contract_menu = Menu(self.main_menu, tearoff=0, background=color_bg_menu)
        self.contract_menu.add_command(label="Показать все контракты")
        self.contract_menu.add_command(label="Найти по номеру")
        self.contract_menu.add_command(label="")
        self.contract_menu.add_command(label="")
        self.contract_menu.add_command(label="")

        self.additional_menu = Menu(self.main_menu, tearoff=0, background=color_bg_menu)
        self.additional_menu.add_command(label="Найти доп соглашение")
        self.additional_menu.add_command(label="Показать все допники")
        self.additional_menu.add_command(label="")
        self.additional_menu.add_command(label="")
        self.additional_menu.add_command(label="")

        self.record_menu = Menu(self.main_menu, tearoff=0, background=color_bg_menu)
        self.record_menu.add_command(label="Охуительный отчет 1")
        self.record_menu.add_command(label="")
        self.record_menu.add_command(label="")
        self.record_menu.add_command(label="")
        self.record_menu.add_command(label="Охуительный отчет n")

        self.admin_menu = Menu(self.main_menu, tearoff=0, background=color_bg_menu)
        self.admin_menu.add_command(label="Создать нового пользователя")
        self.admin_menu.add_command(label="Сбросить пароль пользователя")
        self.admin_menu.add_command(label="Удалить пользователя")
        self.admin_menu.add_command(label="Создать новую БД", command=self.create_bd)
        self.admin_menu.add_command(label="Указать путь до БД", command=self.get_dir_bd)

        self.quit_menu = Menu(self.main_menu, tearoff=0, background='#f05e0a', activebackground='#de2137')
        self.quit_menu.add_command(label="Завершить работу", command=self.quit_app)

        self.main_menu.add_cascade(label="Договоры", menu=self.contract_menu)
        # self.main_menu.add_cascade(label="Договоры 44", menu=self.contract_44_menu)
        # self.main_menu.add_cascade(label="Договоры", menu=self.contract_menu)
        # self.main_menu.add_cascade(label="Договоры СМСП", menu=self.contract_SMSP_menu)
        self.main_menu.add_cascade(label="Доп соглашения", menu=self.additional_menu)
        self.main_menu.add_cascade(label="Отчеты", menu=self.record_menu)
        self.main_menu.add_cascade(label="Admin menu", menu=self.admin_menu)
        self.main_menu.add_cascade(label="Exit", menu=self.quit_menu)

    def _put_frames(self):
        self.frame_up_contract = FrameUpContract()
        self.frame_table_contract = ContractTableFrame()

    def get_dir_bd(self):
        # Получаем директорию с файлом или бд
        # функцию можно вынести наружу метода
        path = fd.askdirectory()
        print(path)

    def create_bd(self):
        path_bd = fd.askdirectory()
        print(path_bd)

    def quit_app(self):
        self.quit()


class FrameUpContract(Frame):
    """
    Класс для работы с выводом информации в виджете под меню на всех окнах в договорах
    """

    def __init__(self):
        super().__init__()
        self.pack(side=tk.TOP, fill='x')
        self.configure(height='150')

        self._put_widgets()

    def _put_widgets(self):
        date_from_lbl = Label(self, text='Начало периода')
        date_from_lbl.grid(row=0, column=0, padx=30)
        date_to_lbl = Label(self, text='Конец периода')
        date_to_lbl.grid(row=1, column=0, padx=30)

        date_from_in = Entry(self)
        date_from_in.grid(row=0, column=1, padx=30)
        date_to_in = Entry(self)
        date_to_in.grid(row=1, column=1, padx=30)

        search_btn = Button(self, text='Найти', activebackground=color_bg_btn_activ)
        search_btn.grid(row=0, rowspan=2, column=24, ipadx=50, padx=50)


class ContractTableFrame(Frame):
    """
    Класс выводит таблицу договоров переопределяется в соответствии с выбором таблицы договоров
    Возможно добавлю сюда виджеты из верхнего фрейма.
    """

    def __init__(self):
        super().__init__()
        self.pack(side=tk.TOP, fill='x')
        self.configure(height='600')
        self._put_widgets()

    def _put_widgets(self):
        self.table = ttk.Treeview(self, show="headings", selectmode="browse",
                                  columns=heads_contract, displaycolumns=columns_contract)

        self.table.column('id', minwidth=10, width=80)
        self.table.column('№ договора', minwidth=10, width=150)
        self.table.column('№(входящий)', minwidth=10, width=150)
        self.table.column('Контрагент', minwidth=10, width=300)
        self.table.column('Предмет договора', minwidth=10, width=300)
        self.table.column('comment', minwidth=10, width=200)
        self.table.column('Дата начала', minwidth=10, width=100)
        self.table.column('Дата закл', minwidth=10, width=100)
        self.table.column('Дата окончания', minwidth=10, width=100)
        self.table.column('Сумма', minwidth=10, width=150)
        self.table.column('Ответственный', minwidth=10, width=200)
        self.table.column('Тип договора', minwidth=10, width=150)

        for header in heads_contract:
            self.table.heading(header, text=header, anchor=tk.CENTER)

        for contract in get_all_contract_db():
            row = tuple_contract(contract)
            self.table.insert('', tk.END, values=row)
        # Скроллы
        self.scroll_table = tk.Scrollbar(self, command=self.table.yview)
        self.table.configure(yscrollcommand=self.scroll_table.set)
        self.scroll_table.pack(side=tk.RIGHT, fill=tk.Y)
        # self.scroll_table_x = tk.Scrollbar(self, command=self.table.xview)
        # self.table.configure()
        # self.scroll_table_x.pack(side=tk.BOTTOM, fill=tk.X)



        rew = self.selection_get()
        re = self.table.focus_get()
        log.info(rew)
        log.info(re)




        # Запуск фрейма
        self.table.pack(ipady='150', fill='x')
        # Функция обратного вызова
        self.table.bind('<<TreeviewSelect>>', self.output_select)

        self.frame_table_additional = AdditionalTableFrame()
        # self.frame_info_contract_additional = InfoContractAndAdditionalFrame()


    # Функция обратного вызова
    def output_select(self, event):
        for selection in self.table.selection():
            item = self.table.item(selection)
            values_data = item["values"]
            self.frame_table_additional.destroy()
            self.frame_table_additional = AdditionalTableFrame(values_data)

            # self.rame_info_contract_additional = InfoContractAndAdditionalFrame(values_data)


class AdditionalTableFrame(Frame):
    """
    Общий фрейм для низа окна с договорами
    включет фреймы вывода таблицы с допниками и информамцию о выбранном договоре/допнике
    """

    def __init__(self, data_contract=None):
        super().__init__()
        self.configure(height='800')
        self.pack(side=tk.LEFT, fill='y')

        self._put_table_additional(data_contract)

    def _put_table_additional(self, data_contract):
        self.table = ttk.Treeview(self, show="headings", selectmode="browse",
                                  columns=heads_additional, displaycolumns=columns_additional)
        # self.table.column('ID', minwidth=50, width=150)
        self.table.column('№ допника', minwidth=50, width=150)
        # self.table.column('№ договора', minwidth=50, width=150)
        self.table.column('Что делает', minwidth=50, width=300)
        self.table.column('Дата', minwidth=20, width=200)
        self.table.column('Новая дата', minwidth=20, width=100)
        self.table.column('Сумма', minwidth=20, width=100)
        self.table.column('Коментарий', minwidth=50, width=100)

        for header in heads_additional:
            self.table.heading(header, text=header, anchor=tk.CENTER)

        if data_contract:
            # log.info(f'header:  {data_contract}')
            data_additional = get_additional_db('table_additional_contract', data_contract[0])[:6]
            # log.info(f"data_additional{data_additional}")
            for additional in data_additional:
                row = tuple_additional(additional)
                # log.info(f'row:  {row}')
                self.table.insert('', tk.END, values=row)

        self.table.pack(side='left', ipady='150')

        self.scroll_table = tk.Scrollbar(self, command=self.table.yview)
        self.table.configure(yscrollcommand=self.scroll_table.set)
        self.scroll_table.pack(side=tk.RIGHT, fill=tk.Y)


class InfoContractAndAdditionalFrame(Frame):
    def __init__(self, contract=None):
        super().__init__()
        self.configure(height='800', background='#74e0e8')
        self.pack(anchor='e', fill='x')
        # self.grid(sticky='nswe')
        self.contract = contract

        self.pack_propagate(False)




app = WinContract()
app.mainloop()
