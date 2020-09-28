from tkinter import *
from tkinter import ttk

class ParserGUI:
    def __init__(self, master):
        # Окно
        self.master = master
        self.master.title("Parsers")
        self.master.geometry("640x320")
        self.master.iconbitmap('main.ico')

        # Вкладки
        self.tab_bar = ttk.Notebook(self.master)
        self.tab_settings = ttk.Frame(self.tab_bar)
        self.tab_data = ttk.Frame(self.tab_bar)
        self.tab_bar.add(self.tab_settings, text="Настройки")
        self.tab_bar.add(self.tab_data, text="Данные")

        # Рисование вкладки Настроики
        self.label = Label(self.tab_settings, text="This is our first GUI!")
        self.label.grid(row=0, column=0)

        self.greet_button = Button(self.tab_settings, text="Greet", command=self.greet)
        self.greet_button.grid()
        self.close_button = Button(self.tab_settings, text="Close", command=master.quit)
        self.close_button.grid()

        # Рисование вкладки Данные
        self.label = Label(self.tab_data, text="This is second tab!")
        self.label.grid(row=0, column=0)

        # Собрать вкладки
        self.tab_bar.pack(expand=1, fill='both')



    def greet(self):
        print("Greetings!")



root = Tk()
my_gui = ParserGUI(root)

root.mainloop()