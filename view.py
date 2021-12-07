import tkinter as tk


BG_COLOR = '#33ffe6'


class View:

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.win = tk.Tk()
        self.win['bg'] = BG_COLOR
        self._make_label()
        self._make_button()
        self._add_to_win()
        self.win.title('Counter')
        self.win.geometry("500x600+480+120")

    def man(self):
        self.win.mainloop()

    def _make_label(self):
        self.lbl = tk.Label(self.win, text='0')
        self.lbl_top_text = tk.Label(self.win, text='Tap \'-\' to decrement', bg=BG_COLOR)
        self.lbl_bot_text = tk.Label(self.win, text='Tap \'+\' to increment', bg=BG_COLOR)


    def _make_button(self):
        self.btn1 = tk.Button(self.win, text='+', command=self.click_button_incr)
        self.btn2 = tk.Button(self.win, text='-', command=self.click_button_decr)


    def _add_to_win(self):
        self.btn1.place(relx=.5, rely=.5, x=-50, anchor='center', height=30, width=50)
        self.btn2.place(relx=.5, rely=.5, x=50, anchor='center', height=30, width=50)
        self.lbl.place(relx=.5, rely=.5, anchor='center', height=30, width=50)
        self.lbl_top_text.place(relx=.5, rely=.5, y=30, anchor='center', height=30, width=150)
        self.lbl_bot_text.place(relx=.5, rely=.5, y=-30, anchor='center', height=30, width=150)

    def click_button_decr(self):
        self.lbl['text'] = str((self.controller.click_decr()))

    def click_button_incr(self):
        self.lbl['text'] = str((self.controller.click_incr()))
