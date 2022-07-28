# import tkinter as tk
# from tkinter import ttk
#
#
# from tkcalendar import Calendar, DateEntry
#
#
# def example1():
#     def print_sel():
#         print(cal.selection_get())
#
#     top = tk.Toplevel(root)
#
#     cal = Calendar(top,
#                    font="Arial 14", selectmode='day',
#                    cursor="hand1", year=2022, month=1, day=1)
#     cal.pack(fill="both", expand=True)
#     ttk.Button(top, text="ok", command=print_sel).pack()
#
# def example2():
#     top = tk.Toplevel(root)
#
#     ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
#
#     cal = DateEntry(top, width=12, background='darkblue',
#                     foreground='white', borderwidth=2, locale='ru_RU')
#     cal.pack(padx=10, pady=10)
#
# root = tk.Tk()
# s = ttk.Style(root)
# s.theme_use('clam')
#
# ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
# ttk.Button(root, text='DateEntry', command=example2).pack(padx=10, pady=10)
#
# root.mainloop()


import tkinter

# import ttkcalendar
# import tkSimpleDialog
#
# class CalendarDialog(tkSimpleDialog.Dialog):
#     """Dialog box that displays a calendar and returns the selected date"""
#     def body(self, master):
#         self.calendar = ttkcalendar.Calendar(master)
#         self.calendar.pack()
#
#     def apply(self):
#         self.result = self.calendar.selection
#
#
#
# Demo code:
# def main():
#     root = Tkinter.Tk()
#     root.wm_title("CalendarDialog Demo")
#
#     def onclick():
#         cd = CalendarDialog(root)
#         print cd.result
#
#     button = Tkinter.Button(root, text="Click me to see a calendar!", command=onclick)
#     button.pack()
#     root.update()
#
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     main()
# import tkinter as tk
# from tkinter import font as tkfont
#
# scoreDecisionTree = None
# scoreKnn = None
# scoreRandomForest = None
# scoreKmeans = None
#
#
# class SampleApp(tk.Tk):
#
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#
#         self.title_font = tkfont.Font(
#             family='Helvetica', size=18, weight="bold", slant="italic")
#
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         self.frames = {}
#         self.frames["StartPage"] = StartPage(parent=container, controller=self)
#         self.frames["PageOne"] = PageOne(parent=container, controller=self)
#
#         self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
#         self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame("StartPage")
#
#     def show_frame(self, page_name):
#         '''Show a frame for the given page name'''
#         frame = self.frames[page_name]
#         frame.tkraise()
#
#     def update_globals(self):
#         frame = self.frames["PageOne"]
#         frame.update_globals()
#
# class StartPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         sp = login()
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(
#             self, text="ID playlist canzoni piaciute", font="Times 15")
#         label.pack(side="top", fill="x", pady=10)
#
#         self.entry1 = tk.Entry(self, width=30)
#         self.entry1.pack(side="top", fill="x", pady=10)
#
#         label = tk.Label(
#             self, text="ID playlist canzoni non piaciute", font="Times 15")
#         label.pack(side="top", fill="x", pady=10)
#
#         self.entry2 = tk.Entry(self, width=30)
#         self.entry2.pack(side="top", fill="x", pady=10)
#
#         def parametri():
#             estrazioneCanzoni(sp, self.entry1.get(), self.entry2.get())
#             controller.update_globals()
#             controller.show_frame("PageOne")
#
#         button1 = tk.Button(self, text="Analizza", command=lambda: parametri())
#
#         button1.pack()
#
#
# class PageOne(tk.Frame):
#
#     def __init__(self, parent, controller):
#
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#
#         label = tk.Label(self, text="Accuratezza", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         self.label1 = tk.Label(self, font="Times 12")
#         self.label1.pack(side="top", fill="x", pady=10)
#         self.label2 = tk.Label(self, font="Times 12")
#         self.label2.pack(side="top", fill="x", pady=10)
#         self.label3 = tk.Label(self, font="Times 12")
#         self.label3.pack(side="top", fill="x", pady=10)
#         self.label4 = tk.Label(self, font="Times 12")
#         self.label4.pack(side="top", fill="x", pady=10)
#
#     def update_globals(self):
#         self.label1.config(text="Decision tree: {}".format(scoreDecisionTree))
#         self.label2.config(text="Knn: {}".format(scoreKnn))
#         self.label3.config(text="Random forest: {}".format(scoreRandomForest))
#         self.label4.config(text="Kmeans: {}".format(scoreKmeans))
#
# def login():
#     # just a simple example to allow the program to run
#     return 10
#
#
# def estrazioneCanzoni(sp, a, b):
#     # just a simple example to allow the program to run
#     global scoreDecisionTree, scoreKnn, scoreRandomForest, scoreKmeans
#     scoreDecisionTree, scoreKnn, scoreRandomForest, scoreKmeans = sp, a, b, a+b
#
#
# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()


import re
name = 'Рома Г.Р'


# pattern = r'[а-яА-Яё]{3,}'
pattern = r'[а-яА-Яё]{3,}\s[а-яА-Яё]{,1}\.[а-яА-Яё]{,1}\.'
if re.search(pattern, name):
  print('ok')
else:
    print('not')

# ans =
# a = re.findall(pattern, name)
# print(ans)
# print(a)