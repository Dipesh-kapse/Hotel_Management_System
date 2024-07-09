import tkinter.ttk
from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
def connect():
    cur = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dipesh@143",
        database="hotel_management"
    )
    return cur
def insert_menu():
    # Clear previous data
    tree.delete(*tree.get_children())
    conn = connect()
    c = conn.cursor()
    c.execute("select * from menu_card")
    res = c.fetchall()
    for i in res:
        tree.insert('', 'end', values=i)
    conn.commit()
    conn.close()

def show_entry():
    selected_item = tree.focus()
    values = tree.item(selected_item, 'values')
    if values:
        oentry1.delete(0, END)
        oentry2.delete(0, END)
        oentry1.insert(0, values[0])
        oentry2.insert(0, values[1])
def clear_entry():
    oentry1.delete(0,END)
    oentry2.delete(0,END)
    oentry3.delete(0,END)
def Add_item():
    con = connect()
    cur = con.cursor()
    name = oentry1.get()
    rate = oentry2.get()
    quantity = oentry3.get()

    cur.execute(
        "insert into orderr values('" + name + "' , " + rate + ", " + quantity + ")")
    con.commit()
    con.close()
    treee.insert('', "end", values=(name, rate, quantity))
    messagebox.showinfo('Success', 'Record Added Successfully')
    oentry1.delete(0, END)
    oentry2.delete(0, END)
    oentry3.delete(0, END)

def bill():
    root.destroy()
    import Bill

def update():
    conn = connect()
    c = conn.cursor()
    name = oentry1.get()
    rate = oentry2.get()
    quantity = oentry3.get()

    query = ("update orderr set rate = '%s',quantity ='%s' where name = '%s' " % (rate,quantity,name))
    c.execute(query)
    conn.commit()

    selected_item = treee.selection()
    if len(selected_item) == 1:  # Ensure only one item is selected
        item = selected_item[0]
        # Update the values in the selected item
        treee.item(item, values=(f"{name}", f"{rate}", f"{quantity}"))
    messagebox.showinfo("Info", "Selected Record Updated Successfully")
def delete_record():
    conn = connect()
    c = conn.cursor()
    select_del = treee.focus()
    if select_del:
        values = treee.item(select_del,'values')
        # id_to_delete= values[0]
        # delete in database
        query = f"delete from orderr where name = %s"
        c.execute(query,(values[0],))
        conn.commit()
        # delete in treeview
        treee.delete(select_del)
    messagebox.showinfo("Information", "The record is deleted.....")

def show():
    # Clear previous data
    treee.delete(*treee.get_children())
    conn = connect()
    c = conn.cursor()
    c.execute("select * from orderr")
    res = c.fetchall()
    for i in res:
        treee.insert('','end',values=i)
    conn.commit()
    conn.close()

def show_selected_row(event):
    selected_item = treee.focus()
    values = treee.item(selected_item, 'values')
    if values:
        oentry1.delete(0, END)
        oentry2.delete(0, END)
        oentry3.delete(0, END)
        oentry1.insert(0, values[0])
        oentry2.insert(0, values[1])
        oentry3.insert(0, values[2])

root = Tk()
root.geometry("1500x750")
root.maxsize(1450,750)
root.minsize(1450,750)
root.title("HOTEL MANAGEMENT PROJECT")
#*****  hotel management frame one ********
hotel_frame = Frame(root,width=1450,height=50,bd=3,bg="teal",relief=SOLID,)
hotel_frame.place(x=0,y=0)
hotel= Label(root,text="HOTEL MANAGEMENT SYSTEM",fg="white",bg="teal",font="Arial 20 bold")
hotel.place(x=500,y=5)

# ******** frame two *********
frm1 = Frame(root,width=1450,height=60,bg="silver",bd=5,relief=GROOVE)
frm1.place(x=0,y=50)
lbl1= Label(frm1,text="Enter Customer Details -->  Name :-",bg="silver",font="'' 18 bold")
lbl1.place(x=5,y=7)

entry_1= Entry(frm1,width=40,bd=5,relief=RAISED,font="'' 10 bold")
entry_1.place(x=420,y=7,height=35)

lbl2 = Label(frm1,text="Contact :-",bg="silver",font="'' 18 bold")
lbl2.place(x=770,y=7)
entry_2 = Entry(frm1,width=30,bd=5,relief=RAISED,font="'' 10 bold")
entry_2.place(x=900,y=7,height=35)

# ********* exit button *********
exit_btn = Button(frm1,text="EXIT",bd=3,font="'' 13 bold",width=15,bg="red",command=exit)
exit_btn.place(x=1230,y=5)

# ********** menu card frame **********
menu_frame = Frame(root,width=700,height=644,bg="darkslategrey",bd=8,relief=RAISED)
menu_frame.place(x=0,y=108)
mlbl1 = Label(menu_frame,text="HOTEL MENU",font="times 20 bold",width=42,bd=3,relief=RAISED,bg="teal",fg="white")
mlbl1.place(x=0,y=0,height=50)

# ********* insert menu **********
menu_btn = Button(menu_frame,text="Show Menu",width=10,bg="red",bd=3,font="Arial 12 bold",relief=RAISED,command=insert_menu)
menu_btn.place(x=560,y=6)

