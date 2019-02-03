from tkinter import *


class Application(Frame):
    """ГУІ пріложеніе с кнопкамі."""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = Label(self, text="Чтобы узнать секрет долголетия, введите пароль.")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        self.pw_lbl = Label(self, text="Пароль: ")
        self.pw_lbl.grid(row=1, column=0, sticky=W)
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=1, column=1, sticky=W)
        self.sumbit_bttn = Button(self, text="Узнать секрет", command=self.reveal)
        self.sumbit_bttn.grid(row=2, column=1, sticky=W)
        self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self):
        contents = self.pw_ent.get()
        if contents == "Ярик - каблук":
            message = "Чтобы дожить до 100 лет, надо сначала дожить до 99,\nа потом вести себя очень осторожно."
        else:
            message = "Введен неверный пароль. Тайну сегодня ты не услышишь."
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

root = Tk()
root.title("Долгожитель")
root.geometry("280x150")
app = Application(root)
root.mainloop()