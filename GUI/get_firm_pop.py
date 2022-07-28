import tkinter as tk

from tkinter import Button, Label, Entry, Toplevel, ttk, Scrollbar

from utils_gui.setups_win import bg_contract_color, color_bg_btn_activ, heads_firm, list_firm


class GetFirmFrame(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Контрагент')
        self.grid()
        self.configure(bg=bg_contract_color, padx=10, pady=10)
        self.resizable(width=False, height=False)

        self.firm_lbl = Label(self, bg=bg_contract_color, text='Название', justify='right')
        self.firm_lbl.grid(row=1, column=0, sticky='e', ipadx=10, ipady=5)
        self.firm_entry = Entry(self, justify='left')
        self.firm_entry.grid(row=1, column=1, sticky='we', ipadx=10)
        self.firm_btn = Button(self, text='Найти', activebackground=color_bg_btn_activ,
                               command=self.list_firms_by_word)
        self.firm_btn.grid(row=1, column=2, padx=10, pady=10, sticky='wn')

        self.inn_lbl = Label(self, bg=bg_contract_color, text='ИНН', justify='right')
        self.inn_lbl.grid(row=2, column=0, sticky='e', ipadx=10, ipady=5)
        self.inn_entry = Entry(self, justify='right')
        self.inn_entry.grid(row=2, column=1, sticky='we', ipadx=10)
        self.inn_btn = Button(self, text='Найти', activebackground=color_bg_btn_activ,
                              command=self.list_firms_by_inn)
        self.inn_btn.grid(row=2, column=2, padx=10, pady=10, sticky='wn')

        self.table = ttk.Treeview(self,
                                  show="headings",
                                  selectmode="browse",
                                  columns=heads_firm,
                                  displaycolumns=list_firm
                                  )

        self.table.column('id', width=80)
        self.table.column('Название', width=300, anchor='center')
        self.table.column('Полное название', width=450, anchor='e')
        self.table.column('ИНН', width=150, anchor='e')
        self.table.column('СМСП', width=50, anchor='e')

        self.table.grid(column=0, columnspan=4, sticky='we')

        for header in heads_firm:
            self.table.heading(header, text=header, anchor=tk.CENTER)

        self.scroll_table = Scrollbar(self, command=self.table.yview)
        self.table.configure(yscrollcommand=self.scroll_table.set)
        # self.scroll_table.pack(side=tk.RIGHT, fill=tk.Y)
        self.scroll_table.grid(column=5, sticky='nswe')
        self.table.bind('<<TreeviewSelect>>', self.select_records)



    def list_firms_by_word(self):
        ...

    def list_firms_by_inn(self):
        ...

    def select_records(self):
        ...
        # selected = self.table.focus()
        # text = self.table.item(selected, 'values')
        # print(text)
        # self.info_lbl = Label(self, bg=bg_contract_color, text=text, justify='right')
        # self.info_lbl.grid(row=11, column=0, sticky='e', ipadx='10', ipady='5')

    def out_table(self):
        ...