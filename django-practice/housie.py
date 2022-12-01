
import random as rd
from tkinter import * 
# from tabulate import 
num = list(range(1,91)) 
print(num) 

win = Tk() 
win.title("Housie game !!")
win.configure(bg='silver')
win.geometry('500x300+200+300')
win.minsize(500,300)
win.maxsize(500,300) 
def rnum():
    n = rd.choice(num)
    l = Label(win, text=f"---->>The number is : {n}", width=25, height=3, bg='skyblue', fg='navy', font=('time of roman',20))
    l.place(x=50,y=90)

    p = num.index(n)
    num.pop(p) 
    try:
        n = rd.choice(num) 
        pass 
    except IndexError:
        l = Label(win , text="--->>The end", width=25 , height=3, bg='skyblue',fg = 'navy',font=('time of roman',20))
        l.place(x=50,y=90) 
    
h = Button(win , text='Next', command=rnum, bd=8, bg='blue', fg='white', highlightbackground='navy', height=2,width=10,font=('times of roman',15),activebackground='skyblue',activeforeground='navy')
h.pack(pady=20)

def QUIT():
    win.destroy()

q = Button(win, text='Quit', command=QUIT , bd=8, bg='blue', fg='white', highlightbackground='navy', height=2,width=10,font=('times of roman',15),activebackground='skyblue',activeforeground='navy' )
q.place(x=185,y=200)
mainloop()  
