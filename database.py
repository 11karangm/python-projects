from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("3")
root.geometry("400x400")

# Database

#create or connect database

conn = sqlite3.connect('adress_book.db')
c = conn.cursor()#create cursor
'''

#create table
c.execute("""CREATE TABLE addresses (
    f_name text,
    l_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )

""")

'''
#c.execute("DROP TABLE addresses")
def submit():
        
    conn = sqlite3.connect('adress_book.db')
    c = conn.cursor()#create cursor

    #INSERT INTO
    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:city,:state,:zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
                
            })

    conn.commit()
    #close
    conn.close

    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

def query():
    conn = sqlite3.connect('adress_book.db')
    c = conn.cursor()#create cursor

    c.execute("SELECT * , oid FROM addresses")
    records = c.fetchall()
    #print(records)
    printrecords=''
    for record in records :
        printrecords += str(record)+"\n"

    query_label = Label(root,text=printrecords)
    query_label.grid(row=8,column=0,columnspan=2)
    
    conn.commit()
    #close
    conn.close


f_name = Entry(root,width = 35)
f_name.grid(row=0,column=1,padx =20)

l_name = Entry(root,width = 35)
l_name.grid(row=1,column=1,padx =20)

address = Entry(root,width = 35)
address.grid(row=2,column=1,padx =20)

city = Entry(root,width = 35)
city.grid(row=3,column=1,padx =20)

state = Entry(root,width = 35)
state.grid(row=4,column=1,padx =20)

zipcode = Entry(root,width = 35)
zipcode.grid(row=5,column=1,padx =20)

#create text box labels
f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0 ,column=0)

l_name_label = Label(root,text="Last Name")
l_name_label.grid(row=1 ,column=0)

address_label = Label(root,text="Address")
address_label.grid(row=2 ,column=0)

city_label = Label(root,text="City")
city_label.grid(row=3 ,column=0)

state_label = Label(root,text="State")
state_label.grid(row=4 ,column=0)

zipcode_label = Label(root,text="zipcode")
zipcode_label.grid(row=5 ,column=0)

#submit button
submit_btn = Button(root,text="Add Record To Database", command =  submit)
submit_btn.grid(row = 6,column=0,columnspan = 2 , pady=10,padx=10,ipadx=100)

show_btn = Button(root,text="Show Record",command = query)
show_btn.grid(row=7,column=0,columnspan = 2,pady=10,padx=10, ipadx=100)
#commit
conn.commit()
#close
conn.close

root.mainloop()