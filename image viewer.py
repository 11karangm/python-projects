from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("MAVRIN")


myimg1 = ImageTk.PhotoImage(Image.open(r'C:\Users\ASUS\Documents\STUDY\project\gui python\two\images\doge12.jpg'))
myimg2 = ImageTk.PhotoImage(Image.open(r'C:\Users\ASUS\Documents\STUDY\project\gui python\two\images\doge13.jfif'))
myimg3 = ImageTk.PhotoImage(Image.open(r'C:\Users\ASUS\Documents\STUDY\project\gui python\two\images\doge15.png'))
myimg4 = ImageTk.PhotoImage(Image.open(r'C:\Users\ASUS\Documents\STUDY\project\gui python\two\images\dogecoin.png'))



img_list = [myimg1,myimg2,myimg3,myimg4]

mylabel = Label(image = myimg1)
mylabel.grid(row=0,column=0,columnspan=3)
def forward(imn):
    global mylabel
    global button_forward
    global button_back
    mylabel.grid_forget()
    mylabel = Label(image = img_list[imn-1])
    button_forward = Button(root, text=">>",command= lambda: forward(imn+1),bg="skyblue",fg="white",borderwidth=0)
    button_back = Button(root,text = "<<",command = lambda: back(imn-1),bg="skyblue",fg="white",borderwidth=0)
    status =Label(root,pady = 10,text = "image "+ str(imn) +" of " + str(len(img_list)),bd=1,relief = SUNKEN)
    status.grid(row = 2 , column = 0, columnspan =3)
    if imn == 4:
        button_forward = Button(root, text=">>",command= lambda: forward(imn-3),bg="skyblue",fg="white",borderwidth=0)
    mylabel.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)


def back(imn):
    global mylabel
    global button_forward
    global button_back
    mylabel.grid_forget()
    mylabel = Label(image = img_list[imn-1])
    button_forward = Button(root, text=">>",command= lambda: forward(imn+1),bg="skyblue",fg="white",borderwidth=0)
    button_back = Button(root,text = "<<",command = lambda: back(imn-1),bg="skyblue",fg="white",borderwidth=0)
    status =Label(root,pady = 10,text = "image "+ str(imn) +" of " + str(len(img_list)),bd=1,relief = SUNKEN)
    status.grid(row = 2 , column = 0, columnspan =3)
    if imn == 1:
        button_back = Button(root,text = "<<",command = lambda: back(imn+3),bg="skyblue",fg="white",borderwidth=0)
    mylabel.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)


button_back = Button(root,text="<<",borderwidth=0,command = lambda: back(0),bg="skyblue",fg="white")
button_exit = Button(root,text="EXIT",pady = 10,command = root.quit,borderwidth=0,fg="white",bg="#ffcccb")
button_forward = Button(root,text=">>",borderwidth=0,command = lambda : forward(2),bg="skyblue",fg="white")

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

status =Label(root,pady = 10,text = "image 1 of " + str(len(img_list)),bd=1,relief = SUNKEN)

status.grid(row = 2 , column = 0, columnspan =3)


root.mainloop()