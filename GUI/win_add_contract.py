from tkinter import Button, Label, Entry, Text, Toplevel
from tkcalendar import DateEntry

from utils_gui.setups_win import bg_contract_color, color_bg_btn_activ
from GUI.get_firm_pop import GetFirmFrame



class ContractAdd(Toplevel):
    def __init__(self):
        super().__init__()
        self.resizable(width=False, height=False)
        self.title('Создание договора')
        self.grid()
        self.configure(bg=bg_contract_color, padx='10', pady='10',)

        self.firm_lbl = Label(self, bg=bg_contract_color, text='Контрагент', justify='right')
        self.firm_lbl.grid(row=1, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.firm_entry = Entry(self, justify='left')
        self.firm_entry.grid(row=1, column=1, columnspan=3, sticky='we', ipadx='10')

        self.firm_btn = Button(self, text='...', activebackground=color_bg_btn_activ,
                               command=self.launch_company_frame)
        self.firm_btn.grid(row=1, column=4)

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
        self.date_entry = DateEntry(self, width=12, background='darkblue',
                                    foreground='white', borderwidth=2, locale='ru_RU')
        self.date_entry.grid(row=5, column=1, columnspan=1, sticky='we', ipadx='10')

        self.date_start_lbl = Label(self, bg=bg_contract_color, text='Дата начала', justify='right')
        self.date_start_lbl.grid(row=6, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.date_start_entry = DateEntry(self, width=12, background='darkblue',
                                          foreground='white', borderwidth=2, locale='ru_RU')
        self.date_start_entry.grid(row=6, column=1, columnspan=1, sticky='we', ipadx='10')

        self.date_end_lbl = Label(self, bg=bg_contract_color, text='Дата завершения', justify='right')
        self.date_end_lbl.grid(row=7, column=0, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.date_end_entry = DateEntry(self, width=12, background='darkblue',
                                        foreground='white', borderwidth=2, locale='ru_RU')
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

        self.comment_lbl = Label(self, bg=bg_contract_color, text='Комментарий', justify='right')
        self.comment_lbl.grid(row=6, column=2, sticky='e', ipadx='10', ipady='5', padx='20')
        self.comment_entry = Text(self, height=5)
        self.comment_entry.grid(row=7, column=2, rowspan=3, sticky='we', ipadx='10', padx='20')

        self.update_additional_btn = Button(self, text='Сохранить данные', activebackground=color_bg_btn_activ,
                                            command=self.save_contract)
        self.update_additional_btn.grid(row=11, column=2, padx=10, pady=20, sticky='wn')

    def save_contract(self):
        # Добавить обработку сохранения договора в базу данных
        self.destroy()

    def launch_company_frame(self):
        self.get_firm = GetFirmFrame()

        ...

    def get_responsible(self):
        ...

    def get_type_contract(self):
        ...

    def check_data(self):
        ...

    def output_selected_records(self):
        firm = self.firm_entry.get()
        num = self.num_contract_entry.get()
        num_in = self.num_contract_in_entry.get()
        summ = self.sum_entry.get()
        date = self.date_entry.get()
        date_start = self.date_start_entry.get()
        date_end = self.date_end_entry.get()
        responsible = self.responsible_entry.get()
        type_contract = self.type_contract_entry.get()
        subject = self.subject_contract_entry.get("1.0")
        comment = self.comment_entry.get("1.0")



