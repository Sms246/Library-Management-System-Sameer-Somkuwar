# Name: Sameer Somkuwar

from tkinter import ttk
from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1280x720+0+0")

        # ************************************** Variables **************************************

        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address_var = StringVar()
        self.contact_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.laterefine_var = StringVar()
        self.dateoverdue_var = StringVar()

        lbltitle = Label(self.root,text = "LIBRARY MANAGEMENT SYSTEM",bg = "powder blue", fg = "green" ,bd = 20, relief=RIDGE,font=("times new roman",50,"bold"), padx = 2, pady = 6)
        lbltitle.pack(side=TOP,fill = X)

        frame = Frame(self.root,bd = 9, relief=RIDGE,padx = 20,bg = "powder blue")
        frame.place(x=0,y=130,width=1280,height=350)

        # ********************** DATA FRAME LEFT ******************************
        dataFrameLeft = LabelFrame(frame, text = "LIBRARY MEMBERSHIP INFO.",bg = "powder blue", fg = "black" ,bd = 6, relief=RIDGE,font=("times new roman",12,"bold") )
        dataFrameLeft.place(x=0,y=0,width=810,height=320)
        
        lblMember = Label(dataFrameLeft,bg="powder blue",text="Member Type:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember = ttk.Combobox(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.member_var,width=27,state="readonly")
        comMember["value"] = ("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No = Label(dataFrameLeft,bg="powder blue",text="PRN No.:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.prn_var )
        txtPRN_No.grid(row=1,column=1)

        lblROLL_No = Label(dataFrameLeft,bg="powder blue",text="ROLL No.:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblROLL_No.grid(row=2,column=0,sticky=W)
        txtROLL_No = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.id_var)
        txtROLL_No.grid(row=2,column=1)

        lblFirstName = Label(dataFrameLeft,bg="powder blue",text="First Name:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.firstname_var)
        txtFirstName.grid(row=3,column=1)

        lblLastName = Label(dataFrameLeft,bg="powder blue",text="Last Name:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.lastname_var)
        txtLastName.grid(row=4,column=1)

        lblAddress = Label(dataFrameLeft,bg="powder blue",text="Address:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.address_var)
        txtAddress.grid(row=5,column=1)

        lblContact_No = Label(dataFrameLeft,bg="powder blue",text="Contact No.:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblContact_No.grid(row=6,column=0,sticky=W)
        txtContact_No = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.contact_var)
        txtContact_No.grid(row=6,column=1)

        lblBookID = Label(dataFrameLeft,bg="powder blue",text="Book ID:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.bookid_var)
        txtBookID.grid(row=0,column=3)

        lblBookTitle = Label(dataFrameLeft,bg="powder blue",text="Book Title:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.booktitle_var)
        txtBookTitle.grid(row=1,column=3)

        lblAuther = Label(dataFrameLeft,bg="powder blue",text="Auther Name:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.auther_var)
        txtAuther.grid(row=2,column=3)

        lblDataBorrowed = Label(dataFrameLeft,bg="powder blue",text="Data Borrowed:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblDataBorrowed.grid(row=3,column=2,sticky=W)
        txtDataBorrowed = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dateborrowed_var)
        txtDataBorrowed.grid(row=3,column=3)

        lblDataDue = Label(dataFrameLeft,bg="powder blue",text="Due Date:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblDataDue.grid(row=4,column=2,sticky=W)
        txtDataDue = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.datedue_var)
        txtDataDue.grid(row=4,column=3)

        lblDaysOnBook = Label(dataFrameLeft,bg="powder blue",text="Days On Book:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.daysonbook_var)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine = Label(dataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.laterefine_var)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue = Label(dataFrameLeft,bg="powder blue",text="Date Over Due:",font=("times new roman",12,"bold"),padx = 2,pady = 6)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue = Entry(dataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dateoverdue_var)
        txtDateOverDue.grid(row=7,column=3)

        #  ********************* DATA FRAME RIGHT ****************************
        dataFrameRight = LabelFrame(frame, text = "BOOK INFO.",bg = "powder blue", fg = "black" ,bd = 6, relief=RIDGE,font=("times new roman",12,"bold") )
        dataFrameRight.place(x=820,y=0,width=1280-875,height=320)
        
        self.txtBox = Text(dataFrameRight,font=("times new roman",12,"bold"),width=26,height=14,padx=2,pady=5)
        self.txtBox.grid(row=0,column=2)

        listScrollbar = Scrollbar(dataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head First Book','Basics of Python','Python Programming','Basics Concepts of OOP','Fundamentals of Digital Communications',
                 'Cryptography and Network Security','R.D. Sharma','H.C. Verma','Java Programming','Fundamentals of JAVA Programmings',
                 'Computer Networks','Data Structures and Algorithms']

        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if (x == 'Head First Book'):
                self.bookid_var.set("BKID0001")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterefine_var.set("Rs. 50")
                self.dateoverdue_var.set("NO")

            elif (x == 'Basics of Python'):
                self.bookid_var.set("BKID0002")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Baul Cerry")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterefine_var.set("Rs. 150")
                self.dateoverdue_var.set("NO")

            elif (x == 'Python Programming'):
                self.bookid_var.set("BKID0003")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Mary Cerry")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterefine_var.set("Rs. 120")
                self.dateoverdue_var.set("NO")

            elif (x == 'Basics Concepts of OOP'):
                self.bookid_var.set("BKID0004")
                self.booktitle_var.set("OOP Manual")
                self.auther_var.set("E.Balgurusami")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterefine_var.set("Rs. 350")
                self.dateoverdue_var.set("NO")

            elif (x == 'Fundamentals of Digital Communications'):
                self.bookid_var.set("BKID0005")
                self.booktitle_var.set("Digital Communications")
                self.auther_var.set("B.P. Lathi")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterefine_var.set("Rs. 950")
                self.dateoverdue_var.set("NO")

            elif (x == 'Cryptography and Network Security'):
                self.bookid_var.set("BKID0006")
                self.booktitle_var.set("Newtork Security Manual")
                self.auther_var.set("Atul Kahate")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterefine_var.set("Rs. 535")
                self.dateoverdue_var.set("NO")

            elif (x == 'Data Structures and Algorithms'):
                self.bookid_var.set("BKID0007")
                self.booktitle_var.set("DSA Manual")
                self.auther_var.set("James Harly")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterefine_var.set("Rs. 1365")
                self.dateoverdue_var.set("NO")

            elif (x == 'Computer Networks'):
                self.bookid_var.set("BKID0008")
                self.booktitle_var.set("Computer Network Manual")
                self.auther_var.set("William Staline")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterefine_var.set("Rs. 650")
                self.dateoverdue_var.set("NO")

            elif (x == 'Fundamentals of JAVA Programmings'):
                self.bookid_var.set("BKID0009")
                self.booktitle_var.set("Java Manual")
                self.auther_var.set("Mr. Shirude")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterefine_var.set("Rs. 1595")
                self.dateoverdue_var.set("NO")

            elif (x == 'Java Programming'):
                self.bookid_var.set("BKID0010")
                self.booktitle_var.set("Java Manual")
                self.auther_var.set("Mr. Shirude")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterefine_var.set("Rs. 1695")
                self.dateoverdue_var.set("NO")

            elif (x == 'H.C. Verma'):
                self.bookid_var.set("BKID0011")
                self.booktitle_var.set("Physic Manual")
                self.auther_var.set("H.C. Verma")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterefine_var.set("Rs. 650")
                self.dateoverdue_var.set("NO")

            elif (x == 'R.D. Sharma'):
                self.bookid_var.set("BKID0012")
                self.booktitle_var.set("Maths Manual")
                self.auther_var.set("R.D. Sharma")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterefine_var.set("Rs. 800")
                self.dateoverdue_var.set("NO")

        listBox = Listbox(dataFrameRight,font=("times new roman",12,"bold"),width=17,height=14)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=2)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        # ************************ Buttons frames********************

        frameButton = Frame(self.root,bd = 6, relief=RIDGE,padx = 20,bg = "powder blue")
        frameButton.place(x=0,y=480,width=1280,height=50)

        btnAddData = Button(frameButton,command=self.addition_data,text = "Add Data:",font=("times new roman",12,"bold"),width=18,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0,padx=5)

        btnShowData = Button(frameButton,command=self.show_data,text = "Show Data:",font=("times new roman",12,"bold"),width=18,bg="blue",fg="white")
        btnShowData.grid(row=0,column=1,padx=5)

        btnUpdateData = Button(frameButton,command=self.update_data,text = "Update Data:",font=("times new roman",12,"bold"),width=18,bg="blue",fg="white")
        btnUpdateData.grid(row=0,column=2,padx=5)

        btnDeleteData = Button(frameButton,command=self.delete_data,text = "Delete Data:",font=("times new roman",12,"bold"),width=18,bg="blue",fg="white")
        btnDeleteData.grid(row=0,column=3,padx=5)

        btnResetData = Button(frameButton,command=self.reset,text = "Reset Data:",font=("times new roman",12,"bold"),width=18,bg="blue",fg="white")
        btnResetData.grid(row=0,column=4,padx=5)

        btnExit = Button(frameButton,command=self.iExit,text = "Exit:",font=("times new roman",12,"bold"),width=18,bg="blue",fg="white")
        btnExit.grid(row=0,column=5,padx=5)

        # ************************ Information frames********************

        frameDetails = Frame(self.root,bd = 6, relief=RIDGE,padx = 2,bg = "powder blue")
        frameDetails.place(x=0,y=530,width=1280,height=125)

        Table_frame = Frame(frameDetails,bd=6,relief = RIDGE,bg = "powder blue")
        Table_frame.place(x=0,y=0,width = 1250, height = 105)

        xscroll = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame,column=("MemberType","PRNno.","IDno."
                                                ,"FirstName","LastName","Address","ContactNo",
                                                "BookID","BookTitle","Auther","DateBorrowed","DateDue",
                                                "Days","LatereTurnFine","DateOverDue"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("MemberType",text="Member Type")
        self.library_table.heading("PRNno.",text="PRN No.")
        self.library_table.heading("IDno.",text="ID No.")
        self.library_table.heading("FirstName",text="First Name")
        self.library_table.heading("LastName",text="Last Name")
        self.library_table.heading("Address",text="Address")
        self.library_table.heading("ContactNo",text="Contact No.")
        self.library_table.heading("BookID",text="Book ID")
        self.library_table.heading("BookTitle",text="Book Title")
        self.library_table.heading("Auther",text="Auther")
        self.library_table.heading("DateBorrowed",text="Borrowed Date")
        self.library_table.heading("DateDue",text="Due Date")
        self.library_table.heading("Days",text="Days")
        self.library_table.heading("LatereTurnFine",text="Late Turn Fine")
        self.library_table.heading("DateOverDue",text="Date Over Due")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill = BOTH,expand=1)
        
        self.library_table.column("MemberType",width=100)
        self.library_table.column("PRNno.",width=100)
        self.library_table.column("IDno.",width=100)
        self.library_table.column("FirstName",width=100)
        self.library_table.column("LastName",width=100)
        self.library_table.column("Address",width=100)
        self.library_table.column("ContactNo",width=100)
        self.library_table.column("BookID",width=100)
        self.library_table.column("BookTitle",width=100)
        self.library_table.column("Auther",width=100)
        self.library_table.column("DateBorrowed",width=100)
        self.library_table.column("DateDue",width=100)
        self.library_table.column("Days",width=100)
        self.library_table.column("LatereTurnFine",width=100)
        self.library_table.column("DateOverDue",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    # ******************************* Function for Adding the data to the table ************************

    def addition_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', password = 'password', database = 'library_db')
        my_cursor = conn.cursor()
        my_cursor.execute("INSERT INTO library_entries values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address_var.get(),
                                                                                                                self.contact_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.auther_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.laterefine_var.get(),
                                                                                                                self.dateoverdue_var.get()
                                                                                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Entry successful")

    # ****************************** Function for updating the data int the table *****************************************

    def update_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', password = 'password', database = 'library_db')
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE library_entries SET Members=%s,ID=%s,FirstName=%s,LastName=%s,Address=%s,ContactNo.=%s,BookID=%s,BookTitle=%s,Auther=%s,DateBorrowed=%s,DateDue=%s,Days=%s,LatereTurnFine=%s,DateOverDue=%s WHERE PRN_No.=%s",( 
                                                                                                                self.member_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address_var.get(),
                                                                                                                self.contact_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.auther_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.laterefine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                            ) )
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been updated")

    # **************************** Function for getting the data from table and show it in the field ****************************************

    def fetch_data(self):
        conn = mysql.connector.connect(host = 'localhost', username = 'root', password = 'password', database = 'library_db')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library_entries")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event = ""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content["values"]

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address_var.set(row[5]),
        self.contact_var.set(row[6]),
        self.bookid_var.set(row[7]),
        self.booktitle_var.set(row[8]),
        self.auther_var.set(row[9]),
        self.dateborrowed_var.set(row[10]),
        self.datedue_var.set(row[11]),
        self.daysonbook_var.set(row[12]),
        self.laterefine_var.set(row[13]),
        self.dateoverdue_var.set(row[14])

    # ******************************** Show data function for show data button ************************************

    def show_data(self):
        self.txtBox.insert(END,"Member Type:\t\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No.: \t\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No.: \t\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END,"First Name: \t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name: \t\t" + self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address: \t\t" + self.address_var.get() + "\n")
        self.txtBox.insert(END,"Contact No.: \t\t" + self.contact_var.get() + "\n")
        self.txtBox.insert(END,"Book ID: \t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book title: \t\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Auther: \t\t" + self.auther_var.get() + "\n")
        self.txtBox.insert(END,"Date Borrowed: \t\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"Date due: \t\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"Days on book: \t\t" + self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"Late Turn Fine: \t\t" + self.laterefine_var.get() + "\n")
        self.txtBox.insert(END,"Date over due: \t\t" + self.dateoverdue_var.get() + "\n")

    # ********************************** Reset function for reset button **********************************

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address_var.set(""),
        self.contact_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.laterefine_var.set(""),
        self.dateoverdue_var.set("")
        self.txtBox.delete("1.0",END)

    # ***************************** Exit function for Exit button *********************************

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System","Do you want to exit?")
        if iExit > 0:
            self.root.destroy()
            return

    # ******************************* Delete function for delete function **************************************

    def delete_data(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error","First select the member")
        else:
            conn = mysql.connector.connect(host = 'localhost', username = 'root', password = 'password', database = 'library_db')
            my_cursor = conn.cursor()
            query = "delete from library_entries where PRN_No. = %s "
            value = (self.prn_var.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")

  
if __name__ == "__main__":
    root=Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()