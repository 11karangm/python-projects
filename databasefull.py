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

def delete():
    conn = sqlite3.connect('adress_book.db')
    c = conn.cursor()#create cursor

    c.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())    

    conn.commit()
    #close
    conn.close

def editor():
    conn = sqlite3.connect('adress_book.db')
    c = conn.cursor()#create cursor
    record_id=delete_box.get()
    
    c.execute("""UPDATE addresses SET
        f_name= :first,
        l_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
        'first':f_name_e.get(),
        'last': l_name_e.get(),
        'address': address_e.get(),
        'city': city_e.get(),
        'state': state_e.get(),
        'zipcode': zipcode_e.get(),
        'oid':record_id

        })


    edit.destroy()
    conn.commit()
    #close
    conn.close

def update():
    global edit
    edit = Tk()
    edit.title("3")
    edit.geometry("400x400")
    conn = sqlite3.connect('adress_book.db')
    global f_name_e
    global l_name_e
    global address_e
    global city_e
    global state_e
    global zipcode_e

    f_name_e = Entry(edit,width = 35)
    f_name_e.grid(row=0,column=1,padx =20)

    l_name_e = Entry(edit,width = 35)
    l_name_e.grid(row=1,column=1,padx =20)

    address_e = Entry(edit,width = 35)
    address_e.grid(row=2,column=1,padx =20)

    city_e = Entry(edit,width = 35)
    city_e.grid(row=3,column=1,padx =20)

    state_e = Entry(edit,width = 35)
    state_e.grid(row=4,column=1,padx =20)

    zipcode_e = Entry(edit,width = 35)
    zipcode_e.grid(row=5,column=1,padx =20)

#create text box labels
    f_name_label = Label(edit,text="First Name")
    f_name_label.grid(row=0 ,column=0)

    l_name_label = Label(edit,text="Last Name")
    l_name_label.grid(row=1 ,column=0)

    address_label = Label(edit,text="Address")
    address_label.grid(row=2 ,column=0)

    city_label = Label(edit,text="City")
    city_label.grid(row=3 ,column=0)

    state_label = Label(edit,text="State")
    state_label.grid(row=4 ,column=0)

    zipcode_label = Label(edit,text="zipcode")
    zipcode_label.grid(row=5 ,column=0)

    

    Save_button = Button(edit,text="Save",command=editor)
    Save_button.grid(row = 6,column=0,columnspan = 2 , pady=10,padx=10,ipadx=100)
    
    c = conn.cursor()#create cursor

    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses where oid = "+ record_id)
    records = c.fetchall()

     #Loop through results
    for record in records:
        f_name_e.insert(0,record[0])
        l_name_e.insert(0,record[1])
        address_e.insert(0,record[2])
        city_e.insert(0,record[3])
        state_e.insert(0,record[4])
        zipcode_e.insert(0,record[5])

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

delete_box = Entry(root,width=30)
delete_box.grid(row=9,column=1)

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

delete_box1 = Label(root,text="Select ID")
delete_box1.grid(row=9,column=0)

#submit button
submit_btn = Button(root,text="Add Record To Database", command =  submit)
submit_btn.grid(row = 6,column=0,columnspan = 2 , pady=10,padx=10,ipadx=100)

show_btn = Button(root,text="Show Record",command = query)
show_btn.grid(row=7,column=0,columnspan = 2,pady=10,padx=10, ipadx=100)

delete_button= Button(root,text="Delete",command=delete)
delete_button.grid(row=10,column=0,columnspan=2,pady=10,padx=12,ipadx=137)

edit_button= Button(root,text = "Edit Record",command = update)
edit_button.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
#commit
conn.commit()
#close
conn.close

root.mainloop()