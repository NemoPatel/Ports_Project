import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as sql
from tkinter import messagebox
from tkinter import ttk



def customer():
    start_screen.destroy()
    cust = tk.Tk()
    cust.title("Arstotzka Shipment Services")
    cust.iconbitmap('arst.ico')
    cust.geometry("624x600")
    cust.configure(bg="black")

    #functions

    def c_submit():
        name     = NameE.get()
        company  = CompanyE.get()
        gtype    = gt.get()     
        wgood    = Weight_goodE.get()
        dest     = dt.get()
        desc     = DescriptionE.get(1.0, END)
        
        
        if len(name)<=0:
            messagebox.showwarning("ALERT!","Please Enter Name")
        elif len(company)<=0:
            messagebox.showwarning("ALERT!","Please Enter Company Name")
        elif gtype=="Select":
            messagebox.showwarning("ALERT!","Please Select Good Type")
        elif len(wgood)<=0:
            messagebox.showwarning("ALERT!","Please Enter Weight of Good")
        elif wgood.isdecimal()==False:
            messagebox.showwarning("ALERT!","Please Enter Weight of Good in Numericals")
        elif dest=="Select":
            messagebox.showwarning("ALERT!","Please Select Destination")
        elif len(desc)<=1:
            messagebox.showwarning("ALERT!","Please Enter Description")
        elif len(desc)>=1001:
            messagebox.showwarning("ALERT!","Description should be less than 1000 characters")

        else:
            cursor.execute("insert into customer value('%s','%s','%s','%s','%s','%s')"%(name, company, gtype, wgood, dest, desc))
            db.commit()
            db.close
        
            NameE.delete(0, END)
            CompanyE.delete(0, END)
            gt.set("Select")
            Weight_goodE.delete(0, END)
            dt.set("Select")
            DescriptionE.delete(1.0, END)

            messagebox.showinfo("Success!","Your order has been Succesfully submitted")
            cust.destroy()

    #cust stuff
    global img
    img       = ImageTk.PhotoImage(Image.open("Arstotzka top level.jpg"))
    img_label = Label(cust, image=img)
    w_label   = Label(cust, text="Arstotzka Customer Shipment Service", font=("Gotham Medium","15"))

    img_label.grid   (row=1, column=0, pady=5)
    w_label.grid     (row=2, column=0, pady=5)
    
    #Frames
    entry_frame = LabelFrame(cust, text="Details", padx=50, pady=25, borderwidth=5, bg= "LightSteelBlue1")
    entry_frame.grid(row=3, column=0)

    button_frame = LabelFrame(cust, padx=25, pady=10, borderwidth=5, bg= "LightSteelBlue1")
    button_frame.grid(row=4, column=0)
    
    #Variables
    gt = StringVar()
    gt.set("Select")
    
    dt = StringVar()
    dt.set("Select")

    #Buttom frame stuff
    submit = Button(button_frame, text="Submit", command = c_submit, padx=75, bd=5, bg="DarkSeaGreen4", fg="white")
    submit.grid      (row=0, column=0, sticky=W+E)

    #Entry frame stuff
    Name        = Label(entry_frame, text="Name", bg= "LightSteelBlue1")
    Company     = Label(entry_frame, text="Company", bg= "LightSteelBlue1")
    Good_type   = Label(entry_frame, text="Good Type", bg= "LightSteelBlue1")
    Weight_good = Label(entry_frame, text="Weight of Good (in Tonne)", bg= "LightSteelBlue1")
    Destination = Label(entry_frame, text="Destination", bg= "LightSteelBlue1")
    Description = Label(entry_frame, text="Description of Good", bg= "LightSteelBlue1")

    NameE        = Entry(entry_frame)
    CompanyE     = Entry(entry_frame)
    Good_typeE   = OptionMenu(entry_frame, gt,"Fragile", "Flammable", "Organic", "Metal")
    Weight_goodE = Entry(entry_frame)
    DestinationE = OptionMenu(entry_frame, dt, "India", "USA", "UK", "Japan")
    DescriptionE = Text(entry_frame, width=25, height=5)

    Name.grid        (row=1, column=0, pady=5, sticky=W)
    Company.grid     (row=2, column=0, pady=5, sticky=W)
    Good_type.grid   (row=3, column=0, pady=5, sticky=W)
    Weight_good.grid (row=4, column=0, pady=5, sticky=W)
    Destination.grid (row=5, column=0, pady=5, sticky=W)
    Description.grid (row=6, column=0, pady=5, sticky=W)
    
    NameE.grid       (row=1, column=1, pady=5, sticky=W+E)
    CompanyE.grid    (row=2, column=1, pady=5, sticky=W+E)
    Good_typeE.grid  (row=3, column=1, pady=5, sticky=W+E)
    Weight_goodE.grid(row=4, column=1, pady=5, sticky=W+E)
    DestinationE.grid(row=5, column=1, pady=5, sticky=W+E)
    DescriptionE.grid(row=6, column=1, pady=5)
    

