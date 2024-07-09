from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image,ImageTk

root = Tk()
root.title("Billing system")
root.geometry("1400x750")
root.maxsize(1400 ,750)
root.minsize(1400 ,750)
# root.config(bg="light grey")

# ********* entry variable ***********
o1 = IntVar()
o2 = IntVar()
o3 = IntVar()
o4 = IntVar()
o5 = IntVar()
o6 = IntVar()
o7 = IntVar()
o8 = IntVar()
o9 = IntVar()
o10 = IntVar()
o11 = IntVar()
o12 = IntVar()
# second row
o14 = IntVar()
o15 = IntVar()
o16 = IntVar()
o17 = IntVar()
o18 = IntVar()
o19 = IntVar()
o20 = IntVar()
o21 = IntVar()
o22 = IntVar()
o23 = IntVar()
o24 = IntVar()
o25 = IntVar()
# third row
o27 = IntVar()
o28 = IntVar()
o29 = IntVar()
o30 = IntVar()
o31 = IntVar()
o32 = IntVar()
o33 = IntVar()
o13 = IntVar()
o26 = IntVar()
total = IntVar()
# price variable
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()
t9 = StringVar()
t10 = StringVar()
t11 = StringVar()
t12 = StringVar()
t13 = StringVar()
t14 = StringVar()
t15 = StringVar()
t16 = StringVar()
t17 = StringVar()
t18 = StringVar()
t19 = StringVar()
t20 = StringVar()
t21 = StringVar()
t22 = StringVar()
t23 = StringVar()
t24 = StringVar()
t25 = StringVar()
t26 = StringVar()
t27 = StringVar()
t28 = StringVar()
t29 = StringVar()
t30 = StringVar()
t31 = StringVar()
t32 = StringVar()
t33 = StringVar()
total_cost=StringVar()

def Total():
    if (o1.get() == 0 and o2.get() == 0 and o3.get() == 0 and o4.get() == 0 and o5.get() == 0 and o6.get()==0 and
        o7.get()==0 and o8.get()==0 and o9.get()==0 and o10.get()==0 and o11.get()==0 and o12.get()==0 and
        o13.get()==0 and o14.get()==0 and o15.get()==0 and o16.get()==0 and o17.get()==0 and o18.get()==0 and o19.get()==0
        and o20.get()==0 and o21.get()==0 and o22.get()==0 and o23.get()==0 and o24.get()==0 and o25.get()==0 and
         o26.get()==0 and o27.get()==0 and o28.get()==0 and o29.get()==0 and o30.get()==0 and o31.get()==0 and
         o32.get()==0 and o33.get()==0 ):
         messagebox.showerror('Error','Please Select Number of Quantity')
    else:
        a1=o1.get()
        a2=o2.get()
        a3=o3.get()
        a4=o4.get()
        a5=o5.get()
        a6=o6.get()
        a7=o7.get()
        a8=o8.get()
        a9=o9.get()
        a10=o10.get()
        a11=o11.get()
        a12=o12.get()
        a13=o13.get()
        a14=o14.get()
        a15=o15.get()
        a16=o16.get()
        a17=o17.get()
        a18=o18.get()
        a19=o19.get()
        a20=o20.get()
        a21=o21.get()
        a22=o22.get()
        a23=o23.get()
        a24=o24.get()
        a25=o25.get()
        a26=o26.get()
        a27=o27.get()
        a28=o28.get()
        a29=o29.get()
        a30=o30.get()
        a31=o31.get()
        a32=o32.get()
        a33=o33.get()
        totall = (a1*210 +a2*199+a3*230+a4*270+a5*170+a6*300+a7*199+a8*180+a9*150+a10*200+a11*230+a12*240
                  +a13*180+a14*270+a15*250+a16*270+a17*240+a18*270+a19*230+a20*150+a21*160+a22*160+a23*170+a24*170+
                  a25*170+a26*200+a27*200+a28*250+a29*200+a30*250+a31*230+a32*25+a33*30)
        total.set(a1 + a2 + a3 + a4 + a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+
                  a26+a27+a28+a29+a30+a31+a32+a33)
        total_cost.set(str(round(totall, 2)))

        t1.set('₹' + str(round(a1 * 210, 2)))
        t2.set('₹' + str(round(a2 * 199, 2)))
        t3.set('₹' + str(round(a3 * 230, 2)))
        t4.set('₹' + str(round(a4 * 270, 2)))
        t5.set('₹'+str(a5*170))
        t6.set('₹'+str(a6*300))
        t7.set('₹'+str(a7*199))
        t8.set('₹'+str(a8*180))
        t9.set('₹'+str(a9*150))
        t10.set('₹'+str(a10*200))
        t11.set('₹'+str(a11*230))
        t12.set('₹'+str(a12*240))
        t13.set('₹'+str(a13*180))
        t14.set('₹'+str(a14*270))
        t15.set('₹'+str(a15*250))
        t16.set('₹'+str(a16*270))
        t17.set('₹'+str(a17*240))
        t18.set('₹'+str(a18*270))
        t19.set('₹'+str(a19*230))
        t20.set('₹'+str(a20*150))
        t21.set('₹'+str(a21*160))
        t22.set('₹'+str(a22*160))
        t23.set('₹'+str(a23*170))
        t24.set('₹'+str(a24*170))
        t25.set('₹'+str(a25*170))
        t26.set('₹'+str(a26*200))
        t27.set('₹'+str(a27*200))
        t28.set('₹'+str(a28*250))
        t29.set('₹'+str(a29*200))
        t30.set('₹'+str(a30*250))
        t31.set('₹'+str(a31*230))
        t32.set('₹'+str(a32*25))
        t33.set('₹'+str(a33*30))

