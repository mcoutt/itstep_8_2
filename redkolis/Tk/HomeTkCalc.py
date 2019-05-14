from tkinter import *


class Block:
    def __init__(self, master):
        self.e = Entry(master, text="Number 1")
        self.e1 = Entry(master, text='Number 2')
        self.b = Button(master, text='+', width=10)
        self.b1 = Button(master, text='-', width=10)
        self.b2 = Button(master, text='*', width=10)
        self.b3 = Button(master, text='/', width=10)
        self.l = Label(master, bg='white', fg='black', width=20)
        self.b['command'] = self.add
        self.b1['command'] = self.substract
        self.b2['command'] = self.multiply
        self.b3['command'] = self.divide
        self.e.pack()
        self.e1.pack()
        self.b.pack()
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
        self.l.pack()

    def add(self):
        n = float(self.e.get()) + float(self.e1.get())

        self.l['text'] = n

    def substract(self):
        n = float(self.e.get()) - float(self.e1.get())

        self.l['text'] = n

    def divide(self):
        n = float(self.e.get()) / float(self.e1.get())

        self.l['text'] = n

    def multiply(self):
        n = float(self.e.get()) * float(self.e1.get())

        self.l['text'] = n


root = Tk()

block = Block(root)

root.mainloop()
