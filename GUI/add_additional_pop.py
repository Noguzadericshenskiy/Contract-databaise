from tkinter import Label, Entry, Text, Toplevel

from utils_gui.setups_win import bg_contract_color, color_bg_btn_activ


class WinAddAdditional(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Новое дополнительное соглашение')
        self.grid()
        self.resizable(width=False, height=False)

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

        self.comment_additional_lbl = Label(self, bg=bg_contract_color, text='Записать', justify='right')
        self.comment_additional_lbl.grid(row=4, column=2, columnspan=1, sticky='e', ipadx='10', ipady='5')
        self.comment_additional_entry = Text(self, height=6, width=60)
        self.comment_additional_entry.grid(row=3, column=4, rowspan=2, columnspan=2, sticky='we', ipadx='10')
