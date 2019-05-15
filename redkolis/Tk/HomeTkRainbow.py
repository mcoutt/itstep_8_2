from tkinter import *


def red():
    l1.config(text='красный')
    l0.delete(0, END)
    l0.insert(0, '#ff0000')


def orange():
    l1.config(text='оранжевый')
    l0.delete(0, END)
    l0.insert(0, '#ff7d00')


def yellow():
    l1.config(text='желтый')
    l0.delete(0, END)
    l0.insert(0, '#ffff00')


def green():
    l1.config(text='зеленый')
    l0.delete(0, END)
    l0.insert(0, '#00ff00')


def cyan():
    l1.config(text='голубой')
    l0.delete(0, END)
    l0.insert(0, '#007dff')


def blue():
    l1.config(text='синий')
    l0.delete(0, END)
    l0.insert(0, '#0000ff')


def purple():
    l1.config(text='фиолетовый')
    l0.delete(0, END)
    l0.insert(0, '#7d00ff')


root = Tk()
root.geometry('120x222')

l1 = Label(width=17)
l1.pack()

l0 = Entry(justify=CENTER)
l0.pack()

b1 = Button(width=16, bg="#ff0000", command=red)
b1.pack()

b2 = Button(width=16, bg="#ff7d00", command=orange)
b2.pack()

b3 = Button(width=16, bg="#ffff00", command=yellow)
b3.pack()

b4 = Button(width=16, bg="#00ff00", command=green)
b4.pack()

b5 = Button(width=16, bg="#007dff", command=cyan)
b5.pack()

b6 = Button(width=16, bg="#0000ff", command=blue)
b6.pack()

b7 = Button(width=16, bg="#7d00ff", command=purple)
b7.pack()

root.mainloop()
