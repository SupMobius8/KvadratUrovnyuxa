from tkinter import *
from random import *

#def klikker(event):



def text_to_lbl(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)


aken=Tk()
aken.title("Решаем без смс и реги")
aken.geometry("600x500")
btn1=Button(aken,text="Рeшить",font="Arial 20",fg="black",bg="green",width=8,height=1,relief=SUNKEN)
lbl1=Label(aken,text="ИЗИ РЕШАЛКА Квадрат Уровнюхи",font="Arial 20",fg="green",bg="lightblue",width=29,height=1,relief=SUNKEN)
lbl2=Label(aken,text="x**2+",font="Arial 20",fg="green",width=4,height=1)
lbl3=Label(aken,text="x+",font="Arial 20",fg="green",width=2,height=1)
lbl4=Label(aken,text="решение",font="Arial 20",fg="black",bg="yellow",width=60,height=3,)
lbl5=Label(aken,text="  ",width=2,height=1)
lbl6=Label(aken,text="  ",width=2,height=1)
lbl7=Label(aken,text="  ",width=2,height=1)
ent1=Entry(aken,fg="blue",bg="lightblue",width=3, font="Arial 20")
ent2=Entry(aken,fg="blue",bg="lightblue",width=3, font="Arial 20")
ent3=Entry(aken,fg="blue",bg="lightblue",width=3, font="Arial 20")


#btn1.bind("<Button-1>",klikker)#LKM
#btn1.bind("<Button-3>",klikker)#PKM
lbl1.pack()
lbl5.pack()
ent1.pack()
lbl2.pack()
ent2.pack()
lbl3.pack()
ent3.pack()
lbl7.pack()
btn1.pack()
lbl6.pack()
lbl4.pack()
aken.mainloop()
