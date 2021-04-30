import sys
import os
from sqlite3 import *
conn = connect('stock_mng.db')
mycursor = conn.cursor()

from tkcalendar import DateEntry
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as tt
import datetime as dt
from tkinter import filedialog
from tabulate import tabulate
from fpdf import FPDF

root=tk.Tk()
root.geometry("500x500")
root.title("STOCK UP: Log In")
root.iconbitmap(r"dc.ico")

mycursor.execute("create table IF NOT EXISTS supplier(name text, pname text,cnum int, date1 date, mop text, sadd text, sp text)")
mycursor.execute("create table IF NOT EXISTS stock(srno int, pname2 text,quantity int, measure text, pi int)")
mycursor.execute("create table IF NOT EXISTS purchase(pname3 text,Quantity int,Measurement text, Price int, name2 text , date2 date, City text)")
mycursor.execute("create table IF NOT EXISTS sale(ino int,dob date, pname5 text,Quantity2 int,Measurement2 text, rate1 int , discount1 int, Price2 int)")
mycursor.execute("create table IF NOT EXISTS sale2(ino1 int, cname text,cadd text,dob1 date, nop int , tq int, td int ,ta int)")
mycursor.execute("create table IF NOT EXISTS sale3(pname4 text,Quantity1 int,Measurement1 text, rate int , discount int, Price1 int)")

 
skframe,listBox,name1, pname1,cnum1, date2, sadd1, mop1, sp1,name, pname,cnum, date1, sadd, mop, sp,r,option = None,None,None, None, None, None, None,None,None,None, None, None, None, None, None, None , None , None        
srno, pname2,quantity, measure, pi,listBox1,option1,r1,skframe1=None,None,None,None,None,None,None,None,None
listBox2,option2,r2,skframe2,pname3,Quantity,Measurement,Price,name2,date2,City,listBox3,option3,r3,skframe3 =None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
listBox4,listBox5,r6,skframe5,r7,pname4,Quantity1,Measurement1,rate,discount,r9,r10,r12,r11,z,r4,r5=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
cframe=tk.Frame(root)
cframe.pack(pady=120)

def call1():
    global t2
    t2=tk.Entry(cframe,show='')
    t2.grid(row=3,columnspan=2)

l1=tk.Label(cframe,text="User",font=("arial",10,"bold"))
l2=tk.Label(cframe,text="Password",font=("arial",10,"bold"))
l3=tk.Label(cframe,text="Option",font=("arial",10,"bold"))
p=tk.StringVar()
t1=tk.Entry(cframe,textvariable=p)
v=tk.StringVar()
t2=tk.Entry(cframe,show='*')
v=["Purchase","Sales"]
c1= tt.Combobox(cframe,value=v,width=15,state='readonly')
c1.set("Select")
l1.grid(row=0,columnspan=2)
t1.grid(row=1,columnspan=2)
l2.grid(row=2,columnspan=2)
t2.grid(row=3,columnspan=2)
l3.grid(row=4,columnspan=2)
c1.grid(pady=10,row=5,columnspan=2)

b1=tk.Button(cframe,text="SHOW",padx=15,pady=5,bd=4,font=("arial",10,"bold"),command=lambda:call1())
b1.grid(row=6,column=1)

Mp = tk.Toplevel(root)
Mp.title("STOCK UP: Manage Purchase")
Ms = tk.Toplevel(root)
Ms.title("STOCK UP: Manage Suppliers")
Ip = tk.Toplevel(root)
Ip.title("STOCK UP: Manage Product")
Sa = tk.Toplevel(root)
Sa.title("STOCK UP: Manage Sales")

def Open():
    x= t1.get()
    y= t2.get()
    z= c1.get()
    if x=="admin" and y=="jain" and z=="Purchase":
        root.withdraw()
        toplevel1(Mp)
    elif x=="admin" and y=="jain" and z=="Sales":
        root.withdraw()
        toplevel5(Sa)
    else:
        pass
    
def clear():
    name.set("")
    pname.set("")
    cnum.set("")
    sadd.set("")
    mop.set("")
    sp.set("")

def clear1():
    srno.set("")
    pname2.set("")
    quantity.set("")
    measure.set("")
    pi.set("")

def clear2():
    pname3.set("Choose the product Properly!")
    Quantity.set("")
    Measurement.set("Choose the Measurement Properly!") 
    Price.set("")
    City.set("")
    name2.set("")
    

def clear3():
    pname4.set("Choose the product Properly!")
    Quantity1.set("")
    Measurement1.set("Choose the Measurement Properly!")
    rate.set("")
    discount.set("")

def clear4():
    r7.set("")
    r9.set("")
    r10.set("")
    r12.set("")
    r11.set("")
    
def menue(t):
    global listBox2,listBox3
    def onclosing():
        mycursor.execute("Drop table if exists sale3")
        Mp.destroy()
        Ms.destroy()
        Ip.destroy()
        Sa.destroy()
        root.destroy()
    def cleardatabase():
        mycursor.execute("Drop table if exists purchase")
        mycursor.execute("Drop table if exists sale")
        mycursor.execute("Drop table if exists sale2")
        mycursor.execute("create table IF NOT EXISTS purchase(pname3 text,Quantity int,Measurement text, Price int, name2 text , date2 date, City text)")
        mycursor.execute("create table IF NOT EXISTS sale(ino int,dob date, pname5 text,Quantity2 int,Measurement2 text, rate1 int , discount1 int, Price2 int)")
        mycursor.execute("create table IF NOT EXISTS sale2(ino1 int, cname text,cadd text,dob1 date, nop int , tq int, td int ,ta int)")
        try:
            listBox2.delete(*listBox2.get_children())
            listBox3.delete(*listBox3.get_children())
        except:
            pass
    if t==Ms:        
        Mp.withdraw()
        Ip.withdraw()
        Sa.withdraw()
    elif t==Mp:
        Ms.withdraw()
        Ip.withdraw()
        Sa.withdraw()
    elif t==Sa:
        Mp.withdraw()
        Ip.withdraw()
        Ms.withdraw()
    else:
        Mp.withdraw()
        Ms.withdraw()
        Sa.withdraw()
    t.deiconify()
    t.iconbitmap(r"dc.ico")
    x, y = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (x, y))
    
    t.resizable(1, 1)
    #Menue Bar
    menubar=tk.Menu(t)
    t.config(menu=menubar)
    #Sub Menue
    submenu=tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=submenu)
    submenu.add_command(label="Clear Database",command=cleardatabase)
    submenu.add_command(label="Exit",command=onclosing)

    submenu=tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=submenu)
    submenu.add_command(label="Manage Purchase",command=lambda:toplevel1(Mp))
    submenu.add_command(label="Manage Suppliers",command=lambda:toplevel2(Ms))
    submenu.add_command(label="Manage Product",command=lambda:toplevel4(Ip))
    submenu.add_command(label="Manage Sales",command=lambda:toplevel5(Sa))
    def aboutus():
        messagebox.showinfo("About Inventery Management","This is a Stock Management Software.\nCreated By Samarpan Jain using Python")

    submenu=tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=submenu)
    submenu.add_command(label="About Us",command=aboutus)

    t.protocol("WM_DELETE_WINDOW",onclosing)

def toplevel2(top):
    global listBox,option,r
    def onclosing():
        clear()
        Ad.withdraw()
    def onclosings():
        Md.withdraw()
    Ad = tk.Toplevel(Ms)
    Ad.title("STOCK UP: ADD ENTRY")
    Ad.withdraw()
    Ad.protocol("WM_DELETE_WINDOW",onclosing)
    Md = tk.Toplevel(Ms)
    Md.title("STOCK UP: MODIFY ENTRY")
    Md.withdraw()
    Md.protocol("WM_DELETE_WINDOW",onclosings)
    menue(top)
    
    l4=tk.Label(top,text="Suppliers Detail and Management",font=("arial",25,"bold"))
    l4.place(relx=0.385, rely=0.019, height=79, width=525)
    
    
    l5=tk.Label(top,text="Type:",font=("arial",20,"bold"))
    l5.place(relx=0.001, rely=0.125, height=40, relwidth=0.341)
    
    r=tk.StringVar()
    Entry1=tk.Entry(top,width=40,textvariable=r)
    Entry1.place(relx=0.209, rely=0.125, height=40, relwidth=0.241)
    Entry1.configure(background="white")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="-family {Palatino Linotype} -size 15")
    Entry1.configure(foreground="#000000")
    Entry1.configure(highlightbackground="#d9d9d9")
    Entry1.configure(highlightcolor="black")
    Entry1.configure(insertbackground="black")
    Entry1.configure(selectbackground="#c4c4c4")
    Entry1.configure(selectforeground="black")

    option = tk.StringVar()
    v=['All Records','Supplier Name', 'Product Name' ,'Contact Number','Date of becoming Supplier','Mode of Payment','Address','Problem']
    c2= tt.Combobox(top,value=v,width=35,textvariable=option,state='readonly')
    c2.set("Choose Category to Search")
    c2.place(relx=0.568, rely=0.114, relheight=0.069, relwidth=0.269)
    c2.configure(font="-family {Palatino Linotype} -size 14")
    cols = ('SUPPLIER NAME', 'SUPPLIER PRODUCT NAME' ,'CONTACT NUMBER','DATE Of BECOMING SUPPLIER','YOUR MODE OF PAYMENT','ADDRESS OF SUPPLIER','PROBLEM FROM SUPPLIER')
    
    listBox = tt.Treeview(top, columns=cols, show='headings', selectmode='browse',height=25)
    listBox.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
    for col in cols:
        listBox.heading(col, text=col)
        
    vsb = tt.Scrollbar(top, orient="vertical", command=listBox.yview)
    vsb.place(relx=0.937, rely=0.216, relheight=0.580, relwidth=0.012)
    listBox.configure(yscrollcommand = vsb.set)

    vsb1 = tt.Scrollbar(top, orient="horizontal", command=listBox.xview)
    vsb1.place(relx=0.046, rely=0.797, relheight=0.025, relwidth=0.896)
    listBox.configure(xscrollcommand=vsb1.set)
    

    mycursor.execute("select count(*) from supplier")
    
    for i in mycursor:
        l6=tk.Label(top,text="Total Supplier :",font=("arial",15,"bold"))
        l7=tk.Label(top,text=str(i[0]),font=("arial",15,"bold"))
        l6.place(relx=0.056, rely=0.827, relheight=0.025, relwidth=0.12)
        l7.place(relx=0.162, rely=0.827, relheight=0.025, relwidth=0.12)
        
    
    
    button1=tk.Button(top,text="SEARCH",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:search_btn(Ms))
    button1.place(relx=0.021, rely=0.867, height=60, width=250)

    button2=tk.Button(top,text="ADD",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:ADD(Ad))
    button2.place(relx=0.200, rely=0.867, height=60, width=250)

    button3=tk.Button(top,text="DELETE",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:delete_btn())
    button3.place(relx=0.415, rely=0.867, height=60, width=250)

    button4=tk.Button(top,text="MODIFY",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:modi_btn(Md))
    button4.place(relx=0.627, rely=0.867, height=60, width=250)

    button5=tk.Button(top,text="GENERATE RECORD",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:gen_btn())
    button5.place(relx=0.809, rely=0.867, height=60, width=250)

    mycursor.execute("select * from supplier order by name asc")
    for i in mycursor:
        listBox.insert("", "end", values=i)
    
def toplevel1(top):
    global listBox2,option2,r2,skframe2,l6,l7
    def onclosing():
        clear2()
        Ad1.withdraw()
    def onclosings():
        Md1.withdraw()
    Ad1 = tk.Toplevel(Mp)
    Ad1.title("STOCK UP: ADD ENTRY")
    Ad1.withdraw()
    Ad1.protocol("WM_DELETE_WINDOW",onclosing)
    Md1 = tk.Toplevel(Mp)
    Md1.title("STOCK UP: MODIFY ENTRY")
    Md1.withdraw()
    Md1.protocol("WM_DELETE_WINDOW",onclosings)
    menue(top)
    
    
    l4=tk.Label(top,text="Purchase Details",font=("arial",35,"bold"))
    l4.place(relx=0.385, rely=0.019, height=79, width=525)
    
    
    l5=tk.Label(top,text="Type:",font=("arial",20,"bold"))
    l5.place(relx=0.001, rely=0.125, height=40, relwidth=0.341)
    
    r2=tk.StringVar()
    Entry1=tk.Entry(top,width=40,textvariable=r2)
    Entry1.place(relx=0.209, rely=0.125, height=40, relwidth=0.241)
    Entry1.configure(background="white")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="-family {Palatino Linotype} -size 15")
    Entry1.configure(foreground="#000000")
    Entry1.configure(highlightbackground="#d9d9d9")
    Entry1.configure(highlightcolor="black")
    Entry1.configure(insertbackground="black")
    Entry1.configure(selectbackground="#c4c4c4")
    Entry1.configure(selectforeground="black")

    option2 = tk.StringVar()
    v=['All Records','Product Name','Quantity','Measurement', 'Price','Supplier Name','Date','Address']
    c2= tt.Combobox(top,value=v,width=35,textvariable=option2,state='readonly')
    c2.set("Choose Category to Search")
    c2.place(relx=0.568, rely=0.114, relheight=0.069, relwidth=0.269)
    c2.configure(font="-family {Palatino Linotype} -size 14")
    cols = ('PRODUCT NAME','QUANTITY','MEASUREMENT','PRICE','SUPPLIER NAME','DATE Of PURCHASE','ADDRESS OF SUPPLIER')
    
    listBox2 = tt.Treeview(top, columns=cols, show='headings', selectmode='browse',height=25)
    listBox2.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
    for col in cols:
        listBox2.heading(col, text=col)
        
    vsb = tt.Scrollbar(top, orient="vertical", command=listBox2.yview)
    vsb.place(relx=0.942, rely=0.216, relheight=0.580, relwidth=0.012)
    listBox2.configure(yscrollcommand = vsb.set)

    x=[]
    r6=tk.StringVar()
    mycursor.execute("select * from purchase order by date2 desc")
    for i in mycursor:
        x.append(i)

    mycursor.execute("select SUM(Price) from purchase")
    for i in mycursor:
        if len(x)==0:
            l6=tk.Label(top,text="Total Purchase :",font=("arial",15,"bold"))
            l7=tk.Entry(top,width=10,textvariable=r6,state="readonly")
            l6.place(relx=0.046, rely=0.827, relheight=0.025, relwidth=0.12)
            l7.place(relx=0.176, rely=0.827, relheight=0.025, relwidth=0.10)
            r6.set(str(0))
        else:    
            l6=tk.Label(top,text="Total Purchase :",font=("arial",15,"bold"))
            l7=tk.Entry(top,width=20,textvariable=r6,state="readonly")
            l6.place(relx=0.046, rely=0.827, relheight=0.025, relwidth=0.12)
            l7.place(relx=0.176, rely=0.827, relheight=0.025, relwidth=0.10)
            r6.set(str(i[0]))
        
   
    
    button1=tk.Button(top,text="SEARCH",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:search_btn(Mp))
    button1.place(relx=0.021, rely=0.867, height=60, width=250)

    button2=tk.Button(top,text="ADD",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:Add2(Ad1))
    button2.place(relx=0.200, rely=0.867, height=60, width=250)

    button3=tk.Button(top,text="DELETE",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:delete_btn2())
    button3.place(relx=0.415, rely=0.867, height=60, width=250)

    button4=tk.Button(top,text="MODIFY",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:modi_btn2(Md1))
    button4.place(relx=0.627, rely=0.867, height=60, width=250)

    button5=tk.Button(top,text="GENERATE RECORD",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:gen_btn2())
    button5.place(relx=0.809, rely=0.867, height=60, width=250)
    
    listBox2.delete(*listBox2.get_children())
    mycursor.execute("select * from purchase order by date2 desc")
    for i in mycursor:
        listBox2.insert("", "end", values=i)
    
