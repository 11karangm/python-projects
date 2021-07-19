from tkinter import *

root = Tk()
root.title("Simple calculator")
E = Entry(root,width = 35,borderwidth = 0)
E.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def bc(number):
    #E.delete(0,END)
    current = E.get()
    E.delete(0,END)
    E.insert(0,str(current) + str(number))
def bclear():
    E.delete(0,END)
def badd():
    fs = E.get()
    global fn 
    global math
    math = "add"
    fn = int(fs)
    E.delete(0,END)

def bqual():
    ss = E.get()
    E.delete(0,END)
    
    if math == "add":
        E.insert(0,fn + int(ss))
    if math == "subtract":
        E.insert(0,fn - int(ss))
    if math == "divide":
        E.insert(0,fn / int(ss))
    if math == "multiply":
        E.insert(0,fn * int(ss))

def bsub():
    fs = E.get()
    global fn 
    global math
    math ="subtract"
    fn = int(fs)
    E.delete(0,END)

def bdiv():
    fs = E.get()
    global fn 
    global math
    math = "divide"
    fn = int(fs)
    E.delete(0,END)

def bmul():
    fs = E.get()
    global fn 
    global math
    math = "multiply"
    fn = int(fs)
    E.delete(0,END)

Button0 = Button(root,text = '0',padx=40,pady=20,command = lambda: bc(0), borderwidth =0)
Button1 = Button(root,text = '1',padx=40,pady=20,command = lambda: bc(1) , borderwidth =0)
Button2 = Button(root,text = '2',padx=40,pady=20,command = lambda: bc(2) , borderwidth =0)
Button3 = Button(root,text = '3',padx=40,pady=20,command = lambda: bc(3) , borderwidth =0)
Button4 = Button(root,text = '4',padx=40,pady=20,command = lambda: bc(4) , borderwidth =0)
Button5 = Button(root,text = '5',padx=40,pady=20,command = lambda: bc(5), borderwidth =0)
Button6 = Button(root,text = '6',padx=40,pady=20,command = lambda: bc(6) , borderwidth =0)
Button7 = Button(root,text = '7',padx=40,pady=20,command = lambda: bc(7) , borderwidth =0)
Button8 = Button(root,text = '8',padx=40,pady=20,command = lambda: bc(8) , borderwidth =0)
Button9 = Button(root,text = '9',padx=40,pady=20,command = lambda: bc(9) , borderwidth =0)
ButtonC = Button(root,text = 'C',padx=79,pady=20,command = bclear , borderwidth =0)
ButtonAdd = Button(root,text = '+',padx=39,pady=20,command = badd , borderwidth =0,bg = 'light yellow')
ButtonEquals = Button(root,text = '=',padx=91,pady=20,bg = 'skyblue',command = bqual , borderwidth =0)

ButtonSub = Button(root,text = '-',padx=43,pady=20,bg='light pink',command = bsub , borderwidth =0)
ButtonDiv = Button(root,text = '/',padx=45,pady=20,bg = 'orange',command = bdiv , borderwidth =0)
ButtonMul = Button(root,text = 'x',padx=40,pady=20,bg = 'light green',command = bmul , borderwidth =0)
#placing buttons on screen

Button1.grid(row=3,column =0)
Button2.grid(row=3,column =1)
Button3.grid(row=3,column =2)

Button4.grid(row=2,column =0)
Button5.grid(row=2,column =1)
Button6.grid(row=2,column =2)

Button7.grid(row=1,column =0)
Button8.grid(row=1,column =1)
Button9.grid(row=1,column =2)

Button0.grid(row=4,column=0)

ButtonC.grid(row= 4, column= 1,columnspan=2 )
ButtonAdd.grid(row= 5, column=0 )
ButtonSub.grid(row = 5,column =1)
ButtonDiv.grid(row = 5,column =2)

ButtonEquals .grid(row=6 , column=1 ,columnspan=2 )
ButtonMul.grid(row = 6,column =0)



#myButton = Button(root,text = "Enter your name", padx = 50,fg = 'blue',bg='red')

root.mainloop()