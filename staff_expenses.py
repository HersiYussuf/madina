from tkinter import *
from tkinter import ttk

class ExpensesTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expenses Tracking System")
        self.root.geometry("1000x600")
        self.root.configure(bg="black")

        self.create_widgets()

    def create_widgets(self):
        self.create_title_frame()
        self.create_expenses_frame("Hotel Expenses", 0, 70)
        self.create_expenses_frame("Other Expenses", 500, 70)
        self.create_expenses_frame("Staff Expenses", 250, 320)

    def create_title_frame(self):
        title_frame = Frame(self.root, bg="black", relief=GROOVE)
        title_frame.pack(side=TOP, fill="x")

        title_label = Label(title_frame, text="EXPENSES TRACKING SYSTEM",
                            font=("Montserrat SemiBold", 19, "bold"), bg="black", fg="gold")
        title_label.pack(pady=10)

    def create_expenses_frame(self, title, x_position, y_position):
        expenses_frame = LabelFrame(self.root, text=title, font=("Montserrat", 14), border=0,
                                    bg="black", fg="gold")
        expenses_frame.place(x=x_position, y=y_position, width=500, height=220)

        expenses_tabel = ttk.Treeview(expenses_frame, columns=("date", "description", "amount"), show="headings")
        expenses_tabel.heading("date", text="Date")
        expenses_tabel.heading("description", text="Description")
        expenses_tabel.heading("amount", text="Amount")
        expenses_tabel.pack(fill=BOTH, expand=1)

        print_receipt_button = self.create_button(expenses_frame, "Print Receipt", self.print_receipt)
        print_receipt_button.pack(pady=10)

        edit_update_button = self.create_button(expenses_frame, "Edit and Update", self.edit_update_expenses)
        edit_update_button.pack(pady=10)

    def create_button(self, frame, text, command):
        style = ttk.Style()
        style.configure("Gold.TButton", font=("Montserrat", 12), background="#FFA726", foreground="gold", padding=5)
        return ttk.Button(frame, text=text, style="Gold.TButton", command=command)

    def print_receipt(self):
        # Add your code here to handle printing the receipt
        pass

    def edit_update_expenses(self):
        # Add your code here to handle editing and updating expenses
        pass

if __name__ == "__main__":
    root = Tk()
    app = ExpensesTracker(root)
    root.mainloop()