def toplevel4(top):
    global listBox1,option1,r1
    def onclosing():
        clear1()
        Add.withdraw()
    def onclosings():
        Mdd.withdraw()
    Add = tk.Toplevel(Ip)
    Add.title("STOCK UP: ADD ENTRY")
    Add.withdraw()
    Add.protocol("WM_DELETE_WINDOW",onclosing)
    Mdd = tk.Toplevel(Ip)
    Mdd.title("STOCK UP: MODIFY ENTRY")
    Mdd.withdraw()
    Mdd.protocol("WM_DELETE_WINDOW",onclosings)
    menue(top)
    
    l4=tk.Label(top,text="Remaining Stock",font=("arial",35,"bold"))
    l4.place(relx=0.385, rely=0.019, height=79, width=525)

    l5=tk.Label(top,text="Type:",font=("arial",20,"bold"))
    l5.place(relx=0.001, rely=0.125, height=40, relwidth=0.341)
    
    r1=tk.StringVar()
    Entry1=tk.Entry(top,width=40,textvariable=r1)
    Entry1.place(relx=0.209, rely=0.125, height=40, relwidth=0.241)
    Entry1.configure(background="white")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="-family {Palatino Linotype} -size 15")
    Entry1.configure(foreground="#000000")
    Entry1.configure(highlightbackground="#d9d9d9")
    Entry1.configure(highlightcolor="black")
    Entry1.configure(insertbackground="black")
    Entry1.configure(selectbackground="#c4c4c4")
    Entry1.configure(selectforeground="black")

    option1 = tk.StringVar()
    v=['All Records','SR.NO','PRODUCT NAME' ,'QUANTITY','MEASUREMENT','PRICE INVESTED']
    c2= tt.Combobox(top,value=v,width=35,textvariable=option1,state='readonly')
    c2.set("Choose Category to Search")
    c2.place(relx=0.568, rely=0.114, relheight=0.069, relwidth=0.269)
    c2.configure(font="-family {Palatino Linotype} -size 14")
    cols = ('SR.N0','PRODUCT NAME' ,'QUANTITY','MEASUREMENT','PRICE INVESTED')
    
    listBox1 = tt.Treeview(top, columns=cols, show='headings', selectmode='browse',height=28)
    listBox1.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.643)
    for col in cols:
        listBox1.heading(col, text=col)
        listBox1.column(col,minwidth=0,width=100)
        
    vsb = tt.Scrollbar(top, orient="vertical", command=listBox1.yview)
    vsb.place(relx=0.689, rely=0.216, relheight=0.580, relwidth=0.012)
    listBox1.configure(yscrollcommand = vsb.set)

    mycursor.execute("select count(*) from stock")
    for i in mycursor:
        l6=tk.Label(top,text="Total Product :",font=("arial",15,"bold"))
        l7=tk.Label(top,text=str(i[0]),font=("arial",15,"bold"))
        l6.place(relx=0.002, rely=0.807, relheight=0.025, relwidth=0.15)
        l7.place(relx=0.134, rely=0.807, relheight=0.025, relwidth=0.14)
    sbframe=tk.Frame(top)
    sbframe.place(relx=0.748, rely=0.214, relheight=0.769, relwidth=0.179)
    
    button1=tk.Button(sbframe,text="SEARCH",padx=98,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:search_btn(Ip))
    button1.pack(side="top",pady=25)
     
    button2=tk.Button(sbframe,text="ADD",padx=110,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:Add1(Add))
    button2.pack(side="top",pady=25)

    button3=tk.Button(sbframe,text="DELETE",padx=100,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:delete_btn1())
    button3.pack(side="top",pady=25)

    button4=tk.Button(sbframe,text="MODIFY",padx=99,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:modi_btn1(Mdd))
    button4.pack(side="top",pady=25)

    button5=tk.Button(sbframe,text="GENERATE RECORD",padx=61,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:gen_btn1())
    button5.pack(side="top",pady=25)

    mycursor.execute("select * from stock")
    for i in mycursor:
        listBox1.insert("", "end", values=i)
    
def modi_btn1(top):
    global listBox1
    selected_items1 = listBox1.selection()
    cur_item1=listBox1.focus()
    k=listBox1.item(cur_item1)["values"]
    if(len(k)==0):
        messagebox.showerror("No Record Selected","Please select a record to Modify")
    else:
        def onclosing():
            top.withdraw()
        global pname2,srno,measure,quantity,pi
        top.deiconify()
        top.geometry("500x550+0+0")
        
        srno = tk.StringVar()
        pname2 =tk.StringVar()
        quantity=tk.StringVar()
        measure=tk.StringVar()
        pi=tk.StringVar()

        Label2 = tk.Label(top)
        Label2.grid(row=0,column=1,pady=20,sticky="nw")
        Label2.configure(font="-family {Palatino Linotype} -size 18")
        Label2.configure(text="Record Entery")

        Label2 = tk.Label(top)
        Label2.grid(row=2,column=0,pady=20,sticky="w")
        Label2.configure(font="-family {Palatino Linotype} -size 12")
        Label2.configure(text="SR.NO")

        Label2_1 = tk.Label(top)
        Label2_1.grid(row=3,column=0,pady=20,sticky="w")
        Label2_1.configure(font="-family {Palatino Linotype} -size 12")
        Label2_1.configure(text="PRODUCT NAME")

        Label2_2 = tk.Label(top)
        Label2_2.grid(row=4,column=0,pady=20,sticky="w")
        Label2_2.configure(font="-family {Palatino Linotype} -size 12")
        Label2_2.configure(text="QUANTITY")
        
        Label3 = tk.Label(top)
        Label3.grid(row=5,column=0,pady=20,sticky="w")
        Label3.configure(font="-family {Palatino Linotype} -size 12")
        Label3.configure(text="MEASUREMENT")

        Label3_5 = tk.Label(top)
        Label3_5.grid(row=6,column=0,pady=20,sticky="w")
        Label3_5.configure(font="-family {Palatino Linotype} -size 12")
        Label3_5.configure(text="PRICE INVESTED")

        Entry1 = tk.Entry(top,width=28, textvariable=srno)
        Entry1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
        Entry1.configure(font="-family {Palatino Linotype} -size 12")

        Entry2 = tk.Entry(top,width=28, textvariable=pname2)
        Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 12")

        Entry3 = tk.Entry(top,width=28, textvariable=quantity)
        Entry3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
        Entry3.configure(font="-family {Palatino Linotype} -size 12")

        Entry4 = tk.Entry(top,width=28, textvariable=measure)
        Entry4.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        Entry4.configure(font="-family {Palatino Linotype} -size 12")

        Entry5 = tk.Entry(top,width=28, textvariable=pi)
        Entry5.grid(row=6,column=1,pady=20,padx=20,sticky="w")
        Entry5.configure(font="-family {Palatino Linotype} -size 12")
        

        button6=tk.Button(top,text="SAVE",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:savemodi1(k,top))
        button6.grid(row=7,column=1,pady=20)

        button7=tk.Button(top,text="CANCEL",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:onclosing())
        button7.grid(row=7,column=0,pady=20)

        srno.set(k[0])
        pname2.set(k[1])
        quantity.set(k[2])
        measure.set(k[3])
        pi.set(k[4])
        
def Add2(top):
    def onclosing():
        clear2()
        top.withdraw()
    global pname3, Price,Quantity,Measurement,name2,date2,City
    top.deiconify()
    top.geometry("500x650+0+0")
    
    pname3 = tk.StringVar()
    Quantity = tk.StringVar()
    Measurement = tk.StringVar()
    Price = tk.StringVar()
    name2 = tk.StringVar()
    City = tk.StringVar()    

    Label2 = tk.Label(top)
    Label2.grid(row=0,column=1,pady=20,sticky="nw")
    Label2.configure(font="-family {Palatino Linotype} -size 18")
    Label2.configure(text="Record Entery")

    Label2 = tk.Label(top)
    Label2.grid(row=2,column=0,pady=20,sticky="w")
    Label2.configure(font="-family {Palatino Linotype} -size 12")
    Label2.configure(text="Product Name")

    Label2_1 = tk.Label(top)
    Label2_1.grid(row=3,column=0,pady=20,sticky="w")
    Label2_1.configure(font="-family {Palatino Linotype} -size 12")
    Label2_1.configure(text="Quantity")

    Label2_2 = tk.Label(top)
    Label2_2.grid(row=4,column=0,pady=20,sticky="w")
    Label2_2.configure(font="-family {Palatino Linotype} -size 12")
    Label2_2.configure(text="Measurement")
    
    Label3 = tk.Label(top)
    Label3.grid(row=5,column=0,pady=20,sticky="w")
    Label3.configure(font="-family {Palatino Linotype} -size 12")
    Label3.configure(text="Price")

    Label3_5 = tk.Label(top)
    Label3_5.grid(row=6,column=0,pady=20,sticky="w")
    Label3_5.configure(font="-family {Palatino Linotype} -size 12")
    Label3_5.configure(text="Supplier Name")

    Label3_6 = tk.Label(top)
    Label3_6.grid(row=7,column=0,pady=20,sticky="w")
    Label3_6.configure(font="-family {Palatino Linotype} -size 12")
    Label3_6.configure(text="Date Of Purchase(dd/mm/yy)")

    Label3_8 = tk.Label(top)
    Label3_8.grid(row=8,column=0,pady=20,sticky="w")
    Label3_8.configure(activebackground="#f9f9f9")
    Label3_8.configure(font="-family {Palatino Linotype} -size 12")
    Label3_8.configure(text="Address of Supplier")

    v=[]
    mycursor.execute("select pname2 from stock")
    for i in mycursor:
        if i not in v:
            v.append(i)
    
    c2= tt.Combobox(top,value=v,width=21,textvariable=pname3,state='readonly')
    c2.set("Choose the Product")
    c2.grid(row=2,column=1,pady=20,padx=20,sticky="w")
    c2.configure(font="-family {Palatino Linotype} -size 14")

    Entry2 = tk.Entry(top,width=28, textvariable=Quantity)
    Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
    Entry2.configure(font="-family {Palatino Linotype} -size 12")

    f=[]
    mycursor.execute("select measure from stock")
    for i in mycursor:
        if i not in f:
            f.append(i)
    
    c3= tt.Combobox(top,value=f,width=21,textvariable=Measurement,state='readonly')
    c3.set("Choose the Measurement")
    c3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
    c3.configure(font="-family {Palatino Linotype} -size 14")

    Entry4 = tk.Entry(top,width=28, textvariable=Price)
    Entry4.grid(row=5,column=1,pady=20,padx=20,sticky="w")
    Entry4.configure(font="-family {Palatino Linotype} -size 12")

    Entry5 = tk.Entry(top,width=28, textvariable=name2)
    Entry5.grid(row=6,column=1,pady=20,padx=20,sticky="w")
    Entry5.configure(font="-family {Palatino Linotype} -size 12")

    date2 = DateEntry(top,width=34, background="blue",foreground="white",borderwidth=2)
    date2.grid(row=7,column=1,pady=20,padx=20,sticky="w")

    Entry7 = tk.Entry(top,width=28, textvariable=City)
    Entry7.grid(row=8,column=1,pady=20,padx=20,sticky="w")
    Entry7.configure(font="-family {Palatino Linotype} -size 12")

    mycursor.execute("select name2 from purchase order by date2 desc limit 1")
    for i in mycursor:
        name2.set(i[0])
    
    button6=tk.Button(top,text="SAVE",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:saveadd2(top))
    button6.grid(row=9,column=1,pady=20)

    button7=tk.Button(top,text="CANCEL",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:onclosing())
    button7.grid(row=9,column=0,pady=20)