def receipt():
    txtarea.delete(1.0,END)
    txtarea.insert(END,"\t   ** welcome Customer **")
    txtarea.insert(END, '\n========================================')
    txtarea.insert(END,f'\nCustomer Name :\t{name_entry.get()}')
    txtarea.insert(END,f'\nPhone Number :\t{number_entry.get()}')
    txtarea.insert(END, '\n========================================')
    txtarea.insert(END,"\nNAME\t\t \t       QTY\t     PRICE")
    txtarea.insert(END, '\n--------------------------------------------------------------------------')
    if o1.get() > 0:
         txtarea.insert(END,f'\nPaneer mutter\t\t \t          {o1.get()}\t        {t1.get()}')

    if o2.get() > 0:
         txtarea.insert(END,f'\nPaneer Tikka\t\t \t          {o2.get()}\t        {t2.get()}')

    if o3.get() > 0:
         txtarea.insert(END,f'\nVeg Kolhapuri\t\t \t          {o3.get()}\t        {t3.get()}')

    if o4.get() > 0:
        txtarea.insert(END,f'\nPaneer Handi\t\t \t          {o4.get()}\t        {t4.get()}')

    if o5.get() > 0:
        txtarea.insert(END, f'\nPalak Paneer \t\t \t          {o5.get()}\t        {t5.get()}')

    if o6.get() > 0:
        txtarea.insert(END, f'\nMixed Veg\t\t \t          {o6.get()}\t        {t6.get()}')

    if o7.get() > 0:
        txtarea.insert(END, f'\nDal Makhani\t\t \t          {o7.get()}\t        {t7.get()}')

    if o8.get() > 0:
        txtarea.insert(END, f'\nDal Tadka\t\t \t          {o8.get()}\t        {t8.get()}')

    if o9.get() > 0:
        txtarea.insert(END, f'\nDal Aloo\t\t \t          {o9.get()}\t        {t9.get()}')

    if o10.get() > 0:
        txtarea.insert(END, f'\nKadai Mushroom\t\t \t          {o10.get()}\t        {t10.get()}')

    if o11.get() > 0:
        txtarea.insert(END, f'\nPaneer Shahi\t\t \t          {o11.get()}\t        {t11.get()}')

    if o12.get() > 0:
        txtarea.insert(END, f'\nChana Masala\t\t \t          {o12.get()}\t        {t12.get()}')

    if o13.get() > 0:
        txtarea.insert(END, f'\nAloo Jira Fry\t\t \t          {o13.get()}\t        {t13.get()}')

    if o14.get() > 0:
        txtarea.insert(END, f'\nMutter Mushroom\t\t \t          {o14.get()}\t        {t14.get()}')

    if o15.get() > 0:
        txtarea.insert(END, f'\nPaneer Butter Masala\t\t \t          {o15.get()}\t        {t15.get()}')

    if o16.get() > 0:
        txtarea.insert(END, f'\nKaju Paneer Mutter\t\t \t          {o16.get()}\t        {t16.get()}')

    if o17.get() > 0:
        txtarea.insert(END, f'\nPaneer Shahi Kurma\t\t \t          {o17.get()}\t        {t17.get()}')

    if o18.get() > 0:
        txtarea.insert(END, f'\nPaneer 65 Masala\t\t \t          {o18.get()}\t        {t18.get()}')

    if o19.get() > 0:
        txtarea.insert(END, f'\nButter Chiken\t\t \t          {o19.get()}\t        {t19.get()}')

    if o20.get() > 0:
        txtarea.insert(END, f'\nPlane Rice\t\t \t          {o20.get()}\t        {t20.get()}')

    if o21.get() > 0:
        txtarea.insert(END, f'\nFried Rice\t\t \t          {o21.get()}\t        {t21.get()}')

    if o22.get() > 0:
        txtarea.insert(END, f'\nShezwan Rice\t\t \t          {o22.get()}\t        {t22.get()}')

    if o23.get() > 0:
        txtarea.insert(END, f'\nTriple Shezwan Rice\t\t \t          {o23.get()}\t        {t23.get()}')

    if o24.get() > 0:
        txtarea.insert(END, f'\nVegetable Fried Rice\t\t \t          {o24.get()}\t        {t24.get()}')

    if o25.get() > 0:
        txtarea.insert(END, f'\nGarlic Fried Rice\t\t \t          {o25.get()}\t        {t25.get()}')

    if o26.get() > 0:
        txtarea.insert(END, f'\nChiken Rice\t\t \t          {o26.get()}\t        {t26.get()}')

    if o27.get() > 0:
        txtarea.insert(END, f'\nPaneer Biryani\t\t \t          {o27.get()}\t        {t27.get()}')

    if o28.get() > 0:
        txtarea.insert(END, f'\nChiken Biryani\t\t \t          {o28.get()}\t        {t28.get()}')

    if o29.get() > 0:
        txtarea.insert(END, f'\nMix Biryani\t\t \t          {o29.get()}\t        {t29.get()}')

    if o30.get() > 0:
        txtarea.insert(END, f'\nSpecial Biryani\t\t \t          {o30.get()}\t        {t30.get()}')

    if o31.get() > 0:
        txtarea.insert(END, f'\nMutton Birayni\t\t \t          {o31.get()}\t        {t31.get()}')

    if o32.get() > 0:
        txtarea.insert(END,f'\nRoti\t\t \t          {o32.get()}\t        {t32.get()}')

    if o33.get() > 0:
        txtarea.insert(END,f'\nButter Roti\t\t \t          {o33.get()}\t        {t33.get()}')

    txtarea.insert(END, '\n\n========================================')
    txtarea.insert(END, f'\nTotal Price\t\t\t          {total.get()}\t        {total_cost.get()}')
    txtarea.insert(END, '\n=============================================')
    txtarea.insert(END, '\n=============================================')