def employee():
    start_screen.destroy()
    global emp
    emp = tk.Tk()
    emp.title("Arstotzka Shipment Management")
    emp.iconbitmap('arst.ico')
    emp.geometry("624x500")
        

    def login():
        ID_raw   = User_IDE.get()
        global username
        username = UsernameE.get()
        password = PasswordE.get()
        
        db       = sql.connect(
        host     = "localhost",
        user     = "your user",
        passwd   = "your password",
        database ="your database")
        cursor   = db.cursor()

        cursor.execute("select Id_no from employee;")
        id_1=cursor.fetchall()    

        if len(ID_raw)<=0:
            messagebox.showwarning("ALERT!","Please Enter ID Number")
        elif ID_raw.isnumeric()==False:
            messagebox.showwarning("ALERT!","Please Enter ID Number in numericals")
        elif len(username)<=0:
            messagebox.showwarning("ALERT!","Please Enter Username")
        elif len(password)<=0:
            messagebox.showwarning("ALERT!","Please Enter Password")
        else:
            ID = int(ID_raw)
            ID_list=[]
            for i in id_1:
                for l in i:
                    ID_list.append(l)

            if ID in ID_list:                   
                cursor.execute("select Username from employee where Id_no='%s';"%(ID))
                username_1=cursor.fetchall()
                username_2=username_1[0]
                username_final=username_2[0]
                    
                cursor.execute("select Password from employee where Id_no='%s';"%(ID))
                password_1=cursor.fetchall()
                password_2=password_1[0]
                password_final=password_2[0]

                if username==username_final and password==password_final:
                    management()
                else:
                    messagebox.showwarning("ALERT!","Invalid Credentials")
            else:
                messagebox.showwarning("ALERT!","Invalid Credentials")
                            
                    

    #emp stuff
    global img
    img       = ImageTk.PhotoImage(Image.open("Arstotzka top level.jpg"))
    img_label = Label(emp, image=img)
    w_label   = Label(emp, text="Arstotzka Shipment Management", font=("Gotham Medium","15"))

    img_label.grid   (row=1, column=0, pady=5)
    w_label.grid     (row=2, column=0, pady=5)

    #Frames
    entry_frame = LabelFrame(emp, text="Login", padx=50, pady=25, borderwidth=5)
    entry_frame.grid(row=3, column=0)

    button_frame = LabelFrame(emp, padx=25, pady=10, borderwidth=5)
    button_frame.grid(row=4, column=0)
    
    #Entry frame Stuff
    User_ID     = Label(entry_frame, text="User ID")
    Username    = Label(entry_frame, text="Username")
    Password    = Label(entry_frame, text="Password")

    User_IDE    = Entry(entry_frame)
    UsernameE   = Entry(entry_frame)
    PasswordE   = Entry(entry_frame, show="*")

    User_ID.grid    (row=1, column=0, pady=5, sticky=W)
    Username.grid   (row=2, column=0, pady=5, sticky=W)
    Password.grid   (row=3, column=0, pady=5, sticky=W)

    User_IDE.grid   (row=1, column=1, pady=5, sticky=W+E)
    UsernameE.grid  (row=2, column=1, pady=5, sticky=W+E)
    PasswordE.grid  (row=3, column=1, pady=5, sticky=W+E)

    #Button frame stuff
    login = Button(button_frame, text="Login", command = login, padx=97)
    login.grid     (row=0, column=0, sticky=W+E)

