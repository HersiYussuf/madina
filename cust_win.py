from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
class Cust_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM:")
        self.root.geometry("1295x550+230+220")
        #self.root.geometry("1295x550+0+0")
        # Title
        lbl_title = Label(self.root, text="CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bd=4, relief="ridge")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        
        # Logo
        img1 = Image.open("Images/madinalogo.jpg")
        img1 = img1.resize((100, 40), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_image = Label(self.root, image=self.photoimg1, bd=0, relief="ridge")
        lbl_image.place(x=5, y=2, width=100, height=40)
        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief="ridge", text="Guest Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)
        # label and
        # # Receipt number
        lbl_receipt = Label(labelframeleft,text="RECEIPT NUMBER", font=("arial", 10, "bold"), padx=2, pady=6)
        lbl_receipt.grid(row=0, column=0, sticky=W)
        entry_receipt = ttk.Entry(labelframeleft, font=("arial", 10, "bold"), width=20)
        entry_receipt.grid(row=0, column=1)
        
        # Room no
        lbl_room = Label(labelframeleft,text="ROOM NUMBER", font=("arial", 10, "bold"), padx=2, pady=3)
        lbl_room.grid(row=1, column=0, sticky=W)
        entry_room = ttk.Entry(labelframeleft, font=("arial", 10, "bold"), width=20)
        entry_room.grid(row=1, column=1)

        # Customer name
        lbl_customer = Label(labelframeleft, text="CUSTOMER NAME", font=("arial", 10, "bold"), padx=2, pady=3)
        lbl_customer.grid(row=2, column=0, sticky=W)
        entry_customer = ttk.Entry(labelframeleft, font=("arial", 10, "bold"), width=20)
        entry_customer.grid(row=2, column=1)
        # Phone Number
        lbl_phone = Label(labelframeleft,text="PHONE NUMBER", font=("arial", 10, "bold"), padx=2, pady=3)
        lbl_phone.grid(row=3, column=0, sticky=W)
        entry_phone = ttk.Entry(labelframeleft, font=("arial", 10, "bold"), width=20)
        entry_phone.grid(row=3, column=1)
        # ID or passport number
        lbl_id = Label(labelframeleft,text="ID/PASSPORT", font=("arial", 10, "bold"), padx=2, pady=3)
        lbl_id.grid(row=4, column=0, sticky=W)
        entry_id = ttk.Entry(labelframeleft, font=("arial", 10, "bold"), width=20)
        entry_id.grid(row=4, column=1)
        # Balance B/F
        lbl_balance = Label(labelframeleft,text="BALANCE B/F", font=("arial", 10, "bold"), padx=2, pady=3)
        lbl_balance.grid(row=5, column=0, sticky=W)
        entry_balance = ttk.Entry(labelframeleft, font=("arial", 10, "bold"), width=20)
        entry_balance.grid(row=5, column=1)
       
        # Daily Charges
        lbl_daily = Label(labelframeleft,text="DAILY CHARGES", font=("arial", 10, "bold"), padx=2, pady=3)
        lbl_daily.grid(row=6, column=0, sticky=W)
        entry_daily = ttk.Entry(labelframeleft, font=("arial", 10, "bold"), width=20)
        entry_daily.grid(row=6, column=1)
        # Total amount due
        lbl_total = Label(labelframeleft,text="TOTAL AMOUNT DUE", font=("arial", 10, "bold"), padx=2, pady=3)
        lbl_total.grid(row=7, column=0, sticky=W)
        entry_total = ttk.Entry(labelframeleft, font=("arial", 10, "bold"), width=20)
        entry_total.grid(row=7, column=1)
        
        # Other services
        lbl_services = Label(labelframeleft,text="OTHER SERVICES", font=("arial", 10, "bold"), padx=2, pady=3)
        lbl_services.grid(row=8, column=0, sticky=W)
        entry_services = ttk.Entry(labelframeleft, font=("arial", 10, "bold"), width=20)
        entry_services.grid(row=8, column=1)
        # Amount paid
        lbl_paid = Label(labelframeleft, text="AMOUNT PAID", font=("arial", 10, "bold"), padx=2, pady=3)
        lbl_paid.grid(row=9, column=0, sticky=W)
        entry_paid = ttk.Entry(labelframeleft, font=("arial", 10, "bold"), width=20)
        entry_paid.grid(row=9, column=1)
         # Advance
        lbl_advance = Label(labelframeleft, text ="ADVANCE", font=("arial", 10, "bold"), padx=2, pady=3)
        lbl_advance.grid(row=10, column=0, sticky=W)
        entry_advance = ttk.Entry(labelframeleft, font=("arial", 10, "bold"), width=20)
        entry_advance.grid(row=10, column=1)
        # Balance to pay
        lbl_balance_pay = Label(labelframeleft,text="BALANCE TO PAY", font=("arial", 10, "bold"), padx=2, pady=3)
        lbl_balance_pay.grid(row=11, column=0, sticky=W)
        entry_balance_pay = ttk.Entry(labelframeleft, font=("arial", 10, "bold"), width=20)
        entry_balance_pay.grid(row=11, column=1)
        
        # Button frame
        btn_frame = Frame(labelframeleft, bd=2, relief="ridge")
        btn_frame.place(x=0, y=350, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)
        # ===============table frame=========
        # label frame
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search system", font=("arial435", 12, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=860, height=490)
        # label search bar
        label_search_bar = Label(table_frame,text="Search Bar", font=("arial", 12, "bold"), bg= "red", fg = "White")
        label_search_bar.grid(row = 0  , column = 0, sticky = W)
        # combo box
        combo_search_bar = ttk.Combobox(table_frame, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_search_bar['values'] = ('Receipt number', 'Customer name', 'Gender', 'Contact', 'Passport or ID number')
        combo_search_bar.grid(row = 0  , column = 1, sticky = W)
        combo_search_bar.current(0)
        # entry search bar
        entr_search_bar = ttk.Entry(table_frame, width=18, font=("arial", 12, "bold"))
        entr_search_bar.grid(row = 0  , column = 2, sticky = W)
        # button search bar
        btn_search_bar = Button(table_frame, text="Search", font=("arial", 12, "bold"), bg = "black", fg = "gold", width =5)
        btn_search_bar.grid(row = 0  , column = 3, sticky = W)
        # show all
        btn_show_all = Button(table_frame, text="Show All", font=("arial", 12, "bold"), bg = "black", fg = "gold", width =5)
        btn_show_all.grid(row = 0  , column = 4, sticky = W)
        # Table frame
        table_frame = LabelFrame(self.root, bd=2, relief="ridge", text="View Details and Search system", font=("arial", 12, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=860, height=490)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.CustomerDetails_Table = ttk.Treeview(table_frame, columns=("Receipt number", "Room no", "Customer name", "Phone Number", "ID or passport number", "Balance B/F", "Daily Charges", "Total amount due", "Other services", "Amount paid", "Advance", "Balance to pay"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.CustomerDetails_Table.xview)
        scroll_y.config(command=self.CustomerDetails_Table.yview)

        self.CustomerDetails_Table.heading("Receipt number", text="Receipt number")
        self.CustomerDetails_Table.heading("Room no", text="Room no")
        self.CustomerDetails_Table.heading("Customer name", text="Customer name")
        self.CustomerDetails_Table.heading("Phone Number", text="Phone Number")
        self.CustomerDetails_Table.heading("ID or passport number", text="ID or passport number")
        self.CustomerDetails_Table.heading("Balance B/F", text="Balance B/F")
        self.CustomerDetails_Table.heading("Daily Charges", text="Daily Charges")
        self.CustomerDetails_Table.heading("Total amount due", text="Total amount due")
        self.CustomerDetails_Table.heading("Other services", text="Other services")
        self.CustomerDetails_Table.heading("Amount paid", text="Amount paid")
        self.CustomerDetails_Table.heading("Advance", text="Advance")
        self.CustomerDetails_Table.heading("Balance to pay", text="Balance to pay")

        self.CustomerDetails_Table['show'] = 'headings'
       

        self.CustomerDetails_Table.column("Receipt number", width=80)
        self.CustomerDetails_Table.column("Room no", width=80)
        self.CustomerDetails_Table.column("Customer name", width=80)
        self.CustomerDetails_Table.column("Phone Number", width=100)
        self.CustomerDetails_Table.column("ID or passport number", width=80)
        self.CustomerDetails_Table.column("Balance B/F", width=80)
        self.CustomerDetails_Table.column("Daily Charges", width=80)
        self.CustomerDetails_Table.column("Total amount due", width=80)
        self.CustomerDetails_Table.column("Other services", width=80)
        self.CustomerDetails_Table.column("Amount paid", width=80)
        self.CustomerDetails_Table.column("Advance", width=80)
        self.CustomerDetails_Table.column("Balance to pay", width=80)

        self.CustomerDetails_Table.pack(fill=BOTH, expand=1)

        


        
if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()