def clear():
    txtarea.delete(1.0, END)
    o1.set(0)
    o2.set(0)
    o3.set(0)
    o4.set(0)
    o5.set(0)
    o6.set(0)
    o7.set(0)
    o8.set(0)
    o9.set(0)
    o10.set(0)
    o11.set(0)
    o12.set(0)
    o13.set(0)
    o14.set(0)
    o15.set(0)
    o16.set(0)
    o17.set(0)
    o18.set(0)
    o19.set(0)
    o20.set(0)
    o21.set(0)
    o22.set(0)
    o23.set(0)
    o24.set(0)
    o25.set(0)
    o26.set(0)
    o27.set(0)
    o28.set(0)
    o29.set(0)
    o30.set(0)
    o31.set(0)
    o32.set(0)
    o33.set(0)
    total.set(0)
    t1.set('')
    t2.set('')
    t3.set('')
    t4.set('')
    t5.set('')
    t6.set('')
    t7.set('')
    t8.set('')
    t9.set('')
    t10.set('')
    t11.set('')
    t12.set('')
    t13.set('')
    t14.set('')
    t15.set('')
    t16.set('')
    t17.set('')
    t18.set('')
    t19.set('')
    t20.set('')
    t21.set('')
    t22.set('')
    t23.set('')
    t24.set('')
    t25.set('')
    t26.set('')
    t27.set('')
    t28.set('')
    t29.set('')
    t30.set('')
    t31.set('')
    t32.set('')
    t33.set('')
    total_cost.set('')
def back():
    root.destroy()
    import main