def Add1(top):
    def onclosing():
        clear1()
        top.withdraw()
    global srno, pname2,quantity, measure, pi
    top.deiconify()
    top.geometry("500x550+0+0")
        
    srno = tk.StringVar()
    pname2 = tk.StringVar()
    quantity = tk.StringVar()
    measure = tk.StringVar()
    pi = tk.StringVar()

    Label2 = tk.Label(top)
    Label2.grid(row=0,column=1,pady=20,sticky="nw")
    Label2.configure(font="-family {Palatino Linotype} -size 18")
    Label2.configure(text="Record Entery")

    Label2 = tk.Label(top)
    Label2.grid(row=2,column=0,pady=20,sticky="w")
    Label2.configure(font="-family {Palatino Linotype} -size 12")
    Label2.configure(text="SR.NO")

    Label2_1 = tk.Label(top)
    Label2_1.grid(row=3,column=0,pady=20,sticky="w")
    Label2_1.configure(font="-family {Palatino Linotype} -size 12")
    Label2_1.configure(text="PRODUCT NAME")

    Label2_2 = tk.Label(top)
    Label2_2.grid(row=4,column=0,pady=20,sticky="w")
    Label2_2.configure(font="-family {Palatino Linotype} -size 12")
    Label2_2.configure(text="QUANTITY")
    
    Label3 = tk.Label(top)
    Label3.grid(row=5,column=0,pady=20,sticky="w")
    Label3.configure(font="-family {Palatino Linotype} -size 12")
    Label3.configure(text="MEASUREMENT")

    Label3_5 = tk.Label(top)
    Label3_5.grid(row=6,column=0,pady=20,sticky="w")
    Label3_5.configure(font="-family {Palatino Linotype} -size 12")
    Label3_5.configure(text="PRICE INVESTED")

    Entry1 = tk.Entry(top,width=28, textvariable=srno)
    Entry1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
    Entry1.configure(font="-family {Palatino Linotype} -size 12")

    Entry2 = tk.Entry(top,width=28, textvariable=pname2)
    Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
    Entry2.configure(font="-family {Palatino Linotype} -size 12")

    Entry3 = tk.Entry(top,width=28, textvariable=quantity)
    Entry3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
    Entry3.configure(font="-family {Palatino Linotype} -size 12")

    Entry4 = tk.Entry(top,width=28, textvariable=measure)
    Entry4.grid(row=5,column=1,pady=20,padx=20,sticky="w")
    Entry4.configure(font="-family {Palatino Linotype} -size 12")

    Entry5 = tk.Entry(top,width=28, textvariable=pi)
    Entry5.grid(row=6,column=1,pady=20,padx=20,sticky="w")
    Entry5.configure(font="-family {Palatino Linotype} -size 12")
    

    button6=tk.Button(top,text="SAVE",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:saveadd1(top))
    button6.grid(row=7,column=1,pady=20)

    button7=tk.Button(top,text="CANCEL",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:onclosing())
    button7.grid(row=7,column=0,pady=20)

    mycursor.execute("select count(*) from stock")
    for i in mycursor:
        srno.set(i[0]+1)

def ADD(top):
    def onclosing():
        clear()
        top.withdraw()
    global name, pname,cnum, date1, sadd, mop, sp
    top.deiconify()
    top.geometry("520x650+0+0")
    
    name = tk.StringVar()
    pname = tk.StringVar()
    cnum = tk.StringVar()
    mop = tk.StringVar()
    sadd = tk.StringVar()
    sp = tk.StringVar()

    Label2 = tk.Label(top)
    Label2.grid(row=0,column=1,pady=20,sticky="nw")
    Label2.configure(font="-family {Palatino Linotype} -size 18")
    Label2.configure(text="Record Entery")

    Label2 = tk.Label(top)
    Label2.grid(row=2,column=0,pady=20,sticky="w")
    Label2.configure(font="-family {Palatino Linotype} -size 12")
    Label2.configure(text="SUPPLIER NAME")

    Label2_1 = tk.Label(top)
    Label2_1.grid(row=3,column=0,pady=20,sticky="w")
    Label2_1.configure(font="-family {Palatino Linotype} -size 12")
    Label2_1.configure(text="PRODUCT NAME")

    Label2_2 = tk.Label(top)
    Label2_2.grid(row=4,column=0,pady=20,sticky="w")
    Label2_2.configure(font="-family {Palatino Linotype} -size 12")
    Label2_2.configure(text="CONTACT NUMBER")

    Label3 = tk.Label(top)
    Label3.grid(row=5,column=0,pady=20,sticky="w")
    Label3.configure(font="-family {Palatino Linotype} -size 12")
    Label3.configure(text="Date Of Becoming Supplier:")

    Label3_5 = tk.Label(top)
    Label3_5.grid(row=6,column=0,pady=20,sticky="w")
    Label3_5.configure(font="-family {Palatino Linotype} -size 12")
    Label3_5.configure(text="MODE OF PAYMENT")

    Label3_6 = tk.Label(top)
    Label3_6.grid(row=7,column=0,pady=20,sticky="w")
    Label3_6.configure(font="-family {Palatino Linotype} -size 12")
    Label3_6.configure(text="ADDRESS OF SUPPLIER")

    Label3_8 = tk.Label(top)
    Label3_8.grid(row=8,column=0,pady=20,sticky="w")
    Label3_8.configure(activebackground="#f9f9f9")
    Label3_8.configure(font="-family {Palatino Linotype} -size 12")
    Label3_8.configure(text="PROBLEM FROM SUPPLIER")

    Entry1 = tk.Entry(top,width=28, textvariable=name)
    Entry1.grid(row=2,column=1,pady=20,padx=20,sticky="w")
    Entry1.configure(font="-family {Palatino Linotype} -size 12")

    Entry2 = tk.Entry(top,width=28, textvariable=pname)
    Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
    Entry2.configure(font="-family {Palatino Linotype} -size 12")

    Entry3 = tk.Entry(top,width=28, textvariable=cnum)
    Entry3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
    Entry3.configure(font="-family {Palatino Linotype} -size 12")

    date1 = DateEntry(top,width=34, background="blue",foreground="white",borderwidth=2)
    date1.grid(row=5,column=1,pady=20,padx=20,sticky="w")

    Entry5 = tk.Entry(top,width=28, textvariable=mop)
    Entry5.grid(row=6,column=1,pady=20,padx=20,sticky="w")
    Entry5.configure(font="-family {Palatino Linotype} -size 12")
    
    Entry6 = tk.Entry(top,width=28, textvariable=sadd)
    Entry6.grid(row=7,column=1,pady=20,padx=20,sticky="w")
    Entry6.configure(font="-family {Palatino Linotype} -size 12")

    Entry7 = tk.Entry(top,width=28, textvariable=sp)
    Entry7.grid(row=8,column=1,pady=20,padx=20,sticky="w")
    Entry7.configure(font="-family {Palatino Linotype} -size 12")

    button6=tk.Button(top,text="SAVE",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:saveadd(top))
    button6.grid(row=9,column=1,pady=20)

    button7=tk.Button(top,text="CANCEL",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:onclosing())
    button7.grid(row=9,column=0,pady=20)


def saveadd2(tp):
    
    
    if (name2.get() == "" or pname3.get() == "" or Quantity.get() == "" or Measurement.get()=="" or Price.get()=="" or date2.get_date()=="" or City.get() == ""):
        clear2()
        pname3.set("Please fill all the fields correctly!")
    
    else:
        list1=[]
        if(pname3.get()==""):
            list1.append('Null')
        else:
            list1.append(pname3.get())
        if (Quantity.get() == ""):
            list1.append('Null')
        else:
            num=Quantity.get()
            if(num.isalpha()==True):
                Quantity.set("Please fill all the fields correctly!")
            else:
                list1.append(Quantity.get())
        if (Measurement.get() == ""):
            list1.append('Null')
        else:
            num=Measurement.get()
            if(num.isdigit()==True):
                Measurement.set("Please fill all the fields correctly!")
            else:
                list1.append(Measurement.get())
        if (Price.get() == ""):
            list1.append('Null')
        else:
            num=Price.get()
            if(num.isalpha()==True):
                Price.set("Please fill all the fields correctly!")
            else:
                list1.append(Price.get())
        if (name2.get() == ""):
            list1.append('Null')
        else:
            t=[]
            mycursor.execute("select sadd,count(*) from supplier where name=? GROUP BY name",(name2.get().upper(),))
            for i in mycursor:
                t.append(i)
            if len(t)==0:
                name2.set("Please check the supplier name carefully!")
            else:
                list1.append(name2.get().upper())
        if (date2.get_date() == ""):
            list1.append('Null')
        else:
            try:
                da=date2.get_date()
                list1.append(da)
            except:
                pass
        if (City.get() == ""):
            City.set("Please check the supplier address carefully!")
        else:
            t=[]
            mycursor.execute("select name,count(*) from supplier where sadd=? GROUP BY sadd",(City.get().upper(),))
            for i in mycursor:
                t.append(i)
            if len(t)==0:
                City.set("Please check the supplier name carefully!")
            else:
                list1.append(City.get().upper())
        
        mycursor.execute("INSERT INTO purchase VALUES(?,?,?,?,?,?,?)",(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6]))
        mycursor.execute("UPDATE stock SET Quantity=Quantity+?,pi=pi+? where pname2=? AND measure=?",(int(list1[1]),int(list1[3]),list1[0],list1[2])) 
        conn.commit()
        clear2()
        tp.withdraw()
    listBox2.delete(*listBox2.get_children())
    mycursor.execute("select * from purchase order by date2 desc")  
               
    for i in mycursor:
        listBox2.insert("", "end", values=i)
    x=[]
    r6=tk.StringVar()
    mycursor.execute("select * from purchase order by date2 desc")
    for i in mycursor:
        x.append(i)

    mycursor.execute("select SUM(Price) from purchase")
    for i in mycursor:
        if len(x)==0:
            l6=tk.Label(Mp,text="Total Purchase :",font=("arial",15,"bold"))
            l7=tk.Entry(Mp,width=20,textvariable=r6,state="readonly")
            l6.place(relx=0.046, rely=0.827, relheight=0.025, relwidth=0.12)
            l7.place(relx=0.176, rely=0.827, relheight=0.025, relwidth=0.10)
            r6.set(str(list1[3]))
        else:    
            l6=tk.Label(Mp,text="Total Purchase :",font=("arial",15,"bold"))
            l7=tk.Entry(Mp,width=20,textvariable=r6,state="readonly")
            l6.place(relx=0.046, rely=0.827, relheight=0.025, relwidth=0.12)
            l7.place(relx=0.176, rely=0.827, relheight=0.025, relwidth=0.10)
            r6.set(str(i[0]))
    

def saveadd1(tp):
    try:
        if (srno.get() == "" or pname2.get() == "" or measure.get() == ""):
            clear1()
            srno.set("Please fill all the fields correctly!")
        else:
            list1=[]
            if(srno.get()==""):
                list1.append('Null')
            else:
                num1=srno.get()
                if(num1.isalpha()==True):
                    srno.set("Please fill all the fields correctly!")
                else:
                    list1.append(num1)
            if (pname2.get() == ""):
                list1.append('Null')
            else:
                list1.append(pname2.get())
            if (quantity.get() == ""):
                list1.append('0')
            else:
                num=quantity.get()
                if(num.isalpha()==True):
                    quantity.set("Please fill all the fields correctly!")
                else:
                    list1.append(num)
            if (measure.get() == ""):
                list1.append('Null')
            else:
                list1.append(measure.get())
            if (pi.get() == ""):
                list1.append('0')
            else:
                num2=pi.get()
                if(num2.isalpha()==True):
                    pi.set("Please fill all the fields correctly!")
                else:
                    list1.append(num2)
            
            mycursor.execute("INSERT INTO stock VALUES(?,?,?,?,?)",(list1[0],list1[1],list1[2],list1[3],list1[4]))
            conn.commit()
            clear1()
            tp.withdraw()
        listBox1.delete(*listBox1.get_children())
        mycursor.execute("select * from stock order by srno asc")
        for i in mycursor:
            listBox1.insert("", "end", values=i)
        mycursor.execute("select count(*) from stock")
        for i in mycursor:
            l6=tk.Label(Ip,text="Total Product :",font=("arial",15,"bold"))
            l7=tk.Label(Ip,text=str(i[0]),font=("arial",15,"bold"))
            l6.place(relx=0.002, rely=0.807, relheight=0.025, relwidth=0.15)
            l7.place(relx=0.134, rely=0.807, relheight=0.025, relwidth=0.14)
    except:
        pass
def saveadd(tp):
    try:
        if (name.get() == "" or pname.get() == ""):
            clear()
            name.set("Please fill all the fields correctly!")
        else:
            try:
                list1=[]
                if(name.get()==""):
                    list1.append('Null')
                else:
                    list1.append(name.get().upper())
                if (pname.get() == ""):
                    list1.append('Null')
                else:
                    list1.append(pname.get().upper())
                if (cnum.get() == ""):
                    list1.append('Null')
                else:
                    num=cnum.get()
                    if(num.isalpha()==True or len(num)!=10):
                        cnum.set("Please fill all the fields correctly!")
                    else:
                        list1.append(num)
                if (date1.get() == ""):
                    list1.append('Null')
                else:
                    try:
                        da=date1.get_date()
                        list1.append(da)
                    except:
                        pass
                if (mop.get() == ""):
                    list1.append('Null')
                else:
                    list1.append(mop.get())
                if (sadd.get() == ""):
                    list1.append('Null')
                else:
                    list1.append(sadd.get().upper())
                if (sp.get() == ""):
                    list1.append('Null')
                else:
                    list1.append(sp.get())
            
                mycursor.execute("INSERT INTO supplier VALUES(?,?,?,?,?,?,?)",(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6]))
                conn.commit()
                clear()
                tp.withdraw()
            except:
                pass
        listBox.delete(*listBox.get_children())
        mycursor.execute("select * from supplier order by name asc")  
                   
        for i in mycursor:
            listBox.insert("", "end", values=i)
        mycursor.execute("select count(*) from supplier")
        for i in mycursor:
            l6=tk.Label(Ms,text="Total Supplier :",font=("arial",15,"bold"))
            l7=tk.Label(Ms,text=str(i[0]),font=("arial",15,"bold"))
            l6.place(relx=0.056, rely=0.827, relheight=0.025, relwidth=0.12)
            l7.place(relx=0.162, rely=0.827, relheight=0.025, relwidth=0.12)
    except:
        pass
    
