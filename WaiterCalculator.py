# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
root.geometry('550x250')
frame = Frame(root)
frame.grid()

st = StringVar()
en = StringVar()
ta = StringVar()

def sum():
    resl.delete(0, END)
    if st.get().isdigit() and en.get().isdigit(): 
        nach = float(st.get())  
        con = float(en.get())
    elif float(st.get()) > (en.get()):
        pass
    
    if con == 1:
        con = 25
    chas = con - nach
    tx = 0
    if 18 > nach:
        tx = (18 - nach) * 49
        chas = chas - (18 - nach)
    
    if con < 22:
        tx += chas * 21
    elif con > 22:
        tx += (22 - nach) * 21 + (chas - (22 - nach)) * 25.2
        
    if ta.get():
        tea = float(ta.get())
        tx += tea
    resl.insert(END, 'Результат = ' + str(tx) + ' руб')


entl = Label(text='День')
ent = Entry(width='15')
entl.grid(column=0,row=0)
ent.grid(column=0,row=1)

startl = Label(text="Начало работы")
start = Entry(width='5', textvariable = st)
startl.grid(column=1, row=0)
start.grid(column=1, row=1, padx='10')

endl = Label(text='Конец работы')
end = Entry(width='5', textvariable = en)
endl.grid(column=2, row=0)
end.grid(column=2, row=1, padx='10')

teal = Label(text='Чай')
tea = Entry(width='5', textvariable = ta)
teal.grid(column=3, row=0)
tea.grid(column=3, row=1)

res_but = Button(text='Посчитать', command=sum)
res_but.grid(column=4, row=1, padx=10) 

resleb = Label(text='Выручка')
resl = Entry(root, width=20)
resleb.grid(column=5, row=0)
resl.grid(column=5, row=1, padx=10)  











root.mainloop()