bill_lbl = Label(root,text="BILLING SYSTEM",bd=7,relief=GROOVE,font="times 18 bold",bg="black",fg="yellow",width=99)
bill_lbl.place(x=0,y=0,height=55)
# ********* customer details ************
frm1 = LabelFrame(root,text="Customer details",fg="yellow",font="castellar 12 bold",width=1399,bd=5,relief=RIDGE,bg="black")
frm1.place(x=0,y=59,height=90)

lbl1 = Label(frm1,text="Name",font="Times 20 bold",bg="black",fg="white")
lbl1.place(x=30,y=9)

name_entry = Entry(frm1,font="bookman 12 bold",width=25,bd=5,relief=SUNKEN)
name_entry.place(x=120,y=10,height=35)

lbl2 = Label(frm1,text="Phone Number",font="times 20 bold",bg="black",fg="white")
lbl2.place(x=450,y=9)

number_entry = Entry(frm1,font="bookman 12 bold",width=25,bd=5,relief=SUNKEN)
number_entry.place(x=670,y=10,height=35)

frm2 = LabelFrame(root,text="Item details",font="times 15 bold",bg="black",fg="yellow",width=900,bd=5,relief=RIDGE)
frm2.place(x=0,y=158,height=485)



# *** heading labels ***
nlbl1 = Label(frm2,text="NAME",font="Arial 12 bold",bg="black",fg="yellow").place(x=30,y=2)
nlbl2 = Label(frm2,text="QTY",font="Arial 12 bold",bg="black",fg="yellow").place(x=170,y=2)
nlbl3 = Label(frm2,text="PRICE",font="Arial 12 bold",bg="black",fg="yellow").place(x=235,y=2)
nlbl4 = Label(frm2,text="NAME",font="Arial 12 bold",bg="black",fg="yellow").place(x=335,y=2)
nlbl5 = Label(frm2,text="QTY",font="Arial 12 bold",bg="black",fg="yellow").place(x=490,y=2)
nlbl6 = Label(frm2,text="PRICE",font="Arial 12 bold",bg="black",fg="yellow").place(x=550,y=2)
nlbl7 = Label(frm2,text="NAME",font="Arial 12 bold",bg="black",fg="yellow").place(x=650,y=2)
nlbl8 = Label(frm2,text="QTY",font="Arial 12 bold",bg="black",fg="yellow").place(x=760,y=2)
nlbl9 = Label(frm2,text="PRICE",font="Arial 12 bold",bg="black",fg="yellow").place(x=825,y=2)
# *** first row labels
Ilbl1 = Label(frm2,text="Paneer Mutter",bg="black",fg="white",font="Arial 12 bold").place(x=5,y=25)
Ilbl2 = Label(frm2,text="Paneer Tikka",bg="black",fg="white",font="Arial 12 bold").place(x=5,y=60)
Ilbl3 = Label(frm2,text="Veg Kholapuri",bg="black",fg="white",font="Arial 12 bold").place(x=5,y=95)
Ilbl4 = Label(frm2,text="Paneer Handi",bg="black",fg="white",font="Arial 12 bold").place(x=5,y=130)
Ilbl5 = Label(frm2,text="Palak Paneer",bg="black",fg="white",font="Arial 12 bold").place(x=5,y=165)
Ilbl6 = Label(frm2,text="Mixed Veg",bg="black",fg="white",font="Arial 12 bold").place(x=5,y=200)
Ilbl7 = Label(frm2,text="Dal Makhani",bg="black",fg="white",font="Arial 12 bold").place(x=5,y=235)
Ilbl8 = Label(frm2,text="Dal Tadka",bg="black",fg="white",font="Arial 12 bold").place(x=5,y=270)
Ilbl9 = Label(frm2,text="Dal Aloo",bg="black",fg="white",font="Arial 12 bold").place(x=5,y=305)
Ilbl10 = Label(frm2,text="Kadai Mushroom",bg="black",fg="white",font="Arial 12 bold").place(x=5,y=340)
Ilbl11= Label(frm2,text="Paneer Shahi",bg="black",fg="white",font="Arial 12 bold").place(x=5,y=375)
Ilbl12 = Label(frm2,text="Chana Masala",bg="black",fg="white",font="Arial 12 bold").place(x=5,y=410)

