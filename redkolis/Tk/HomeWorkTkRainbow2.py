from tkinter import *


def red():
    l1.config(text='красный')
    e1.delete(0, END)
    e1.insert(0, '#ff0000')


def orange():
    l1.config(text='Оранжевый')
    e1.delete(0, END)
    e1.insert(0, '#ff7d00')


def yellow():
    l1.config(text='желтый')
    e1.delete(0, END)
    e1.insert(0, '#ffff00')


def green():
    l1.config(text='зеленый')
    e1.delete(0, END)
    e1.insert(0, '#00ff00')


def cyan():
    l1.config(text='голубой')
    e1.delete(0, END)
    e1.insert(0, '#007dff')


def blue():
    l1.config(text='синий')
    e1.delete(0, END)
    e1.insert(0, '#0000ff')


def purple():
    l1.config(text='фиолетовый')
    e1.delete(0, END)
    e1.insert(0, '#7d00ff')


root = Tk()

f1 = Frame()
f1.pack()

l1 = Label(f1, width=20)
l1.pack()

e1 = Entry(f1, width=20, justify=CENTER)
e1.pack()

b1 = Button(f1, width=2, bg='#ff0000')
b1['command'] = red
b1.pack(side=LEFT, padx=1)

b2 = Button(f1, width=2, bg='#ff7d00')
b2['command'] = orange
b2.pack(side=LEFT, padx=1)

b3 = Button(f1, width=2, bg='#ffff00')
b3['command'] = yellow
b3.pack(side=LEFT, padx=1)

b4 = Button(f1, width=2, bg='#00ff00')
b4['command'] = green
b4.pack(side=LEFT, padx=1)

b5 = Button(f1, width=2, bg='#007dff')
b5['command'] = cyan
b5.pack(side=LEFT, padx=1)

b6 = Button(f1, width=2, bg='#0000ff')
b6['command'] = blue
b6.pack(side=LEFT, padx=1)

b7 = Button(f1, width=2, bg='#7d00ff')
b7['command'] = purple
b7.pack(side=LEFT, padx=1)

root.mainloop()