def delete_btn():
    try:
        global listBox
        MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning")
        if MsgBox == "yes":
            selected_items = listBox.selection()
            cur_item=listBox.focus()
            k=listBox.item(cur_item)["values"]
            mycursor.execute("DELETE FROM supplier WHERE name=? AND pname=? AND cnum=? AND date1=? AND mop=? AND sadd=? AND sp=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4]),str(k[5]),str(k[6])))
            listBox.delete(*listBox.get_children())
            mycursor.execute("select * from supplier order by name asc")   
            for i in mycursor:
                listBox.insert("", "end", values=i)
            conn.commit()
            mycursor.execute("select count(*) from supplier")
        for i in mycursor:
            l6=tk.Label(Ms,text="Total Supplier :",font=("arial",15,"bold"))
            l7=tk.Label(Ms,text=str(i[0]),font=("arial",15,"bold"))
            l6.place(relx=0.056, rely=0.827, relheight=0.025, relwidth=0.12)
            l7.place(relx=0.162, rely=0.827, relheight=0.025, relwidth=0.12)
        else:
            pass
    except:
        pass

def delete_btn1():
    try:
        global listBox1
        MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning")
        if MsgBox == "yes":
            selected_items = listBox1.selection()
            cur_item=listBox1.focus()
            k=listBox1.item(cur_item)["values"]
            mycursor.execute("DELETE FROM stock WHERE srno=? AND pname2=? AND quantity=? AND measure=? AND pi=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4])))
            conn.commit()
            for selected_item in selected_items:
                listBox1.delete(selected_item)
            mycursor.execute("select count(*) from stock")
            for i in mycursor:
                l6=tk.Label(Ip,text="Total Product :",font=("arial",15,"bold"))
                l7=tk.Label(Ip,text=str(i[0]),font=("arial",15,"bold"))
                l6.place(relx=0.002, rely=0.807, relheight=0.025, relwidth=0.15)
                l7.place(relx=0.134, rely=0.807, relheight=0.025, relwidth=0.14)
        else:
            pass
    except:
        pass
    
def delete_btn2():
    try:
        global listBox2,skframe2
        MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning")
        if MsgBox == "yes":
            selected_items = listBox2.selection()
            cur_item=listBox2.focus()
            k=listBox2.item(cur_item)["values"]
            mycursor.execute("DELETE FROM purchase WHERE pname3=? AND Quantity=? AND Measurement=? AND Price=? AND name2=? AND date2=? AND City=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4]),str(k[5]),str(k[6])))
            mycursor.execute("UPDATE stock SET Quantity=Quantity-?,pi=pi-? where pname2=? AND measure=?",(int(k[1]),int(k[3]),k[0],k[2]))
            listBox2.delete(*listBox2.get_children())
            mycursor.execute("select * from purchase order by date2 desc")             
            for i in mycursor:
                listBox2.insert("", "end", values=i)
            conn.commit()
            x=[]
            r6=tk.StringVar()
            mycursor.execute("select * from purchase order by date2 desc")
            for i in mycursor:
                x.append(i)

            mycursor.execute("select SUM(Price) from purchase")
            for i in mycursor:
                if len(x)==0:
                    l6=tk.Label(Mp,text="Total Purchase :",font=("arial",15,"bold"))
                    l7=tk.Entry(Mp,width=20,textvariable=r6,state="readonly")
                    l6.place(relx=0.046, rely=0.827, relheight=0.025, relwidth=0.12)
                    l7.place(relx=0.176, rely=0.827, relheight=0.025, relwidth=0.10)
                    r6.set(str(0))
                else:    
                    l6=tk.Label(Mp,text="Total Purchase :",font=("arial",15,"bold"))
                    l7=tk.Entry(Mp,width=20,textvariable=r6,state="readonly")
                    l6.place(relx=0.046, rely=0.827, relheight=0.025, relwidth=0.12)
                    l7.place(relx=0.176, rely=0.827, relheight=0.025, relwidth=0.10)
                    r6.set(str(i[0]))
            
        else:
            pass
    except:
        pass

def search_btn(top):
    if top==Ms:
        global listBox,option,r
        _entry = r.get()
        _option = option.get()

        if (_option == 'Supplier Name'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from supplier where name like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Product Name'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from supplier where pname like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == "Date of becoming Supplier"):
            listBox.delete(*listBox.get_children())
            mycursor.execute("select * from supplier where date1 like '%{0}%'".format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Contact Number'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from supplier where cnum like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Mode of Payment'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from supplier where mop like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Address'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from supplier where sadd like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == 'Problem'):
            listBox.delete(*listBox.get_children())
            mycursor.execute('select * from supplier where sp like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox.insert("", "end", values=i)
        elif (_option == "All Records"):
            listBox.delete(*listBox.get_children())
            mycursor.execute("select * from supplier order by name asc")
            for i in mycursor:
                listBox.insert("", "end", values=i)
        else:
            option.set("Choose Category Correctly!")
    elif top==Ip:
        global listBox1,option1,r1
        _entry = r1.get()
        _option1 = option1.get()

        if (_option1 == 'SR.NO'):
            listBox1.delete(*listBox1.get_children())
            mycursor.execute('select * from stock where srno like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox1.insert("", "end", values=i)
        elif (_option1 == 'PRODUCT NAME'):
            listBox1.delete(*listBox1.get_children())
            mycursor.execute('select * from stock where pname2 like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox1.insert("", "end", values=i)
        elif (_option1 == "QUANTITY"):
            listBox1.delete(*listBox1.get_children())
            mycursor.execute('select * from stock where quantity like "{0}"'.format(_entry))
            for i in mycursor:
                listBox1.insert("", "end", values=i)
        elif (_option1 == 'MEASUREMENT'):
            listBox1.delete(*listBox1.get_children())
            mycursor.execute('select * from stock where measure like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox1.insert("", "end", values=i)
        elif (_option1 == 'PRICE INVESTED'):
            listBox1.delete(*listBox1.get_children())
            mycursor.execute('select * from stock where pi like "{0}"'.format(_entry))
            for i in mycursor:
                listBox1.insert("", "end", values=i)
        elif (_option1 == "All Records"):
            listBox1.delete(*listBox1.get_children())
            mycursor.execute("select * from stock")
            for i in mycursor:
                listBox1.insert("", "end", values=i)
        else:
            option1.set("Choose Category Correctly!")
    elif top==Mp:
        global listBox2,option2,r2
        _entry = r2.get()
        _option2 = option2.get()

        if (_option2 == 'Product Name'):
            listBox2.delete(*listBox2.get_children())
            mycursor.execute('select * from purchase where pname3 like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox2.insert("", "end", values=i)
        elif (_option2 == 'Quantity'):
            listBox2.delete(*listBox2.get_children())
            mycursor.execute('select * from purchase where Quantity like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox2.insert("", "end", values=i)
        elif (_option2 == 'Measurement'):
            listBox2.delete(*listBox2.get_children())
            mycursor.execute('select * from purchase where Measurement like "%{0}"'.format(_entry))
            for i in mycursor:
                listBox2.insert("", "end", values=i)
        elif (_option2 == 'Price'):
            listBox2.delete(*listBox2.get_children())
            mycursor.execute('select * from purchase where Price like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox2.insert("", "end", values=i)
        elif (_option2 == 'Supplier Name'):
            listBox2.delete(*listBox2.get_children())
            mycursor.execute('select * from purchase where name2 like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox2.insert("", "end", values=i)
        elif (_option2 == 'Date'):
            listBox2.delete(*listBox2.get_children())
            mycursor.execute('select * from purchase where date2 like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox2.insert("", "end", values=i)
        elif (_option2 == 'Address'):
            listBox2.delete(*listBox2.get_children())
            mycursor.execute('select * from purchase where City like "%{0}%"'.format(_entry))
            for i in mycursor:
                listBox2.insert("", "end", values=i)
        elif (_option2 == 'All Records'):
            listBox2.delete(*listBox2.get_children())
            mycursor.execute("select * from purchase order by date2 desc")
            for i in mycursor:
                listBox2.insert("", "end", values=i)
        else:
            option2.set("Choose Category Correctly!")
            
def gen_btn():
    try:
        global listBox
        files=[("Pdf Document","*.pdf")]
        fp= tk.filedialog.asksaveasfile(filetype = files,mode="w",defaultextension=".pdf")
        fw= open("temp.txt","w")
        if fp is None:
            messagebox.showerror("Invalid file Name","Please enter valid Name")
        else:
            l1=[]
            h=()
            for l in listBox.get_children():
                d=[]
                m=listBox.item(l)["values"]
                m.pop(len(m)-1)
                for i in m:
                    b=str(i)
                    r=b.replace(" ","\n")
                    d.append(r)
                h=tuple(d)
                l1.append(h)
            st="\n"
            head=['Supplier Name', 'Product Name' ,'Contact No.','Date','Mop','Address']
            st+=tabulate(l1,headers=head,tablefmt="grid")
            fw.write(st)
            fw.close()
            pdf=FPDF()
            pdf.add_page()
            pdf.set_font("Courier",style="B",size=8.5)
            pdf.set_margins(0,0,0)
            f=open("temp.txt","r")
            for x in f:
                pdf.cell(-1,5,txt = x, ln = 1)
            pdf.output(fp.name)
            f.close()
            os.remove("temp.txt")
            
    except PermissionError:
        messagebox.showerror("Error Message","Please try again after closing the document you want to overwrite")
    except:
        pass
        
        

def gen_btn1():
    try:
        global listBox1
        files=[("Pdf Document","*.pdf")]
        fp= tk.filedialog.asksaveasfile(filetype = files,mode="w",defaultextension=".pdf")
        fw= open("temp.txt","w")
        if fp is None:
            messagebox.showerror("Invalid file Name","Please enter valid Name")
        else:   
            l1=[]
            h=()
            for l in listBox1.get_children():
                d=[]
                m=listBox1.item(l)["values"]
                for i in m:
                    b=str(i)
                    r=b.replace(" ","\n")
                    d.append(r)
                h=tuple(d)
                l1.append(h)
            st="\n"
            head=['SR.N0','PRODUCT NAME' ,'QUANTITY','MEASUREMENT','PRICE INVESTED']
            st+=tabulate(l1,headers=head,tablefmt="grid")
            fw.write(st)
            fw.close()
            pdf=FPDF()
            pdf.add_page()
            pdf.set_font("Courier",style="B",size=8.5)
            pdf.set_margins(0,0,0)
            f=open("temp.txt","r")
            for x in f:
                pdf.cell(0,5,txt = x, ln = 1,align="C")
            pdf.output(fp.name)
            f.close()
            os.remove("temp.txt")
    except PermissionError:
        messagebox.showerror("Error Message","Please try again after closing the document you want to overwrite")
    except:
        pass
def gen_btn2():
    try:
        global listBox2
        files=[("Pdf Document","*.pdf")]
        fp= tk.filedialog.asksaveasfile(filetype = files,mode="w",defaultextension=".pdf")
        fw= open("temp.txt","w")
        if fp is None:
            messagebox.showerror("Invalid file Name","Please enter valid Name")
        else:   
            l1=[]
            h=()
            for l in listBox2.get_children():
                d=[]
                m=listBox2.item(l)["values"]
                for i in m:
                    b=str(i)
                    r=b.replace(" ","\n")
                    d.append(r)
                h=tuple(d)
                l1.append(h)
            st="\n"
            head=['PRODUCT NAME','QUANTITY','MEASUREMENT','PRICE','SUPPLIER NAME','DATE\nOf PURCHASE','ADDRESS\nOF SUPPLIER']
            st+=tabulate(l1,headers=head,tablefmt="grid")
            fw.write(st)
            fw.close()
            pdf=FPDF()
            pdf.add_page()
            pdf.set_font("Courier",style="B",size=8.5)
            pdf.set_margins(0,0,0)
            f=open("temp.txt","r")
            for x in f:
                pdf.cell(-1,5,txt = x, ln = 1)
            pdf.output(fp.name)
            f.close()
            os.remove("temp.txt")
    except PermissionError:
        messagebox.showerror("Error Message","Please try again after closing the document you want to overwrite")
    except:
        pass

def modi_btn2(top):
    global listBox2
    selected_items1 = listBox2.selection()
    cur_item1=listBox2.focus()
    k1=listBox2.item(cur_item1)["values"]
    if(len(k1)==0):
        messagebox.showerror("No Record Selected","Please select a record to Modify")
    else:
        def onclosing():
            clear2()
            top.withdraw()
        global pname3, Price,Quantity,Measurement,name2,date2,City
        top.deiconify()
        top.geometry("500x650+0+0")
        
        pname3 = tk.StringVar()
        Quantity = tk.StringVar()
        Measurement = tk.StringVar()
        Price = tk.StringVar()
        name2 = tk.StringVar()
        date2 = tk.StringVar()
        City = tk.StringVar()    

        Label2 = tk.Label(top)
        Label2.grid(row=0,column=1,pady=20,sticky="nw")
        Label2.configure(font="-family {Palatino Linotype} -size 18")
        Label2.configure(text="Record Entery")

        Label2 = tk.Label(top)
        Label2.grid(row=2,column=0,pady=20,sticky="w")
        Label2.configure(font="-family {Palatino Linotype} -size 12")
        Label2.configure(text="Product Name")

        Label2_1 = tk.Label(top)
        Label2_1.grid(row=3,column=0,pady=20,sticky="w")
        Label2_1.configure(font="-family {Palatino Linotype} -size 12")
        Label2_1.configure(text="Quantity")

        Label2_2 = tk.Label(top)
        Label2_2.grid(row=4,column=0,pady=20,sticky="w")
        Label2_2.configure(font="-family {Palatino Linotype} -size 12")
        Label2_2.configure(text="Measurement")
        
        Label3 = tk.Label(top)
        Label3.grid(row=5,column=0,pady=20,sticky="w")
        Label3.configure(font="-family {Palatino Linotype} -size 12")
        Label3.configure(text="Price")

        Label3_5 = tk.Label(top)
        Label3_5.grid(row=6,column=0,pady=20,sticky="w")
        Label3_5.configure(font="-family {Palatino Linotype} -size 12")
        Label3_5.configure(text="Supplier Name")

        Label3_6 = tk.Label(top)
        Label3_6.grid(row=7,column=0,pady=20,sticky="w")
        Label3_6.configure(font="-family {Palatino Linotype} -size 12")
        Label3_6.configure(text="Date Of Purchase(dd/mm/yy)")

        Label3_8 = tk.Label(top)
        Label3_8.grid(row=8,column=0,pady=20,sticky="w")
        Label3_8.configure(activebackground="#f9f9f9")
        Label3_8.configure(font="-family {Palatino Linotype} -size 12")
        Label3_8.configure(text="Address of Supplier")

        v=[]
        mycursor.execute("select pname2 from stock")
        for i in mycursor:
            v.append(i)
        
        c2= tt.Combobox(top,value=v,width=21,textvariable=pname3,state='readonly')
        c2.set("Choose the Product")
        c2.grid(row=2,column=1,pady=20,padx=20,sticky="w")
        c2.configure(font="-family {Palatino Linotype} -size 14")

        Entry2 = tk.Entry(top,width=28, textvariable=Quantity)
        Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 12")

        f=[]
        mycursor.execute("select measure from stock")
        for i in mycursor:
            f.append(i)
        
        c3= tt.Combobox(top,value=f,width=21,textvariable=Measurement,state='readonly')
        c3.set("Choose the Measurement")
        c3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
        c3.configure(font="-family {Palatino Linotype} -size 14")

        Entry4 = tk.Entry(top,width=28, textvariable=Price)
        Entry4.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        Entry4.configure(font="-family {Palatino Linotype} -size 12")

        Entry5 = tk.Entry(top,width=28, textvariable=name2)
        Entry5.grid(row=6,column=1,pady=20,padx=20,sticky="w")
        Entry5.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry6 = tk.Entry(top,width=28, textvariable=date2)
        Entry6.grid(row=7,column=1,pady=20,padx=20,sticky="w")
        Entry6.configure(font="-family {Palatino Linotype} -size 12")

        Entry7 = tk.Entry(top,width=28, textvariable=City)
        Entry7.grid(row=8,column=1,pady=20,padx=20,sticky="w")
        Entry7.configure(font="-family {Palatino Linotype} -size 12")
        
        button6=tk.Button(top,text="SAVE",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:savemodi2(k1,top))
        button6.grid(row=9,column=1,pady=20)

        button7=tk.Button(top,text="CANCEL",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:onclosing())
        button7.grid(row=9,column=0,pady=20)
            
        pname3.set(k1[0])
        Quantity.set(k1[1])
        Measurement.set(k1[2]) 
        Price.set(k1[3])
        name2.set(k1[4])
        date2.set(k1[5])
        City.set(k1[6])
    
def modi_btn(top):
    global listBox
    selected_items1 = listBox.selection()
    cur_item1=listBox.focus()
    k1=listBox.item(cur_item1)["values"]
    if(len(k1)==0):
        messagebox.showerror("No Record Selected","Please select a record to Modify")
    else:
        def onclosing():
            top.withdraw()
        global name1, pname1,cnum1, date2, sadd1, mop1, sp1
        top.deiconify()
        top.geometry("600x650+0+0")
        
        name1 = tk.StringVar()
        pname1 = tk.StringVar()
        cnum1 = tk.StringVar()
        date2 = tk.StringVar()
        mop1 = tk.StringVar()
        sadd1 = tk.StringVar()
        sp1 = tk.StringVar()

        Label2 = tk.Label(top)
        Label2.grid(row=0,column=1,pady=20,sticky="nw")
        Label2.configure(font="-family {Palatino Linotype} -size 18")
        Label2.configure(text="Record Entery")

        Label2 = tk.Label(top)
        Label2.grid(row=2,column=0,pady=20,sticky="w")
        Label2.configure(font="-family {Palatino Linotype} -size 12")
        Label2.configure(text="Supplier Name")

        Label2_1 = tk.Label(top)
        Label2_1.grid(row=3,column=0,pady=20,sticky="w")
        Label2_1.configure(font="-family {Palatino Linotype} -size 12")
        Label2_1.configure(text="PRODUCT NAME")

        Label2_2 = tk.Label(top)
        Label2_2.grid(row=4,column=0,pady=20,sticky="w")
        Label2_2.configure(font="-family {Palatino Linotype} -size 12")
        Label2_2.configure(text="Contact Number")

        Label3 = tk.Label(top)
        Label3.grid(row=5,column=0,pady=20,sticky="w")
        Label3.configure(font="-family {Palatino Linotype} -size 12")
        Label3.configure(text="Date Of Becoming Supplier(dd/mm/yy)")

        Label3_5 = tk.Label(top)
        Label3_5.grid(row=6,column=0,pady=20,sticky="w")
        Label3_5.configure(font="-family {Palatino Linotype} -size 12")
        Label3_5.configure(text="MODE OF PAYMENT")

        Label3_6 = tk.Label(top)
        Label3_6.grid(row=7,column=0,pady=20,sticky="w")
        Label3_6.configure(font="-family {Palatino Linotype} -size 12")
        Label3_6.configure(text="Address OF SUPPLIER")

        Label3_8 = tk.Label(top)
        Label3_8.grid(row=8,column=0,pady=20,sticky="w")
        Label3_8.configure(activebackground="#f9f9f9")
        Label3_8.configure(font="-family {Palatino Linotype} -size 12")
        Label3_8.configure(text="PROBLEM FROM SUPPLIER")

        Entry_a = tk.Entry(top,width=28, textvariable=name1)
        Entry_a.grid(row=2,column=1,pady=20,padx=20,sticky="w")
        Entry_a.configure(font="-family {Palatino Linotype} -size 12")

        Entry_b = tk.Entry(top,width=28, textvariable=pname1)
        Entry_b.grid(row=3,column=1,pady=20,padx=20,sticky="w")
        Entry_b.configure(font="-family {Palatino Linotype} -size 12")

        Entry_c = tk.Entry(top,width=28, textvariable=cnum1)
        Entry_c.grid(row=4,column=1,pady=20,padx=20,sticky="w")
        Entry_c.configure(font="-family {Palatino Linotype} -size 12")

        Entry_d = tk.Entry(top,width=28, textvariable=date2)
        Entry_d.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        Entry_d.configure(font="-family {Palatino Linotype} -size 12")

        Entry_e = tk.Entry(top,width=28, textvariable=mop1)
        Entry_e.grid(row=6,column=1,pady=20,padx=20,sticky="w")
        Entry_e.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry_f = tk.Entry(top,width=28, textvariable=sadd1)
        Entry_f.grid(row=7,column=1,pady=20,padx=20,sticky="w")
        Entry_f.configure(font="-family {Palatino Linotype} -size 12")

        Entry_g = tk.Entry(top,width=28, textvariable=sp1)
        Entry_g.grid(row=8,column=1,pady=20,padx=20,sticky="w")
        Entry_g.configure(font="-family {Palatino Linotype} -size 12")

        button6=tk.Button(top,text="SAVE",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:savemodi(k1,top))
        button6.grid(row=9,column=1,pady=20)

        button7=tk.Button(top,text="CANCEL",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:onclosing())
        button7.grid(row=9,column=0,pady=20)

        name1.set(k1[0])
        pname1.set(k1[1])
        cnum1.set(k1[2])
        date2.set(k1[3])
        sadd1.set(k1[5])
        mop1.set(k1[4])
        sp1.set(k1[6])

def savemodi(k2,top1):
    global listBox,name1, pname1,cnum1, date2, sadd1, mop1, sp1
    try:
        if (name1.get() == "" or pname1.get() == ""):
            name1.set("Please fill all the fields correctly!") 
        else:
            try:
                list1=[]
                if(name1.get()==""):
                    list1.append('Null')
                else:
                    list1.append(name1.get())
                if (pname1.get() == ""):
                    list1.append('Null')
                else:
                    list1.append(pname1.get())
                if (cnum1.get() == ""):
                    list1.append('Null')
                else:
                    num=cnum1.get()
                    if(num.isalpha()==True or len(num)<10 or len(num)>10):
                        cnum1.set("Please fill all the fields correctly!")
                    else:
                        list1.append(num)
                if (date2.get() == ""):
                    list1.append('Null')
                else:
                    try:
                        da=date2.get()
                        d=dt.datetime.strptime(da,"%d/%m/%y")
                        list1.append(da)
                    except:
                        date2.set("Please fill all the fields correctly!")
                if (mop1.get() == ""):
                    list1.append('Null')
                else:
                    list1.append(mop1.get())
                if (sadd1.get() == ""):
                    list1.append('Null')
                else:
                    list1.append(sadd1.get())
                if (sp1.get() == ""):
                    list1.append('Null')
                else:
                    list1.append(sp1.get())
                
                mycursor.execute("UPDATE supplier SET name=?,pname=?,cnum=?,date1=?,mop=?,sadd=?,sp=? WHERE name=? AND pname=? AND cnum=? AND date1=? AND mop=? AND sadd=? AND sp=?",(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],k2[0],k2[1],k2[2],k2[3],k2[4],k2[5],k2[6]))
                conn.commit()
                top1.withdraw()
            except:
                pass
        listBox.delete(*listBox.get_children())
        mycursor.execute("select * from supplier order by name asc")
        for i in mycursor:
            listBox.insert("", "end", values=i)
        
    except:
        pass

def savemodi1(k3,top2):
    global listBox1,pname2,srno,measure,quantity,pi
    try:
        if (srno.get() == "" or pname2.get() == "" or measure.get() == ""):
            clear1()
            srno.set("Please fill all the fields correctly!")
        else:
            list1=[]
            if(srno.get()==""):
                list1.append('Null')
            else:
                num1=srno.get()
                if(num1.isalpha()==True):
                    srno.set("Please fill all the fields correctly!")
                else:
                    list1.append(num1)
            if (pname2.get() == ""):
                list1.append('Null')
            else:
                list1.append(pname2.get())
            if (quantity.get() == ""):
                list1.append('0')
            else:
                num=quantity.get()
                if(num.isalpha()==True):
                    quantity.set("Please fill all the fields correctly!")
                else:
                    list1.append(num)
            if (measure.get() == ""):
                list1.append('Null')
            else:
                num2=measure.get()
                if(num2.isalpha()!=True):
                    measure.set("Please fill all the fields correctly!")
                else:
                    list1.append(num2)
            if (pi.get() == ""):
                list1.append('0')
            else:
                num2=pi.get()
                if(num2.isalpha()==True):
                    pi.set("Please fill all the fields correctly!")
                else:
                    list1.append(num2)
                list1.append(pi.get())
                
            mycursor.execute("UPDATE stock SET srno=?,pname2=?,quantity=?,measure=?,pi=? WHERE srno=? AND pname2=? AND quantity=? AND measure=? AND pi=?",(list1[0],list1[1],list1[2],list1[3],list1[4],k3[0],k3[1],k3[2],k3[3],k3[4]))
            conn.commit()
            top2.withdraw()
                    
            listBox1.delete(*listBox1.get_children())
            mycursor.execute("select * from stock order by srno asc")
            for i in mycursor:
                listBox1.insert("", "end", values=i)
    except:
        pass

def savemodi2(k4,top3):
    global pname3,Quantity,Measurement,Price,name2,date2,City,skframe2
    try:
        if (name2.get() == "" or pname3.get() == "" or Quantity.get() == "" or Measurement.get()=="" or Price.get()=="" or date2.get()=="" or City.get() == ""):
            name2.set("Please fill all the fields correctly!") 
        else:
            list1=[]
            if(pname3.get()==""):
                list1.append('Null')
            else:
                list1.append(pname3.get())
            if (Quantity.get() == ""):
                list1.append('Null')
            else:
                num=Quantity.get()
                if(num.isalpha()==True):
                    Quantity.set("Please fill all the fields correctly!")
                else:
                    list1.append(Quantity.get())
            if (Measurement.get() == ""):
                list1.append('Null')
            else:
                num=Measurement.get()
                if(num.isdigit()==True):
                    Measurement.set("Please fill all the fields correctly!")
                else:
                    list1.append(Measurement.get())
            if (Price.get() == ""):
                list1.append('Null')
            else:
                num=Price.get()
                if(num.isalpha()==True):
                    Price.set("Please fill all the fields correctly!")
                else:
                    list1.append(Price.get())
            if (name2.get() == ""):
                list1.append('Null')
            else:
                t=[]
                mycursor.execute("select name from supplier")
                for i in mycursor:
                    t.append(i)
                p=0
                for i in t:
                    if name2.get() not in i[0]:
                        p=0
                    else:
                        p+=1
                        break
                if p==0:
                    name2.set("Please check the supplier name carefully!")
                else:
                    list1.append(name2.get())
            if (date2.get() == ""):
                list1.append('Null')
            else:
                try:
                    da=date2.get()
                    d=dt.datetime.strptime(da,"%d/%m/%y")
                    list1.append(da)
                except:
                    date2.set("Please Fill the date carefully!")
            if (City.get() == ""):
                City.set("Please check the supplier address carefully!")
            else:
                t=[]
                mycursor.execute("select sadd from supplier")
                for i in mycursor:
                    t.append(i)
                p=0
                for i in t:
                    if City.get() not in i[0]:
                        p=0
                    else:
                        p+=1
                        break
                if p==0:
                    City.set("Please check the supplier name carefully!")
                else:
                    list1.append(City.get())
            
            mycursor.execute("UPDATE purchase SET pname3=?,Quantity=?,Measurement=?,Price=?,name2=?,date2=?,City=? WHERE pname3=? AND Quantity=? AND Measurement=? AND Price=? AND name2=? AND date2=? AND City=?",(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],k4[0],k4[1],k4[2],k4[3],k4[4],k4[5],k4[6]))
            if list1[1]!=k4[1]:
                a=int(list1[1])
                b=int(k4[1])
                if(a>b):
                   h=a-b
                   mycursor.execute("UPDATE stock SET quantity=quantity+? WHERE pname2=? AND measure=?",(h,list1[0],list1[2]))
                else:
                    h=b-a
                    mycursor.execute("UPDATE stock SET quantity=quantity-? WHERE pname2=? AND measure=?",(h,list1[0],list1[2]))
            else:
                pass
            if list1[3]!=k4[3]:
                c=int(list1[3])
                d=int(k4[3])
                if(c>d):
                    h=c-d
                    mycursor.execute("UPDATE stock SET quantity=quantity+? WHERE pname2=? AND measure=?",(h,list1[0],list1[2]))
                else:
                    h=d-c
                    mycursor.execute("UPDATE stock SET quantity=quantity-? WHERE pname2=? AND measure=?",(h,list1[0],list1[2]))
            else:
                pass
            conn.commit()
            top3.withdraw()
        listBox2.delete(*listBox2.get_children())
        mycursor.execute("select * from purchase order by date2 desc")
        for i in mycursor:
            listBox2.insert("", "end", values=i)
        x=[]
        r6=tk.StringVar()
        mycursor.execute("select * from purchase order by date2 desc")
        for i in mycursor:
            x.append(i)

        mycursor.execute("select SUM(Price) from purchase")
        for i in mycursor:
            if len(x)==0:
                l6=tk.Label(Mp,text="Total Purchase :",font=("arial",15,"bold"))
                l7=tk.Entry(Mp,width=20,textvariable=r6,state="readonly")
                l6.place(relx=0.046, rely=0.807, relheight=0.025, relwidth=0.10)
                l7.place(relx=0.146, rely=0.807, relheight=0.025, relwidth=0.10)
                r6.set(str(0))
            else:    
                l6=tk.Label(Mp,text="Total Purchase :",font=("arial",15,"bold"))
                l7=tk.Entry(Mp,width=20,textvariable=r6,state="readonly")
                l6.place(relx=0.046, rely=0.807, relheight=0.025, relwidth=0.10)
                l7.place(relx=0.146, rely=0.807, relheight=0.025, relwidth=0.10)
                r6.set(str(i[0]))
    except:
        pass
#############################################------------------------------SALES------------------------------------------################################################################################################################################

def toplevel5(top1):
    global listBox3,option3,r3,skframe3
    def onclosing():
        As1.withdraw()
    def onclosings():
        mycursor.execute("Drop table if exists sale3")
        cb1.withdraw()
    As1 = tk.Toplevel(Sa)
    As1.title("STOCK UP: VIEW ENTRY")
    As1.withdraw()
    As1.protocol("WM_DELETE_WINDOW",onclosing)
    cb1 = tk.Toplevel(Sa)
    cb1.title("STOCK UP: CREATE BILL")
    cb1.withdraw()
    cb1.protocol("WM_DELETE_WINDOW",onclosings)
    menue(top1)
    global listBox3,option3,r3,skframe3
    r3 = tk.StringVar()
    option3 = tk.StringVar()

    Label1 = tk.Label(top1)
    Label1.place(relx=0.385, rely=0.019, height=79, width=492)
    Label1.configure(font="-family {Palatino Linotype} -size 24")
    Label1.configure(text='''SALES RECORD''')

    Label2 = tk.Label(top1)
    Label2.place(relx=0.001, rely=0.125, height=40, relwidth=0.341)
    Label2.configure(font="-family {Palatino Linotype} -size 17")
    Label2.configure(text='''TYPE''')

    Entry1 = tk.Entry(top1,textvariable=r3)
    Entry1.place(relx=0.209, rely=0.125, height=40, relwidth=0.241)
    Entry1.configure(background="white")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="-family {Palatino Linotype} -size 15")
    Entry1.configure(foreground="#000000")
    Entry1.configure(highlightbackground="#d9d9d9")
    Entry1.configure(highlightcolor="black")
    Entry1.configure(insertbackground="black")
    Entry1.configure(selectbackground="#c4c4c4")
    Entry1.configure(selectforeground="black")

    TCombobox1 = tt.Combobox(top1, textvariable=option3,state='readonly')
    value_list = ['All Record', 'Invoice No.', 'Customer Name','Customer Address', 'Date of Bill(dd-mm-yy)', 'No. Of Product', 'Total Quantity','Total Price','Final Amount']
    TCombobox1.place(relx=0.568, rely=0.114, relheight=0.069, relwidth=0.269)
    TCombobox1.configure(values=value_list)
    TCombobox1.configure(font="-family {Palatino Linotype} -size 14")
    option3.set("Choose Category to Search")

    global listBox3
    cols = ('INVOICE NO.','CUSTUMOR NAME','CUSTOMER ADDRESS','DATE OF BILL','No. OF PRODUCT','TOTAL QUANTITY','TOTAL PRICE','FINAL AMOUNT')
    listBox3 = tt.Treeview(top1, columns=cols, show='headings', selectmode='browse')
    for col in cols:
        listBox3.heading(col, text=col)
    listBox3.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
    vsb = tt.Scrollbar(top1, orient="horizontal", command=listBox3.xview)
    vsb.place(relx=0.046, rely=0.797, relheight=0.025, relwidth=0.896)
    listBox3.configure(xscrollcommand=vsb.set)

    vsb = tt.Scrollbar(top1, orient="vertical", command=listBox3.yview)
    vsb.place(relx=0.937, rely=0.216, relheight=0.580, relwidth=0.012)
    listBox3.configure(yscrollcommand=vsb.set)

    Button1 = tk.Button(top1,command=lambda:search_btn1())
    Button1.place(relx=0.021, rely=0.867, height=60, width=250)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#d9d9d9")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(font="-family {Palatino Linotype} -size 16")
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''SEARCH''')

    Button2 = tk.Button(top1,command=lambda:As(As1))
    Button2.place(relx=0.200, rely=0.867, height=60, width=250)
    Button2.configure(activebackground="#ececec")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#d9d9d9")
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(font="-family {Palatino Linotype} -size 16")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''VIEW''')

    Button3 = tk.Button(top1,command=lambda:delete_btn4())
    Button3.place(relx=0.415, rely=0.867, height=60, width=250)
    Button3.configure(activebackground="#ececec")
    Button3.configure(activeforeground="#000000")
    Button3.configure(background="#d9d9d9")
    Button3.configure(disabledforeground="#a3a3a3")
    Button3.configure(font="-family {Palatino Linotype} -size 16")
    Button3.configure(foreground="#000000")
    Button3.configure(highlightcolor="black")
    Button3.configure(highlightbackground="#d9d9d9")
    Button3.configure(pady="0")
    Button3.configure(text='''DELETE''')

    Button4 = tk.Button(top1,command=lambda:cb(cb1))
    Button4.place(relx=0.627, rely=0.867, height=60, width=250)
    Button4.configure(activebackground="#ececec")
    Button4.configure(activeforeground="#000000")
    Button4.configure(background="#d9d9d9")
    Button4.configure(disabledforeground="#a3a3a3")
    Button4.configure(font="-family {Palatino Linotype} -size 16")
    Button4.configure(foreground="#000000")
    Button4.configure(highlightbackground="#d9d9d9")
    Button4.configure(highlightcolor="black")
    Button4.configure(pady="0")
    Button4.configure(text='''CREATE BILL''')

    Button5 = tk.Button(top1,command=lambda:gen_btn6())
    Button5.place(relx=0.809, rely=0.867, height=60, width=250)
    Button5.configure(activebackground="#ececec")
    Button5.configure(activeforeground="#000000")
    Button5.configure(background="#d9d9d9")
    Button5.configure(disabledforeground="#a3a3a3")
    Button5.configure(font="-family {Palatino Linotype} -size 16")
    Button5.configure(foreground="#000000")
    Button5.configure(highlightbackground="#d9d9d9")
    Button5.configure(highlightcolor="black")
    Button5.configure(pady="0")
    Button5.configure(text='''GENERATE RECORD''')


    listBox3.delete(*listBox3.get_children())
    mycursor.execute("select * from sale2 order by dob1 desc")
    for i in mycursor:
        listBox3.insert("", "end", values=i)

def As(top):
    global listBox4,listBox3,r4,r5
    selected_items1 = listBox3.selection()
    cur_item1=listBox3.focus()
    k=listBox3.item(cur_item1)["values"]
    if(len(k)==0):
        messagebox.showerror("No Record Selected","Please select a record to view the bill")
    else:
        x, y = top.winfo_screenwidth(), top.winfo_screenheight()
        top.geometry("%dx%d+0+0" % (x, y))
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.iconbitmap(r"dc.ico")
        def onclosing():
            top.withdraw()
        top.deiconify()
        
        
        l4=tk.Label(top,text="CUSTOMER BILL",font=("arial",35,"bold"))
        l4.place(relx=0.365, rely=0.019, height=79, width=525)
        
       
        l5=tk.Label(top,text="Invoice No.:",font=("arial",20,"bold"))
        l5.place(relx=0.028, rely=0.136,  relheight=0.032, relwidth=0.149)
        
        r5=tk.StringVar()
        Entry1=tk.Entry(top,width=20,textvariable=r5,state="readonly")
        Entry1.place(relx=0.158, rely=0.136,  relheight=0.032, relwidth=0.142)
        Entry1.configure(background="white")
        Entry1.configure(disabledforeground="#a3a3a3")
        Entry1.configure(font="-family {Palatino Linotype} -size 15")
        Entry1.configure(foreground="#000000")
        Entry1.configure(highlightbackground="#d9d9d9")
        Entry1.configure(highlightcolor="black")
        Entry1.configure(insertbackground="black")
        Entry1.configure(selectbackground="#c4c4c4")
        Entry1.configure(selectforeground="black")
        
        r4=tk.StringVar()
        Entry2=tk.Entry(top,width=20,textvariable=r4,state="readonly")
        Entry2.place(relx=0.810, rely=0.136, relheight=0.032, relwidth=0.145)
        Entry2.configure(background="white")
        Entry2.configure(disabledforeground="#a3a3a3")
        Entry2.configure(font="-family {Palatino Linotype} -size 15")
        Entry2.configure(foreground="#000000")
        Entry2.configure(highlightbackground="#d9d9d9")
        Entry2.configure(highlightcolor="black")
        Entry2.configure(insertbackground="black")
        Entry2.configure(selectbackground="#c4c4c4")
        Entry2.configure(selectforeground="black")

        l6=tk.Label(top,text="Date(dd-mm-yy):",font=("arial",20,"bold"))
        l6.place(relx=0.668, rely=0.114, relheight=0.069, relwidth=0.142)
        
        cols = ('PRODUCT NAME' ,'QUANTITY','MEASUREMENT','RATE','DISCOUNT %','TOTAL AMOUNT')
        
        listBox4 = tt.Treeview(top, columns=cols, show='headings', selectmode='browse',height=25)
        listBox4.place(relx=0.046, rely=0.219, relheight=0.580, relwidth=0.896)
        for col in cols:
            listBox4.heading(col, text=col)
            
        vsb = tt.Scrollbar(top, orient="vertical", command=listBox4.yview)
        vsb.place(relx=0.942, rely=0.216, relheight=0.580, relwidth=0.012)
        listBox4.configure(yscrollcommand = vsb.set)
        

        button5=tk.Button(top,text="GENERATE RECORD",padx=61,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:gen_btn5(k))
        button5.place(relx=0.321, rely=0.810, height=60, width=440)

        r5.set(k[0])
        r4.set(k[3])
    
        mycursor.execute("select pname5,Quantity2,Measurement2,rate1,discount1,Price2  from sale where ino=? AND dob=?",(k[0],k[3]))
        for i in mycursor:
            listBox4.insert("", "end", values=i)

def cb(top):
    global listBox5,r6,r7,r9,r10,r12,r11
    mycursor.execute("create table IF NOT EXISTS sale3(pname4 text,Quantity1 int,Measurement1 text, rate int , discount int, Price1 int)")
    def onclosings():
        clear3()
        Add1.withdraw()

    def onclosings1():
        clear3()
        Mdd1.withdraw()

    Add1 = tk.Toplevel(Ip)
    Add1.title("STOCK UP: BILL ENTRY")
    Add1.withdraw()
    Add1.protocol("WM_DELETE_WINDOW",onclosings)

    Mdd1 = tk.Toplevel(Ip)
    Mdd1.title("STOCK UP: MODIFY ENTRY")
    Mdd1.withdraw()
    Mdd1.protocol("WM_DELETE_WINDOW",onclosings1)

    top.deiconify()
    top.iconbitmap(r"dc.ico")
    x, y = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d+0+0" % (x, y))
    top.minsize(148, 1)
    top.maxsize(1924, 1055)
    top.resizable(1, 1)
    
    sbframe2=tk.Frame(top)
    sbframe2.place(relx=0.008, rely=0.114,  relheight=0.269, relwidth=0.549)
    
    
    l4=tk.Label(top,text="CREATE BILL",font=("arial",35,"bold"))
    l4.place(relx=0.365, rely=0.019, height=79, width=525)
    
    l5=tk.Label(sbframe2,text="Invoice No.     :",font=("arial",20,"bold"))
    l5.grid(row=0,column=0)
    
    r7=tk.StringVar()
    Entry1=tk.Entry(sbframe2,width=20,textvariable=r7)
    Entry1.grid(row=0,columnspan=1,column=1,sticky="w")
    Entry1.configure(background="white")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="-family {Palatino Linotype} -size 15")
    Entry1.configure(foreground="#000000")
    Entry1.configure(highlightbackground="#d9d9d9")
    Entry1.configure(highlightcolor="black")
    Entry1.configure(insertbackground="black")
    Entry1.configure(selectbackground="#c4c4c4")
    Entry1.configure(selectforeground="black")
    
    l8=tk.Label(top,text="Date:",font=("arial",20,"bold"))
    l8.place(relx=0.690, rely=0.114, relheight=0.069, relwidth=0.149)
    r6 = DateEntry(top,width=34, background="blue",foreground="white",borderwidth=2)
    r6.place(relx=0.795, rely=0.136, relheight=0.032, relwidth=0.142)

    l9=tk.Label(sbframe2,text="Name-Ph no.   :",font=("arial",20,"bold"))
    l9.grid(row=1,column=0)
    r11=tk.StringVar()
    Entry3=tk.Entry(sbframe2,width=35,textvariable=r11)
    Entry3.grid(row=1,column=1)
    Entry3.configure(background="white")
    Entry3.configure(disabledforeground="#a3a3a3")
    Entry3.configure(font="-family {Palatino Linotype} -size 15")
    Entry3.configure(foreground="#000000")
    Entry3.configure(highlightbackground="#d9d9d9")
    Entry3.configure(highlightcolor="black")
    Entry3.configure(insertbackground="black")
    Entry3.configure(selectbackground="#c4c4c4")
    Entry3.configure(selectforeground="black")

    l10=tk.Label(sbframe2,text="Customer Add. :",font=("arial",20,"bold"))
    l10.grid(row=2,column=0)
    r12=tk.StringVar()
    Entry4=tk.Entry(sbframe2,width=35,textvariable=r12)
    Entry4.grid(row=2,column=1)
    Entry4.configure(background="white")
    Entry4.configure(disabledforeground="#a3a3a3")
    Entry4.configure(font="-family {Palatino Linotype} -size 15")
    Entry4.configure(foreground="#000000")
    Entry4.configure(highlightbackground="#d9d9d9")
    Entry4.configure(highlightcolor="black")
    Entry4.configure(insertbackground="black")
    Entry4.configure(selectbackground="#c4c4c4")
    Entry4.configure(selectforeground="black")
    cols = ('PRODUCT NAME' ,'QUANTITY','MEASUREMENT','RATE','DISCOUNT%','TOTAL AMOUNT')
    
    listBox5 = tt.Treeview(top, columns=cols, show='headings', selectmode='browse',height=25)
    listBox5.place(relx=0.005, rely=0.299, relheight=0.500, relwidth=0.750)
    for col in cols:
        listBox5.heading(col, text=col)
        listBox5.column(col,minwidth=0,width=100)
        
    vsb = tt.Scrollbar(top, orient="vertical", command=listBox5.yview)
    vsb.place(relx=0.755, rely=0.299, relheight=0.500, relwidth=0.012)
    listBox5.configure(yscrollcommand = vsb.set)

    
    sbframe1=tk.Frame(top)
    sbframe1.place(relx=0.021, rely=0.807, height=60, width=750)

    
    r9=tk.StringVar()
    r10=tk.StringVar()
    

    l12=tk.Label(sbframe1,text="Delivery Charges :",font=("arial",15,"bold"))
    l13=tk.Entry(sbframe1,width=20,textvariable=r9)
    l12.pack(side="left",padx=40,pady=10)
    l13.pack(side="left",pady=10)
    

    l10=tk.Label(sbframe1,text="Final Amount :",font=("arial",15,"bold"))
    l11=tk.Entry(sbframe1,width=25,textvariable=r10,state="readonly")
    l10.pack(side="left",padx=40,pady=10)
    l11.pack(side="left",pady=10)

    try:
        k=mycursor.execute('select ino1 from sale2').fetchall()[-1]
        if len(k)>0:
            r7.set(str(int(k[0])+1))
        else:
            r7.set("1")
    except:
        r7.set("1")
    
    sbframe=tk.Frame(top)
    sbframe.place(relx=0.788, rely=0.214, relheight=0.769, relwidth=0.179)

    button1=tk.Button(sbframe,text="ADD",padx=98,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:Add3(Add1))
    button1.pack(side="top",pady=25)


    button2=tk.Button(sbframe,text="DELETE",padx=90,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:delete_btn3())
    button2.pack(side="top",pady=25)

    button3=tk.Button(sbframe,text="MODIFY",padx=90,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:Mdd3(Mdd1))
    button3.pack(side="top",pady=25)

    button4=tk.Button(sbframe,text="SAVE AND CALC. FINAL AMOUNT",padx=10,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:saveandcalc())
    button4.pack(side="top",pady=25)

    button5=tk.Button(sbframe,text="GENERATE BILL",padx=67,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:gen_btn4())
    button5.pack(side="top",pady=25)


def Add3(top):
    global pname4,Quantity1,Measurement1,rate,discount
    def onclosing():
        clear3()
        top.withdraw()
    
    top.deiconify()
    top.geometry("500x550+0+0")

    pname4=tk.StringVar()
    Quantity1=tk.StringVar()
    Measurement1=tk.StringVar()
    rate=tk.StringVar()
    discount=tk.StringVar()
    
    Label2 = tk.Label(top)
    Label2.grid(row=0,column=1,pady=20,sticky="nw")
    Label2.configure(font="-family {Palatino Linotype} -size 18")
    Label2.configure(text="Record Entery")

    Label2 = tk.Label(top)
    Label2.grid(row=2,column=0,pady=20,sticky="w")
    Label2.configure(font="-family {Palatino Linotype} -size 12")
    Label2.configure(text="Product Name")

    Label2_1 = tk.Label(top)
    Label2_1.grid(row=3,column=0,pady=20,sticky="w")
    Label2_1.configure(font="-family {Palatino Linotype} -size 12")
    Label2_1.configure(text="Quantity")

    Label2_2 = tk.Label(top)
    Label2_2.grid(row=4,column=0,pady=20,sticky="w")
    Label2_2.configure(font="-family {Palatino Linotype} -size 12")
    Label2_2.configure(text="Measurement")
    
    Label3 = tk.Label(top)
    Label3.grid(row=5,column=0,pady=20,sticky="w")
    Label3.configure(font="-family {Palatino Linotype} -size 12")
    Label3.configure(text="'Rate")

    Label3_5 = tk.Label(top)
    Label3_5.grid(row=6,column=0,pady=20,sticky="w")
    Label3_5.configure(font="-family {Palatino Linotype} -size 12")
    Label3_5.configure(text="Discount")


    v=[]
    mycursor.execute("select pname2 from stock")
    for i in mycursor:
        if i not in v:
            v.append(i)
    
    c2= tt.Combobox(top,value=v,width=21,textvariable=pname4,state='readonly')
    c2.set("Choose the Product")
    c2.grid(row=2,column=1,pady=20,padx=20,sticky="w")
    c2.configure(font="-family {Palatino Linotype} -size 14")

    Entry2 = tk.Entry(top,width=28, textvariable=Quantity1)
    Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
    Entry2.configure(font="-family {Palatino Linotype} -size 12")

    f=[]
    mycursor.execute("select measure from stock")
    for i in mycursor:
        if i not in f:
            f.append(i)
    
    c3= tt.Combobox(top,value=f,width=21,textvariable=Measurement1,state='readonly')
    c3.set("Choose the Measurement")
    c3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
    c3.configure(font="-family {Palatino Linotype} -size 14")

    Entry5 = tk.Entry(top,width=28, textvariable=rate)
    Entry5.grid(row=5,column=1,pady=20,padx=20,sticky="w")
    Entry5.configure(font="-family {Palatino Linotype} -size 12")
    
    Entry6 = tk.Entry(top,width=28, textvariable=discount)
    Entry6.grid(row=6,column=1,pady=20,padx=20,sticky="w")
    Entry6.configure(font="-family {Palatino Linotype} -size 12")

    
    button6=tk.Button(top,text="ADD",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:saveadd3(top))
    button6.grid(row=9,column=1,pady=20)

    button7=tk.Button(top,text="CANCEL",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=onclosing)
    button7.grid(row=9,column=0,pady=20)

def saveadd3(tp):
    global pname4,Quantity1,Measurement1,rate,discount
    
    try:
        if (pname4.get() == "" or Quantity1.get() == "" or Measurement1.get() == "" or rate.get() == ""):
            clear3()
            pname4.set("Please fill all the fields correctly!")
        else:
            list1=[]
            if(pname4.get()==""):
                pname4.set("Please fill all the fields correctly!")
            else:
                list1.append(pname4.get())
            if (Quantity1.get() == ""):
                Quantity1.set("Please fill all the fields correctly!")
            else:
                f=[]
                num2=Quantity1.get()
                num1=pname4.get()
                mycursor.execute("select quantity from stock where pname2=?",(num1,))
                for i in mycursor:
                    f.append(int(i[0]))
                if(num2.isalpha()==True):
                    Quantity1.set("Please fill all the fields correctly!")
                elif(int(num2)>f[0]):
                    Quantity1.set("You don't have enough quantity to sale!")
                else:
                    list1.append(num2)
            if (Measurement1.get() == ""):
                Measurement1.set("Please fill all the fields correctly!")
            else:
                list1.append(Measurement1.get())
            if (rate.get() == ""):
                rate.set("Please fill all the fields correctly!")
            else:
                list1.append(rate.get())
            if (discount.get() == ""):
                list1.append('0')
            else:
                num2=discount.get()
                if(num2.isalpha()==True):
                    discount.set("Please fill all the fields correctly!")
                else:
                    list1.append(num2)

            h=Quantity1.get()
            g=rate.get()
            i=discount.get()
            m=int(h)*int(g)
            k=m*(int(i)/100)
            n=m-k
            list1.append(n)
            tp.withdraw()
            
            mycursor.execute("INSERT INTO sale3 VALUES(?,?,?,?,?,?)",(list1[0],list1[1],list1[2],list1[3],list1[4],str(n)))
            conn.commit()
            clear3()
            
            listBox5.delete(*listBox5.get_children())
            mycursor.execute("select * from sale3")
            for i in mycursor:
                listBox5.insert("", "end", values=i)
    except:
        pass

    
def Mdd3(top):
    global listBox5,pname4,Quantity1,Measurement1,rate,discount
    selected_items1 = listBox5.selection()
    cur_item1=listBox5.focus()
    k=listBox5.item(cur_item1)["values"]
    if(len(k)==0):
        messagebox.showerror("No Record Selected","Please select a record to Modify")
    else:
        def onclosing():
            clear3()
            top.withdraw()
        
        top.deiconify()
        top.geometry("500x550+0+0")

        pname4=tk.StringVar()
        Quantity1=tk.StringVar()
        Measurement1=tk.StringVar()
        rate=tk.StringVar()
        discount=tk.StringVar()
        
        Label2 = tk.Label(top)
        Label2.grid(row=0,column=1,pady=20,sticky="nw")
        Label2.configure(font="-family {Palatino Linotype} -size 18")
        Label2.configure(text="Record Entery")

        Label2 = tk.Label(top)
        Label2.grid(row=2,column=0,pady=20,sticky="w")
        Label2.configure(font="-family {Palatino Linotype} -size 12")
        Label2.configure(text="Product Name")

        Label2_1 = tk.Label(top)
        Label2_1.grid(row=3,column=0,pady=20,sticky="w")
        Label2_1.configure(font="-family {Palatino Linotype} -size 12")
        Label2_1.configure(text="Quantity")

        Label2_2 = tk.Label(top)
        Label2_2.grid(row=4,column=0,pady=20,sticky="w")
        Label2_2.configure(font="-family {Palatino Linotype} -size 12")
        Label2_2.configure(text="Measurement")
        
        Label3 = tk.Label(top)
        Label3.grid(row=5,column=0,pady=20,sticky="w")
        Label3.configure(font="-family {Palatino Linotype} -size 12")
        Label3.configure(text="'Rate")

        Label3_5 = tk.Label(top)
        Label3_5.grid(row=6,column=0,pady=20,sticky="w")
        Label3_5.configure(font="-family {Palatino Linotype} -size 12")
        Label3_5.configure(text="Discount")


        v=[]
        mycursor.execute("select pname2 from stock")
        for i in mycursor:
            v.append(i)
        
        c2= tt.Combobox(top,value=v,width=21,textvariable=pname4,state='readonly')
        c2.set("Choose the Product")
        c2.grid(row=2,column=1,pady=20,padx=20,sticky="w")
        c2.configure(font="-family {Palatino Linotype} -size 14")

        Entry2 = tk.Entry(top,width=28, textvariable=Quantity1)
        Entry2.grid(row=3,column=1,pady=20,padx=20,sticky="w")
        Entry2.configure(font="-family {Palatino Linotype} -size 12")

        f=[]
        mycursor.execute("select measure from stock")
        for i in mycursor:
            f.append(i)
        
        c3= tt.Combobox(top,value=f,width=21,textvariable=Measurement1,state='readonly')
        c3.set("Choose the Measurement")
        c3.grid(row=4,column=1,pady=20,padx=20,sticky="w")
        c3.configure(font="-family {Palatino Linotype} -size 14")

        Entry5 = tk.Entry(top,width=28, textvariable=rate)
        Entry5.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        Entry5.configure(font="-family {Palatino Linotype} -size 12")
        
        Entry6 = tk.Entry(top,width=28, textvariable=discount)
        Entry6.grid(row=6,column=1,pady=20,padx=20,sticky="w")
        Entry6.configure(font="-family {Palatino Linotype} -size 12")

        
        button6=tk.Button(top,text="MODIFY",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:savemodi3(top,k))
        button6.grid(row=9,column=1,pady=20)

        button7=tk.Button(top,text="CANCEL",padx=60,pady=10,bd=4,font=("arial",10,"bold"),command=lambda:onclosing)
        button7.grid(row=9,column=0,pady=20)

        pname4.set(k[0])
        Quantity1.set(k[1])
        Measurement1.set(k[2])
        rate.set(k[3])
        discount.set(k[4])        

def savemodi3(top,k3):
    global listBox5,pname4,Quantity1,Measurement1,rate,discount
    try:
        if (pname4.get() == "" or Quantity1.get() == "" or Measurement1.get() == "" or rate.get() == ""):
            clear3()
            pname4.set("Please fill all the fields correctly!")
        else:
            list1=[]
            if(pname4.get()==""):
                pname4.set("Please fill all the fields correctly!")
            else:
                list1.append(pname4.get())
            if (Quantity1.get() == ""):
                Quantity1.set("Please fill all the fields correctly!")
            else:
                f=[]
                num2=Quantity1.get()
                num1=pname4.get()
                mycursor.execute("select quantity from stock where pname2=?",(num1,))
                for i in mycursor:
                    f.append(int(i[0]))
                if(num2.isalpha()==True):
                    Quantity1.set("Please fill all the fields correctly!")
                elif(int(num2)>f[0]):
                    Quantity1.set("You don't have enough quantity to sale!")
                else:
                    list1.append(num2)
            if (Measurement1.get() == ""):
                Measurement1.set("Please fill all the fields correctly!")
            else:
                list1.append(Measurement1.get())
            if (rate.get() == ""):
                rate.set("Please fill all the fields correctly!")
            else:
                list1.append(rate.get())
            if (discount.get() == ""):
                list1.append('0')
            else:
                num2=discount.get()
                if(num2.isalpha()==True):
                    discount.set("Please fill all the fields correctly!")
                else:
                    list1.append(num2)

            h=Quantity1.get()
            g=rate.get()
            i=discount.get()
            m=int(h)*int(g)
            k=m*(int(i)/100)
            n=m-k
            list1.append(n)
            top.withdraw()
            
            mycursor.execute("UPDATE sale3 SET pname4=?,Quantity1=?,Measurement1=?,rate=?,discount=?,Price1=? WHERE pname4=? AND Quantity1=? AND Measurement1=? AND rate=? AND discount=? AND Price1=?",(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],k3[0],k3[1],k3[2],k3[3],k3[4],k3[5]))
            conn.commit()
                    
            listBox5.delete(*listBox5.get_children())
            mycursor.execute("select * from sale3 ")
            for i in mycursor:
                listBox5.insert("", "end", values=i)
    except:
        pass
def delete_btn3():
    try:
        global listBox5
        MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning")
        if MsgBox == "yes":
            selected_items = listBox5.selection()
            cur_item=listBox5.focus()
            k=listBox5.item(cur_item)["values"]
            mycursor.execute("DELETE FROM sale3 WHERE pname4=? AND Quantity1=? AND Measurement1=? AND rate=? AND discount=? AND Price1=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4]),str(k[5])))
            conn.commit()
            for selected_item in selected_items:
                listBox5.delete(selected_item)
            mycursor.execute("select count(*) from sale3")
            
        else:
            pass
    except:
        pass

def delete_btn4():
    try:
        global listbox3
        MsgBox= tk.messagebox.askquestion("Delete Record","Are you sure you want to delete current Record",icon="warning")
        if MsgBox == "yes":
            selected_items = listBox3.selection()
            cur_item=listBox3.focus()
            k=listBox3.item(cur_item)["values"]
            mycursor.execute("DELETE FROM sale2 WHERE ino1=? AND cname=? AND cadd=? AND dob1=? AND nop=? AND tq=? AND td=? AND ta=?",(str(k[0]),str(k[1]),str(k[2]),str(k[3]),str(k[4]),str(k[5]),str(k[6]),str(k[7])))
            mycursor.execute("DELETE FROM sale WHERE ino=? AND dob=?",(str(k[0]),str(k[3])))
            listBox3.delete(*listBox3.get_children())
            mycursor.execute("select * from sale2 order by dob1 desc")             
            for i in mycursor:
                listBox3.insert("", "end", values=i)
            conn.commit()
        else:
            pass
    except:
        pass
        
def saveandcalc():
    try:
        global listBox5,r6,r7,r9,r10,r12,r11,listBox3,z
        selected_items1 = listBox5.selection()
        cur_item1=listBox5.focus()
        k=listBox5.item(cur_item1)["values"]
        if(len(k)==0):
            messagebox.showerror("No Record Selected","Please select a record to make sure you have items to make bill")
        else:
            if r7.get()=="" or r12.get()=="" or r11.get()=="" :
                messagebox.showerror("Bill Already Exist","Please check the bill no and date carefully!")
            
            else:
                list1=[]
                list2=[]
                j1=[]
                mycursor.execute("select * from sale2 where ino1=? AND dob1=?",(r7.get(),r6.get_date()))
                for i in mycursor:
                    j1.append(i[0])
                
                if (len(j1)!=0):
                    r7.set("Please fill all the fields correctly!")
                else:
                
                    if(r7.get()==""):
                        r7.set("Please fill all the fields correctly!")
                    else:
                        list1.append(r7.get())
                        list2.append(r7.get())
                    if(r11.get()==""):
                        r11.set("Please fill all the fields correctly!")
                    else:
                        list2.append(r11.get())
                    if(r12.get()==""):
                        r12.set("Please fill all the fields correctly!")
                    else:
                        list2.append(r12.get())
                    if (r6.get() == ""):
                        r6.set("Please fill all the fields correctly!")
                    else:
                         try:
                            da=r6.get_date()
                            list1.append(da)
                            list2.append(da)
                         except:
                            pass
                    a=[]
                    mycursor.execute("select count(pname4) from sale3")
                    for i in mycursor:
                        a.append(i)
                    if(len(a)==0):
                        pass
                    else:
                        list2.append(a[0])
                    a1=[]
                    mycursor.execute("select SUM(Quantity1) from sale3")
                    for i in mycursor:
                        a1.append(i)
                    if(len(a1)==0):
                        pass
                    else:
                        list2.append(a1[0])
                    a2=[]
                    mycursor.execute("select SUM(Price1) from sale3")
                    for i in mycursor:
                        a2.append(i)
                    if(len(a2)==0):
                        pass
                    else:
                        list2.append(a2[0])

                    if (r9.get()==""):
                        r9.set("0.0")
                        
                    else:
                        num2=r9.get()
                        if(num2.isalpha()==True):
                            r9.set("Please fill all the fields correctly!")
                        else:
                            pass
                    l1=[]
                    mycursor.execute("select SUM(Price1) from sale3")
                    for i in mycursor:
                        l1.append(i[0])
                    g=float(r9.get())
                    z=float(l1[0])+g
                    if z==None:
                        r10.set("0.0")
                        list2.append(str(0.0))
                    else:
                        r10.set(z)
                        list2.append(str(z))
                    for l in listBox5.get_children():
                        o=[]
                        m=listBox5.item(l)["values"]
                        for i in m:
                            d=str(i)
                            o.append(d)
                        list1.append(o)
                    
                    if("Please fill all the fields correctly!" not in list1 and "Please fill all the fields correctly!" not in list2):
                        for i in range(2,len(list1)):
                            mycursor.execute("INSERT INTO sale VALUES(?,?,?,?,?,?,?,?)",(list1[0],list1[1],list1[i][0],list1[i][1],list1[i][2],list1[i][3],list1[i][4],list1[i][5]))
                            mycursor.execute("UPDATE stock SET quantity=quantity-? WHERE pname2=? AND measure=?",(list1[i][1],list1[i][0],list1[i][2]))
                        
                        mycursor.execute("INSERT INTO sale2 VALUES(?,?,?,?,?,?,?,?)",(str(list2[0]),str(list2[1]),str(list2[2]),str(list2[3]),str(list2[4][0]),str(list2[5][0]),str(list2[6][0]),str(list2[7])))    
                        conn.commit()
                        listBox3.delete(*listBox3.get_children())
                        mycursor.execute("select * from sale2 order by dob1 desc")
                        for i in mycursor:
                            listBox3.insert("", "end", values=i)
                        
                        clear3()
    except:
        pass

def search_btn1():
    global listBox3,option3,r3
    _entry = r3.get()
    _option = option3.get()
    
    if (_option == 'Invoice No.'):
        listBox3.delete(*listBox3.get_children())
        mycursor.execute('select * from sale2 where ino1 like "%{0}%"'.format(_entry))
        for i in mycursor:
            listBox3.insert("", "end", values=i)
    elif (_option == 'Customer Name'):
        listBox3.delete(*listBox3.get_children())
        mycursor.execute('select * from sale2 where cname like "%{0}%"'.format(_entry))
        for i in mycursor:
            listBox3.insert("", "end", values=i)
    elif (_option == 'Customer Address'):
        listBox3.delete(*listBox3.get_children())
        mycursor.execute("select * from sale2 where cadd like '%{0}%'".format(_entry))
        for i in mycursor:
            listBox3.insert("", "end", values=i)
    elif (_option == 'Date of Bill(dd-mm-yy)'):
        listBox3.delete(*listBox3.get_children())
        mycursor.execute('select * from sale2 where dob1 like "%{0}%"'.format(_entry))
        for i in mycursor:
            listBox3.insert("", "end", values=i)
    elif (_option == 'No. Of Product'):
        listBox3.delete(*listBox3.get_children())
        mycursor.execute('select * from sale2 where nop like "%{0}%"'.format(_entry))
        for i in mycursor:
            listBox3.insert("", "end", values=i)
    elif (_option == 'Total Quantity'):
        listBox3.delete(*listBox3.get_children())
        mycursor.execute('select * from sale2 where tq like "%{0}%"'.format(_entry))
        for i in mycursor:
            listBox3.insert("", "end", values=i)
    elif (_option == 'Total Price'):
        listBox3.delete(*listBox3.get_children())
        mycursor.execute('select * from sale2 where td like "%{0}%"'.format(_entry))
        for i in mycursor:
            listBox3.insert("", "end", values=i)
    elif (_option == 'Final Amount'):
        listBox3.delete(*listBox3.get_children())
        mycursor.execute('select * from sale2 where ta like "%{0}%"'.format(_entry))
        for i in mycursor:
            listBox3.insert("", "end", values=i)
    elif (_option == "All Records"):
        listBox3.delete(*listBox3.get_children())
        mycursor.execute("select * from sale2 order by dob1 desc")
        for i in mycursor:
            listBox3.insert("", "end", values=i)
    else:
        option.set("Choose Category Correctly!")


def gen_btn4():
    try:
        global listBox5,r12,r11,r6,r7,r10
        files=[("Pdf Document","*.pdf")]
        fp= tk.filedialog.asksaveasfile(filetype = files,mode="w",defaultextension=".pdf")
        fw= open("temp.txt","w")
        if fp is None:
            messagebox.showerror("Invalid file Name","Please enter valid Name")
        else:   
            l1=[]
            h=()
            for l in listBox5.get_children():
                d=[]
                m=listBox5.item(l)["values"]
                for i in m:
                    b=str(i)
                    r=b.replace(" ","\n")
                    d.append(r)
                h=tuple(d)
                l1.append(h)
            st="\n"
            st+="CUSTOMER NAME-Ph.NO :"
            st+=r11.get()+"\n"
            st+="CUSTOMER ADDRESS :"
            st+=r12.get()+"\n"
            st+="DATE OF BILL :"
            st+=r6.get()+"\t\t\t"
            st+="INVOICE NO : "
            st+=r7.get()+"\n"
            head=['PRODUCT NAME' ,'QUANTITY','MEASUREMENT','RATE','DISCOUNT %','TOTAL AMOUNT']
            st+=tabulate(l1,headers=head,tablefmt="grid")
            st+="\n\n"
            st+="FINAL AMOUNT : "
            st+=r10.get()
            fw.write(st)
            fw.close()
            pdf=FPDF()
            pdf.add_page()
            pdf.set_font("Courier",style="B",size=8.5)
            pdf.set_margins(0,0,0)
            f=open("temp.txt","r")
            for x in f:
                pdf.cell(-1,5,txt = x, ln = 1)
            pdf.output(fp.name)
            f.close()
            os.remove("temp.txt")
            
    except PermissionError:
        messagebox.showerror("Error Message","Please try again after closing the document you want to overwrite")
    except:
        pass
            
def gen_btn5(w):
    try:
        global listBox4,r5,r4
        files=[("Pdf Document","*.pdf")]
        fp= tk.filedialog.asksaveasfile(filetype = files,mode="w",defaultextension=".pdf")
        fw= open("temp.txt","w")
        if fp is None:
            messagebox.showerror("Invalid file Name","Please enter valid Name")
        else:   
            l1=[]
            h=()
            for l in listBox4.get_children():
                d=[]
                m=listBox4.item(l)["values"]
                for i in m:
                    b=str(i)
                    r=b.replace(" ","\n")
                    d.append(r)
                h=tuple(d)
                l1.append(h)
            st="\n"
            st+="CUSTOMER NAME-Ph.NO :"
            st+=w[1]+"\n"
            st+="CUSTOMER ADDRESS :"
            st+=w[2]+"\n"
            st+="DATE OF BILL :"
            st+=r4.get()+"\t\t\t"
            st+="INVOICE NO : "
            st+=r5.get()+"\n"
            head=['PRODUCT NAME' ,'QUANTITY','MEASUREMENT','RATE','DISCOUNT %','TOTAL AMOUNT']
            st+=tabulate(l1,headers=head,tablefmt="grid")
            st+="\n\n"
            st+="FINAL AMOUNT : "
            st+=str(w[7])
            fw.write(st)
            fw.close()
            pdf=FPDF()
            pdf.add_page()
            pdf.set_font("Courier",style="B",size=8.5)
            pdf.set_margins(0,0,0)
            f=open("temp.txt","r")
            for x in f:
                pdf.cell(-1,5,txt = x, ln = 1)
            pdf.output(fp.name)
            f.close()
            os.remove("temp.txt")
        
    except PermissionError:
        messagebox.showerror("Error Message","Please try again after closing the document you want to overwrite")
    except:
        pass

def gen_btn6():
    try:
        global listBox3
        files=[("Pdf Document","*.pdf")]
        fp= tk.filedialog.asksaveasfile(filetype = files,mode="w",defaultextension=".pdf")
        fw= open("temp.txt","w")
        if fp is None:
            messagebox.showerror("Invalid file Name","Please enter valid Name")
        else:   
            l1=[]
            h=()
            for l in listBox3.get_children():
                d=[]
                m=listBox3.item(l)["values"]
                for i in m:
                    b=str(i)
                    r=b.replace(" ","\n")
                    d.append(r)
                h=tuple(d)
                l1.append(h)
            st="\n"
            head=['INVOICE\nNO.','CUSTUMOR\nNAME','CUSTOMER\nADDRESS','DATE\nOF BILL','No. OF\nPRODUCT','TOTAL\nQUANTITY','TOTAL\nPRICE','FINAL\nAMOUNT']
            st+=tabulate(l1,headers=head,tablefmt="grid")
            fw.write(st)
            fw.close()
            pdf=FPDF()
            pdf.add_page()
            pdf.set_font("Courier",style="B",size=8.5)
            pdf.set_margins(0,0,0)
            f=open("temp.txt","r")
            for x in f:
                pdf.cell(-1,5,txt = x, ln = 1)
            pdf.output(fp.name)
            f.close()
            os.remove("temp.txt")
    except PermissionError:
        messagebox.showerror("Error Message","Please try again after closing the document you want to overwrite")
    except:
        pass
        
Mp.withdraw()
Ms.withdraw()
Ip.withdraw()
Sa.withdraw()
button=tk.Button(cframe,text="SUBMIT",padx=10,pady=5,bd=4,font=("arial",10,"bold"),command=lambda:Open())
button.grid(pady=10,padx=5,row=6,column=0)

root.mainloop()