# ********** dish order ************
orderdish_btn = Button(menu_frame,text="Select",width=8,bg="red",bd=3,font="Arial 12 bold",relief=RAISED,command=show_entry)
orderdish_btn.place(x=460,y=6)
# ********* menu_treeview ************
column = ("name","price")
tree = ttk.Treeview(menu_frame,columns=column,show="headings")
tree.heading("name",text="DISH NAME",anchor=CENTER)
tree.heading('price',text="PRICE",anchor=CENTER)
tree.place(x=0,y=50,width=679,height=600)
tree.column('price',anchor=CENTER)


# ********** scrollbar *******
scrollbar = ttk.Scrollbar(menu_frame,orient=VERTICAL,command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.place(x=660,y=50,height=570)
# ********** order item ************
order_frame = Frame(root,width=750,height=230,bg="darkslategray4",bd=8,relief=RAISED)
order_frame.place(x=700,y=109)

ofrm1 = Label(order_frame,text="ORDER-ITEM",font="Times 20 bold",bg="cyan4",fg="white",relief=RAISED,width=46)
ofrm1.place(x=0,y=0,height=50)

ofram2 = Label(order_frame,text="Name :-",font="Arial 15 bold",bg="darkslategray4")
ofram2.place(x=15,y=60)

oentry1 = Entry(order_frame,width=58,relief=RAISED,bd=5,font="'' 10 bold")
oentry1.place(x=110,y=60,height=30)

ofram3 = Label(order_frame,text="Rate :-",font="Arial 15 bold",bg="darkslategray4")
ofram3.place(x=530,y=60)

oentry2 = Entry(order_frame,width=12,relief=RAISED,bd=5,font="'' 10 bold")
oentry2.place(x=610,y=60,height=30)

ofram4 = Label(order_frame,text="Quantity :-",font="Arial 15 bold",bg="darkslategray4")
ofram4.place(x=190,y=100)

oentry3 = Entry(order_frame,width=12,relief=RAISED,bd=5,font="'' 10 bold")
oentry3.place(x=300,y=100,height=30)

# ****** buttons ******
addbtn = Button(order_frame,text="Add Item",bd=5,relief=RAISED,font="Arial 12 bold",bg="blue",width=10,command=Add_item)
addbtn.place(x=30,y=150)

updatebtn = Button(order_frame,text="Update Item",bd=5,relief=RAISED,font="Arial 12 bold",bg="blue",width=10,command=update)
updatebtn.place(x=200,y=150)

deletebtn = Button(order_frame,text="Delete Item",bd=5,relief=RAISED,font="Arial 12 bold",bg="blue",width=10,command=delete_record)
deletebtn.place(x=380,y=150)

clearbtn = Button(order_frame,text="Clear",bd=5,relief=RAISED,font="Arial 12 bold",bg="blue",width=10,command=clear_entry)
clearbtn.place(x=560,y=150)

# ************ your order *********
your_order_frm = Frame(root,width=746,height=408,bg="light blue",bd=8,relief=RAISED)
your_order_frm.place(x=700,y=340)

yolbl1 = Label(your_order_frm,text="Your Order",bg="darksalmon",fg="black",font="times 18 bold")
yolbl1.place(x=0,y=0,width=730,height=35)

# second treeview
column= ("name","rate","quantity")
treee = ttk.Treeview(your_order_frm,columns=column,show="headings")
treee.heading("name",text="DISH NAME",anchor=CENTER)
treee.heading('rate',text="RATE",anchor=CENTER)
treee.heading('quantity',text="QUANTITY",anchor=CENTER)
treee.place(x=0,y=38,width=730,height=270)
treee.bind("<<TreeviewSelect>>",show_selected_row)
# treee.column('',anchor=CENTER)
treee.column('rate',anchor=CENTER)
treee.column('quantity',anchor=CENTER)

# second scrollbar
scrollbar = ttk.Scrollbar(your_order_frm,orient=VERTICAL,command=treee.yview)
treee.configure(yscrollcommand=scrollbar.set)
scrollbar.place(x=710,y=40,height=260)

yolbl2 = Label(your_order_frm,bg="darksalmon",fg="white")
yolbl2.place(x=0,y=308,width=730,height=83)

# **** total price button ****
# your_order_btn = Button(your_order_frm,text="Total price",bg="silver",bd=5,relief=RAISED,font="Arial 12 bold",width=10)
# your_order_btn.place(x=20,y=326,height=45)

# your_order_entry = Entry(your_order_frm,width=15,bd=8,relief=RAISED)
# your_order_entry.place(x=150,y=326,height=45)

# *** bill button ***
billbtn = Button(your_order_frm,text="BILL",bg="silver",bd=5,relief=RAISED,font="Arial 12 bold",width=8,command=bill)
billbtn.place(x=100,y=326,height=45)

# **** cancel order button ****
# cancelbtn = Button(your_order_frm,text="Cancel order",bg="silver",bd=5,relief=RAISED,font="Arial 12 bold",width=10)
# cancelbtn.place(x=380,y=326,height=45)

# **** show button *****
# billbtn = Button(your_order_frm,text="Show",bg="silver",bd=5,relief=RAISED,font="Arial 12 bold",width=8)
# billbtn.place(x=510,y=326,height=45)

# **** show all ****
billbtn = Button(your_order_frm,text="Show All",bg="silver",bd=5,relief=RAISED,font="Arial 12 bold",width=8,command=show)
billbtn.place(x=520,y=326,height=45)

root.mainloop()