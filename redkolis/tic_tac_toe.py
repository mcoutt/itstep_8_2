from tkinter import *


class Block:
    def __init__(self, root):
        self.f_top = Frame(root)
        self.f_mid = Frame(root)
        self.f_down = Frame(root)
        self.b1 = Button(self.f_top, width=3, text='', command=self.one, font=("Arial 32", 24, "bold"))
        self.b2 = Button(self.f_top, width=3, text='', font=("Arial 32", 24, "bold"))
        self.b3 = Button(self.f_top, width=3, text='', font=("Arial 32", 24, "bold"))
        self.b4 = Button(self.f_mid, width=3, text='', font=("Arial 32", 24, "bold"))
        self.b5 = Button(self.f_mid, width=3, text='', font=("Arial 32", 24, "bold"))
        self.b6 = Button(self.f_mid, width=3, text='', font=("Arial 32", 24, "bold"))
        self.b7 = Button(self.f_down, width=3, text='', font=("Arial 32", 24, "bold"))
        self.b8 = Button(self.f_down, width=3, text='', font=("Arial 32", 24, "bold"))
        self.b9 = Button(self.f_down, width=3, text='', font=("A rial 32", 24, "bold"))
        self.b1.config(bd=3)
        self.b2.config(bd=3)
        self.b2.config(bd=3)
        self.b3.config(bd=3)
        self.b4.config(bd=3)
        self.b5.config(bd=3)
        self.b6.config(bd=3)
        self.b7.config(bd=3)
        self.b8.config(bd=3)
        self.b9.config(bd=3)
        self.f_top.pack()
        self.f_mid.pack()
        self.f_down.pack()
        self.b1.pack(side=LEFT)
        self.b2.pack(side=LEFT)
        self.b3.pack(side=LEFT)
        self.b4.pack(side=LEFT)
        self.b5.pack(side=LEFT)
        self.b6.pack(side=LEFT)
        self.b7.pack(side=LEFT)
        self.b8.pack(side=LEFT)
        self.b9.pack(side=LEFT)

    def one(self):
        self.b1.config(text='X')
        print(self.b1())


master = Tk()

b = Block(master)
b.one()

master.mainloop()
