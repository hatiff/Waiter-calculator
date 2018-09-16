# -*- coding: utf-8 -*-
import tkinter as tk

arw = 2

class Calcul(tk.Frame):
    def __init__(self, root, arw):
        tk.Frame.__init__(self, root)
        self.arw = arw
        self.root = root
        self.arw = arw 
        self.rw = 1
        self.month = 0
        self.start()
        
    def start(self):
        entl = tk.Label(text='День')
        entl.grid(column=0,row=0)

        startl = tk.Label(text="Начало работы")
        startl.grid(column=1, row=0)

        endl = tk.Label(text='Конец работы')
        endl.grid(column=2, row=0)
    
        teal = tk.Label(text='Чай')
        teal.grid(column=3, row=0)

        resleb = tk.Label(text='Выручка')
        resleb.grid(column=5, row=0)

        self.new = tk.Button(text='Добавить день', command=self.new_day)
        self.mes = tk.Button(self.root, text='Общая', command=self.total)
        self.tot = tk.Entry(self.root, width=15)
        
        self.new_day()
        
    def total(self):
        self.tot.delete(0, tk.END)
        self.tot.insert(tk.END, str(self.month))
    
    def sm(self, st, en, ta, resl):
        resl.delete(0, tk.END)
        tx = 0
        
        if st.get().isdigit() and en.get().isdigit():
            nach = float(st.get())  
            con = float(en.get())

            
            if con == 1:
                con = 25
            chas = con - nach
            if 18 > nach:
                tx = (18 - nach) * 49
                chas = chas - (18 - nach)
    
            if con < 22:
                tx += chas * 21
            elif con > 22:
                tx += (22 - nach) * 21 + (chas - (22 - nach)) * 25.2
              
            if nach == 0 or con == 0:
                tx =0
            
        if ta.get():
            tea = float(ta.get())
            tx += tea
        resl.insert(tk.END, str(tx))
        self.month += tx
    
    
    def new_day(self):
        st = tk.StringVar()
        en = tk.StringVar()
        ta = tk.StringVar()
        re = tk.StringVar()
        ent = tk.Entry(self.root, width='15')
        ent.grid(column=0,row=self.rw, padx=5)
    
        start = tk.Entry(self.root, width='5', textvariable = st)
        start.grid(column=1, row=self.rw, padx='10')
    
        end = tk.Entry(self.root, width='5', textvariable = en)
        end.grid(column=2, row=self.rw, padx='10')

        tea = tk.Entry(self.root, width='5', textvariable = ta)
        tea.grid(column=3, row=self.rw)
    
        res_but = tk.Button(self.root, text='Посчитать')
        res_but.grid(column=4, row=self.rw, padx=10) 

        resl = tk.Entry(self.root,  width=10, textvariable = re)
        resl.grid(column=5, row=self.rw, padx=10)
        res_but['command'] = lambda : self.sm(st, en, ta, resl)
        
        self.new.grid(column=3, row=self.arw)
        self.mes.grid(column=5, row=self.arw)
        self.tot.grid(column=5, row=self.arw + 1)
        self.rw += 1
        self.arw += 1
    
def main():
    root = tk.Tk()
    root.geometry('600x250')
    root.title('Waiters calculator')
    Calcul(root, arw)
    root.mainloop()

if __name__ == '__main__':
    main()