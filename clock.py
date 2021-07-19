from tkinter import *
import time

root = Tk()
root.title('Clock')
root.geometry('600x400')

def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    ampm = time.strftime("%p")
    zone = time.strftime("%Z")

    myLabel.config(text = hour + ":" + minute + ":" + second + ":" + ampm)
    myLabel.after(1000,clock)
    myLabel2.config(text = day)
    mylabel3.config(text=zone)

myLabel = Label(root,text = "", font = ("helvetica 48 "),bg="pink",fg="royal blue")
myLabel.pack(pady = 50)

myLabel2 = Label(root,text="",font="helvetica 18 ")
myLabel2.pack()

mylabel3=Label(root,text="",font="helvetica 18")
mylabel3.pack()
#myLabel.after(3000, Update)

clock()

#timer

E = Entry(root)
E.pack()
hours = 0
seconds = 0
minutes = 0

minutes_total = 1

minutes_end = 1
def setting():
    global hours
    global minutes
    global minutes_total
    a = E.get()
#to make sure minutes_total is not an empty string , because empty string can't be changed to integer
    #if a != "" :
    minutes_total = int(a)
    hours = minutes_total//60
    minutes = minutes_total%60
    seconds = 60
    
#minutes_end = int(minutes_end)


def reset():
    global hours
    global minutes
    global seconds
    global minutes_end
    global minutes_total

    hours = 0
    minutes = 0
    seconds = 0
    timerlabel.config(text = 'FUNTIME' )
    
    

def timer():
    global seconds 
    global minutes
    global hours
    global minutes_total
    global minutes_end
    timerlabel.config(text = '%i:%i:%i'%(hours,minutes,seconds) )
    if seconds<1:
        seconds = 60
        minutes = minutes - 1
        minutes_total = minutes_total - 1
    if minutes<1:
        if hours>0:
            hours = hours - 1 
            minutes = 60
    
   
    seconds = seconds - 1
    #timerlabel.after(1000,timer)

    if minutes_total >= 0:
        timerlabel.after(1000,timer)
    else:
        reset()

myButton = Button(root,text = "SET",font = "helvetica 13" , bg ="red",fg="black",command = setting)
myButton.pack()
timerlabel = Label(root,text="",font = "helvetica 48" , bg= "black",fg="red")
timerlabel.pack()

myButton2 = Button(root,text = "START",font = "helvetica 13" , bg ="red",fg="black",command = timer)
myButton2.pack()


#timer()

root.mainloop()