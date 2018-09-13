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
        self.new.grid(column=3, row=arw)
        self.new_day()
        
    def sm(self):
        self.resl.delete(0, tk.END)
        if self.st.get().isdigit() and self.en.get().isdigit(): 
            nach = float(self.st.get())  
            con = float(self.en.get())
            if nach > con:
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
        
            if self.ta.get():
                tea = float(self.ta.get())
                tx += tea
    
            self.resl.insert(tk.END, 'Результат = ' + str(tx) + ' руб')
    
    def new_day(self):
        self.st = tk.StringVar()
        self.en = tk.StringVar()
        self.ta = tk.StringVar()
        
        
        ent = tk.Entry(self.root, width='15')
        ent.grid(column=0,row=self.rw, padx=5)
    
        start = tk.Entry(self.root, width='5', textvariable = self.st)
        start.grid(column=1, row=self.rw, padx='10')
    
        end = tk.Entry(self.root, width='5', textvariable = self.en)
        end.grid(column=2, row=self.rw, padx='10')

        tea = tk.Entry(self.root, width='5', textvariable = self.ta)
        tea.grid(column=3, row=self.rw)
    
        res_but = tk.Button(self.root, text='Посчитать', command=self.sm)
        res_but.grid(column=4, row=self.rw, padx=10) 

        self.resl = tk.Entry(self.root,  width=20)
        self.resl.grid(column=5, row=self.rw, padx=10) 
        
        self.new.grid(column=3, row=self.arw)
        self.rw += 1
        self.arw += 1

def main():
    root = tk.Tk()
    root.geometry('600x250')
    root.title('Waiters calculator')
    a = Calcul(root, arw)
    root.mainloop()

if __name__ == '__main__':
    main()