def management():
    emp.destroy()
    global mag
    mag = tk.Tk()
    mag.title("Arstotzka Shipment Management")
    mag.iconbitmap('arst.ico')
    mag.geometry("624x500")

    #mag stuff
    global img
    img       = ImageTk.PhotoImage(Image.open("Arstotzka top level.jpg"))
    img_label = Label(mag, image=img)
    w_label   = Label(mag, text="Welcome Comrade "+username, font=("Gotham Medium","15"))

    img_label.grid   (row=1, column=0, pady=5)
    w_label.grid     (row=2, column=0, pady=5)

    #Frames
    basic_frame = LabelFrame(mag, text="Arstotzka Shipment Manager", borderwidth=5, padx=20, pady=20)

    basic_frame.grid (row=3, column=0, pady=5)

    #basic frame stuff
    order_r = Button (basic_frame, text="Order Requests",  command = order_request,   padx=100, pady=10, bd=5)
    rs      = Button (basic_frame, text="Review Shipment", command = review_shipment, padx=100, pady=10, bd=5)
    
    order_r.grid (row=0, column=0, pady=10, sticky=W+E)
    rs.grid      (row=1, column=0, pady=10, sticky=W+E)
    
def order_request():
    or_w = Toplevel()
    or_w.title("Arstotzka Shipment Management")
    or_w.iconbitmap('arst.ico')
    or_w.geometry("624x500")

    main_frame = Frame(or_w)
    main_frame.pack(fill= BOTH, expand= 1)

    main_canvas = Canvas(main_frame)
    main_canvas.pack(side= LEFT, fill= BOTH, expand = 1)


    main_scroll = ttk.Scrollbar(main_frame, orient= VERTICAL, command= main_canvas.yview)
    main_scroll.pack(side= RIGHT, fill= Y)


    main_canvas.configure(yscrollcommand = main_scroll.set)
    main_canvas.bind ("<Configure>", lambda e: main_canvas.configure(scrollregion= main_canvas.bbox('all')))

    sec_frame = Frame(main_canvas)
    main_canvas.create_window((0,0), window= sec_frame, anchor="nw")
    

    global img_sub
    img_sub       = ImageTk.PhotoImage(Image.open("Arstotzka sub top level.jpg"))
    img_label = Label(sec_frame, image=img_sub)
    w_label   = Label(sec_frame, text="SHIPMENTS", font=("Gotham Medium","15"))

    img_label.grid   (row=1, column=0, pady=5)
    w_label.grid     (row=2, column=0, pady=5)

    cursor.execute("select * from customer")

    global dataS
    dataS = cursor.fetchall()

    if dataS==[]:
        print("NO NEW ORDERS")
        frame = LabelFrame(sec_frame, padx= 2, pady= 5, fg= "yellow", bg= "grey", font=("Times New Roman", "30"), borderwidth= 3)
        frame.grid(padx = 5, pady= 5)

        catg = Label (frame, text="NO NEW ORDERS", padx=5, pady=5, font=("Times New Roman", "30"))
        catg.grid   (row= 0, column= 0, padx= 5,pady= 5)

    else:
        rowS = dataS[0]
        var = 1
        
        for rowS in dataS:
            frame = LabelFrame(sec_frame, text= rowS[1], padx= 2, pady= 5, fg= "yellow", bg= "grey", font=("Times New Roman", "12"), borderwidth= 3)

            frame.grid(padx= 5,pady= 5)
        
            catg   = Label (frame, text="Category:\n"        + rowS[2],           padx=5, pady=5, font=("Times New Roman", "10"))
            dest   = Label (frame, text="Location:\n"        + rowS[4],           padx=5, pady=5, font=("Times New Roman", "10"))
            weight = Label (frame, text="Weight:\n"          + str(rowS[3])+"T",  padx=5, pady=5, font=("Times New Roman", "10"))
            Cname  = Label (frame, text="Order Placed By:\n" + rowS[0],           padx=5, pady=5, font=("Times New Roman", "10"))
            desc   = Label (frame, text="DESCRIPTION:\n"     + rowS[5],           padx=5, pady=5, font=("Times New Roman", "10"))
            ind    = Label (frame, text= "INDEX: "+str(var), padx= 5)

            catg.grid   (row= 0, column= 0, padx= 5,pady= 5)
            dest.grid   (row= 0, column= 1, padx= 5,pady= 5)
            weight.grid (row= 0, column= 2, padx= 5,pady= 5)
            Cname.grid  (row= 0, column= 3, padx= 5,pady= 5)
            desc.grid   (row= 0, column= 4, padx= 5,pady= 2)
            ind.grid    (row= 1, padx= 5,pady= 2)

            var+=1

        accept_frame = LabelFrame(sec_frame, text="Specify Index of orders to be Accepted", padx= 2, pady= 5, fg= "yellow", bg= "grey", font=("Times New Roman", "12"), borderwidth= 3)
        accept_frame.grid(padx= 5,pady= 5)

        global accept_entry
        accept_entry = Entry(accept_frame)
        accept_entry.grid (row = 0, column = 0, pady=5)
    
        def accep_submit():
            global dataS, accept_entry
        
            accepted_orders = accept_entry.get()
        
            for i in accepted_orders:
                k = int(i)
                approved = dataS[k-1]
                print(approved)

                cursor.execute("insert into approved values('%s','%s','%s',%s,'%s','%s')"%(approved[0],approved[1],approved[2],approved[3],approved[4],approved[5]))
                db.commit()

            cursor.execute("delete from customer")
            db.commit()
    
        butt = Button(accept_frame, text="Submit", command = accep_submit, padx=75, bd=5, bg="DarkSeaGreen4", fg="white")
        butt.grid      (row = 1, column=0, sticky=W+E)