# first row entry
Elbl1 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o1).place(x=160,y=25)
Elbl2 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o2).place(x=160,y=60)
Elbl3 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o3).place(x=160,y=95)
Elbl4 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o4).place(x=160,y=130)
Elbl5 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o5).place(x=160,y=165)
Elbl6 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o6).place(x=160,y=200)
Elbl7 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o7).place(x=160,y=235)
Elbl8 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o8).place(x=160,y=270)
Elbl9 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o9).place(x=160,y=305)
Elbl10 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o10).place(x=160,y=340)
Elbl11 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o11).place(x=160,y=375)
Elbl12 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o12).place(x=160,y=410)

# FIRST ROW PRICE
p1 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t1).place(x=235,y=25)
p2 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t2).place(x=235,y=60)
p3 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t3).place(x=235,y=95)
p4 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t4).place(x=235,y=130)
p5 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t5).place(x=235,y=165)
p6 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t6).place(x=235,y=200)
p7 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t7).place(x=235,y=235)
p8 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t8).place(x=235,y=270)
p9 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t9).place(x=235,y=305)
p10 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t10).place(x=235,y=340)
p11 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t11).place(x=235,y=375)
p12 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t12).place(x=235,y=410)

# second row labels
Ilbl14 = Label(frm2,text="Mutter Mushroom",bg="black",fg="white",font="Arial 12 bold").place(x=300,y=25)
Ilbl15 = Label(frm2,text="Paneer Butter Masala",bg="black",fg="white",font="Arial 12 bold").place(x=300,y=60)
Ilbl16 = Label(frm2,text="Kaju Paneer Mutter",bg="black",fg="white",font="Arial 12 bold").place(x=300,y=95)
Ilbl17 = Label(frm2,text="Paneer Shahi Kurma",bg="black",fg="white",font="Arial 12 bold").place(x=300,y=130)
Ilbl18 = Label(frm2,text="Paneer 65 Masala",bg="black",fg="white",font="Arial 12 bold").place(x=300,y=165)
Ilbl19 = Label(frm2,text="Butter Chiken",bg="black",fg="white",font="Arial 12 bold").place(x=300,y=200)
Ilbl20 = Label(frm2,text="Plane Rice",bg="black",fg="white",font="Arial 12 bold").place(x=300,y=235)
Ilbl21 = Label(frm2,text="Fried Rice",bg="black",fg="white",font="Arial 12 bold").place(x=300,y=270)
Ilbl22 = Label(frm2,text="Shezwan Rice",bg="black",fg="white",font="Arial 12 bold").place(x=300,y=305)
Ilbl23 = Label(frm2,text="Triple Shezwan Rice",bg="black",fg="white",font="Arial 12 bold").place(x=300,y=340)
Ilbl24 = Label(frm2,text="Vegetable Fried Rice",bg="black",fg="white",font="Arial 12 bold").place(x=300,y=375)
Ilbl25 = Label(frm2,text="Garlic Fried Rice",bg="black",fg="white",font="Arial 12 bold").place(x=300,y=410)

# second row quantity
Elbl14 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o14).place(x=480,y=25)
Elbl15 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o15).place(x=480,y=60)
Elbl16 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o16).place(x=480,y=95)
Elbl17 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o17).place(x=480,y=130)
Elbl18 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o18).place(x=480,y=165)
Elbl19 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o19).place(x=480,y=200)
Elbl20 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o20).place(x=480,y=235)
Elbl21 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o21).place(x=480,y=270)
Elbl22 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o22).place(x=480,y=305)
Elbl23 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o23).place(x=480,y=340)
Elbl24 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o24).place(x=480,y=375)
Elbl25 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o25).place(x=480,y=410)

