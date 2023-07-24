from tkinter import *
from tkinter import ttk

class HotelExpensesTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Expenses Tracking")
        self.root.geometry("1000x600")
        self.root.configure(bg="black")
        
        self.create_widgets()

    def create_widgets(self):
        self.create_title_frame()
        self.create_hotel_expenses_frame()
        self.create_other_expenses_frame()

    def create_title_frame(self):
        title_frame = Frame(self.root, bg="black", relief=GROOVE)
        title_frame.pack(side=TOP, fill="x")

        title_label = Label(title_frame, text="HOTEL EXPENSES TRACKING SYSTEM",
                            font=("Montserrat SemiBold", 19, "bold"), bg="black", fg="gold")
        title_label.pack(pady=10)

    def create_hotel_expenses_frame(self):
        hotel_expenses_frame = LabelFrame(self.root, text="Hotel Expenses", font=("Montserrat", 14), border=0,
                                          bg="black", fg="gold")
        hotel_expenses_frame.place(x=0, y=70, width=500, height=500)

        hotel_expenses_tabel = ttk.Treeview(hotel_expenses_frame, columns=("date", "description", "amount"), show="headings")
        hotel_expenses_tabel.heading("date", text="Date")
        hotel_expenses_tabel.heading("description", text="Description")
        hotel_expenses_tabel.heading("amount", text="Amount")
        hotel_expenses_tabel.pack(fill=BOTH, expand=1)

        print_receipt_hotel_button = self.create_button(hotel_expenses_frame, "Print Receipt", self.print_hotel_receipt)
        print_receipt_hotel_button.pack(pady=10)

        edit_update_hotel_button = self.create_button(hotel_expenses_frame, "Edit and Update", self.edit_update_hotel_expenses)
        edit_update_hotel_button.pack(pady=10)

    def create_other_expenses_frame(self):
        other_expenses_frame = LabelFrame(self.root, text="Other Expenses", font=("Montserrat", 14), border=0,
                                          bg="black", fg="gold")
        other_expenses_frame.place(x=500, y=70, width=500, height=500)

        other_expenses_tabel = ttk.Treeview(other_expenses_frame, columns=("date", "description", "amount"), show="headings")
        other_expenses_tabel.heading("date", text="Date")
        other_expenses_tabel.heading("description", text="Description")
        other_expenses_tabel.heading("amount", text="Amount")
        other_expenses_tabel.pack(fill=BOTH, expand=1)

        print_receipt_other_button = self.create_button(other_expenses_frame, "Print Receipt", self.print_other_receipt)
        print_receipt_other_button.pack(pady=10)

        edit_update_other_button = self.create_button(other_expenses_frame, "Edit and Update", self.edit_update_other_expenses)
        edit_update_other_button.pack(pady=10)

    def create_button(self, frame, text, command):
        style = ttk.Style()
        style.configure("Gold.TButton", font=("Montserrat", 12), background="#FFA726", foreground="gold", padding=5)
        return ttk.Button(frame, text=text, style="Gold.TButton", command=command)

    def print_hotel_receipt(self):
        # Add your code here to handle printing the hotel receipt
        pass

    def edit_update_hotel_expenses(self):
        # Add your code here to handle editing and updating hotel expenses
        pass

    def print_other_receipt(self):
        # Add your code here to handle printing the other receipt
        pass

    def edit_update_other_expenses(self):
        # Add your code here to handle editing and updating other expenses
        pass


if __name__ == "__main__":
    root = Tk()
    app = HotelExpensesTracker(root)
    root.mainloop()