def review_shipment():
    rs_w = Toplevel()
    rs_w.title("Arstotzka Shipment Management")
    rs_w.iconbitmap('arst.ico')
    rs_w.geometry("624x500")

    

    cursor.execute("select * from approved")
    dataS= cursor.fetchall()

    rowS= dataS[1]

    main_frame= Frame(rs_w)
    main_frame.pack(fill= BOTH, expand= 1)

    main_canvas= Canvas(main_frame)
    main_canvas.pack(side= LEFT, fill= BOTH, expand= 1)


    main_scroll= ttk.Scrollbar(main_frame, orient= VERTICAL, command= main_canvas.yview)
    main_scroll.pack(side= RIGHT, fill= Y)


    main_canvas.configure(yscrollcommand= main_scroll.set)
    main_canvas.bind("<Configure>", lambda e: main_canvas.configure(scrollregion= main_canvas.bbox('all')))

    sec_frame= Frame(main_canvas)
    main_canvas.create_window((0,0), window= sec_frame, anchor="nw")

    global img_sub
    img_sub   = ImageTk.PhotoImage(Image.open("Arstotzka sub top level.jpg"))
    img_label = Label(sec_frame, image=img_sub)
    w_label   = Label(sec_frame, text="SHIPMENTS", font=("Gotham Medium","15"))

    img_label.grid   (row=1, column=0, pady=5)
    w_label.grid     (row=2, column=0, pady=5)

    for rowS in dataS:
        frame= LabelFrame(sec_frame, text= rowS[1], padx= 2, pady= 5, fg= "yellow", bg= "grey", font=("Times New Roman", "12"), borderwidth= 3)
        frame.grid( padx= 5,pady= 5)
        
        catg   = Label(frame, text="Category:\n"        + rowS[2],           padx=5, pady=5, font=("Times New Roman", "10"))
        dest   = Label(frame, text="Location:\n"        + rowS[4],           padx=5, pady=5, font=("Times New Roman", "10"))
        weight = Label(frame, text="Weight:\n"          + str(rowS[3])+" T", padx=5, pady=5, font=("Times New Roman", "10"))
        Cname  = Label(frame, text="Order Placed By:\n" + rowS[0],           padx=5, pady=5, font=("Times New Roman", "10"))
        desc   = Label(frame, text="DESCRIPTION:\n"     + rowS[5],           padx=5, pady=5, font=("Times New Roman", "10"))

        catg.grid   (row= 0, column= 0, padx= 5,pady= 5)
        dest.grid   (row= 0, column= 1, padx= 5,pady= 5)
        weight.grid (row= 0, column= 2, padx= 5,pady= 5)
        Cname.grid  (row= 0, column= 3, padx= 5,pady= 5)
        desc.grid   (row= 0, column= 4, padx= 5,pady= 2)


#START SCREEN
db       = sql.connect(
host     = "localhost",
user     = "your user",
password = "your password",
database ="your database")
cursor   = db.cursor()
        
global start_screen
start_screen = tk.Tk()
start_screen.title("Arstotzka Shipment services")
start_screen.iconbitmap('arst.ico')
start_screen.geometry("600x500")
start_screen.configure(bg="black")

welcome_image = ImageTk.PhotoImage(Image.open("Arstotzka.jpg"))
welcome_label = Label(start_screen, image=welcome_image)
customer_button = Button(start_screen, text="Customer", command=customer, padx=100, pady=10, bg="DarkSeaGreen4", bd=5)
employee_button = Button(start_screen, text="Employee", command=employee, padx=100, pady=10, bg="DarkSeaGreen4", bd=5)

welcome_label.grid(row=1, column=0, pady=10)
customer_button.grid(row=2, column=0, pady=10)
employee_button.grid(row =3, column = 0, pady=10)    

mainloop()