# second row price
p14 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t14).place(x=552,y=25)
p15 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t15).place(x=552,y=60)
p16 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t16).place(x=552,y=95)
p17 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t17).place(x=552,y=130)
p18 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t18).place(x=552,y=165)
p19 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t19).place(x=552,y=200)
p20 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t20).place(x=552,y=235)
p21 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t21).place(x=552,y=270)
p22 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t22).place(x=552,y=305)
p23 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t23).place(x=552,y=340)
p24 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t24).place(x=552,y=375)
p25 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t25).place(x=552,y=410)
# Third row lables
Ilbl27 = Label(frm2,text="Paneer Biryani",bg="black",fg="white",font="Arial 12 bold").place(x=615,y=25)
Ilbl28 = Label(frm2,text="Chiken Biryani",bg="black",fg="white",font="Arial 12 bold").place(x=615,y=60)
Ilbl29 = Label(frm2,text="Mix Biryani",bg="black",fg="white",font="Arial 12 bold").place(x=615,y=95)
Ilbl30 = Label(frm2,text="Special Biryani",bg="black",fg="white",font="Arial 12 bold").place(x=615,y=130)
Ilbl31 = Label(frm2,text="Mutton Birayni",bg="black",fg="white",font="Arial 12 bold").place(x=615,y=165)
Ilbl32 = Label(frm2,text="Roti",bg="black",fg="white",font="Arial 12 bold").place(x=615,y=200)
Ilbl33 = Label(frm2,text="Butter Roti",bg="black",fg="white",font="Arial 12 bold").place(x=615,y=235)
Ilbl13 = Label(frm2,text="Aloo Jira Fry",bg="black",fg="white",font="Arial 12 bold").place(x=615,y=270)
Ilbl26 = Label(frm2,text="Chiken Rice",bg="black",fg="white",font="Arial 12 bold").place(x=615,y=305)


# Third Row quantity
Elbl27 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o27).place(x=750,y=25)
Elbl28 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o28).place(x=750,y=60)
Elbl29 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o29).place(x=750,y=95)
Elbl30 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o30).place(x=750,y=130)
Elbl31 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o31).place(x=750,y=165)
Elbl32 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o32).place(x=750,y=200)
Elbl33 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o33).place(x=750,y=235)
Elbl13 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o13).place(x=750,y=270)
Elbl26 = Entry(frm2,width=6,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=o26).place(x=750,y=305)

# third row price
p27 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t27).place(x=825,y=25)
p28 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t28).place(x=825,y=60)
p29 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t29).place(x=825,y=95)
p30 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t30).place(x=825,y=130)
p31 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t31).place(x=825,y=165)
p32 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t32).place(x=825,y=200)
p33 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t33).place(x=825,y=235)
p13 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t13).place(x=825,y=270)
p26 = Entry(frm2,width=5,font="Arial 12 bold",bd=3,relief=SUNKEN,textvariable=t26).place(x=825,y=305)

# total info
totalqu= Label(frm2,text="TOTAL-QTY",font="Arial 12 bold",bg="black",fg="yellow").place(x=620,y=360)
qe= Entry(frm2,width=10,bd=5,relief=RAISED,font="Arial 12 bold",textvariable=total).place(x=750,y=355)
totalprice= Label(frm2,text="TOTAL-PRICE",font="Arial 12 bold",bg="black",fg="yellow").place(x=620,y=400)
pe= Entry(frm2,width=10,bd=5,relief=RAISED,font="Arial 12 bold",textvariable=total_cost).place(x=750,y=400)
# Buttons Frame
frm3 = Frame(root,width=900,bg="black",bd=5,relief=GROOVE)
frm3.place(x=0,y=647,height=100)

blbl1 = Label(frm3,bg="white",width=122,bd=8,relief=GROOVE)
blbl1.place(x=10,y=10,height=70)

totalbtn = Button(frm3,text="Total",bd=3,relief=RAISED,bg="black",fg="blue",font="Arial 15 bold",width=10,command=Total)
totalbtn.place(x=250,y=21)

back = Button(frm3,text="BACK",width=10,bg="black",fg="blue",font="Arial 15 bold",bd=3,relief=RAISED,command=back)
back.place(x=50,y=21,height=45)

clearbtn = Button(frm3,text="Clear",bd=3,relief=RAISED,bg="black",fg="blue",font="Arial 15 bold",width=10,command=clear)
clearbtn.place(x=700,y=21)

receiptbtn = Button(frm3,text="Receipt",bd=3,relief=RAISED,bg="black",fg="blue",font="Arial 15 bold",width=10,command=receipt)
receiptbtn.place(x=480,y=21)

# receipt Frame
frm4 = Frame(root,width=485,height=580,bg="white",bd=7,relief=GROOVE)
frm4.place(x=910,y=158)

rlbl1 = Label(frm4,text="Bill Area",bg="light grey",bd=5,relief=RIDGE,font="times 15 bold",width=38)
rlbl1.place(x=0,y=0,height=40)
txtarea=Text(frm4,font=('Calisto,15,bold'))
txtarea.place(x=0,y=40)

scrollbar =Scrollbar(frm4,orient=VERTICAL,command=txtarea.yview)
txtarea.configure(yscrollcommand=scrollbar.set)
scrollbar.place(x=460,y=43,height=520)
root.mainloop()
