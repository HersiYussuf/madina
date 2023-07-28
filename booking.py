from tkinter import *
from tkinter import ttk

# Function to handle the Print Receipt button
def calculate_total(items):
    # Helper function to calculate the total price of purchased items
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

def print_receipt(billing_details, purchased_items):
    # Print the header of the receipt
    print("----- Receipt -----")

    # Print billing details
    print("Name:", billing_details.get("name", ""))
    print("Address:", billing_details.get("address", ""))
    print("Email:", billing_details.get("email", ""))
    print("Phone:", billing_details.get("phone", ""))

    # Print purchased items
    print("\n-- Purchased Items --")
    for index, item in enumerate(purchased_items, start=1):
        print(f"{index}. {item['name']} x {item['quantity']} - ${item['price'] * item['quantity']}")

    # Calculate and print the total
    total = calculate_total(purchased_items)
    print("Total:", total)

    # Print the footer of the receipt
    print("--------------------")

# Example usage:
billing_details = {
    "name": "John Doe",
    "address": "123 Main Street",
    "email": "john@example.com",
    "phone": "555-1234"
}

purchased_items = [
    {"name": "Item 1", "price": 10, "quantity": 2},
    {"name": "Item 2", "price": 5, "quantity": 3},
    {"name": "Item 3", "price": 15, "quantity": 1},
]

print_receipt(billing_details, purchased_items)


# Function to handle the Edit and Update button
def edit_update(billing_details):
    # Display the current billing details
    print("Current Billing Details:")
    print("Name:", billing_details.get("name", ""))
    print("Address:", billing_details.get("address", ""))
    print("Email:", billing_details.get("email", ""))
    print("Phone:", billing_details.get("phone", ""))

    # Ask the user if they want to edit the billing details
    choice = input("Do you want to edit the billing details? (yes/no): ").lower()

    if choice == "yes":
        # Ask the user for the updated details
        updated_name = input("Enter the updated name: ")
        updated_address = input("Enter the updated address: ")
        updated_email = input("Enter the updated email: ")
        updated_phone = input("Enter the updated phone number: ")

        # Update the billing details dictionary
        billing_details["name"] = updated_name
        billing_details["address"] = updated_address
        billing_details["email"] = updated_email
        billing_details["phone"] = updated_phone

        print("Billing details updated successfully!")
    else:
        print("No changes were made to the billing details.")

# Example usage:
billing_details = {
    "name": "John Doe",
    "address": "123 Main Street",
    "email": "john@example.com",
    "phone": "555-1234"
}

edit_update(billing_details)


# Creating the main window
root = Tk()
root.title("Hotel Room Billing")
root.geometry("1000x600")
root.configure(bg="black")  # Setting the background color to black

# Title Frame
title_frame = Frame(root, bg="black", relief=GROOVE)
title_frame.pack(side=TOP, fill="x")

title_label = Label(root, text="HOTEL ROOM BILLING SYSTEM",
                    font=("Montserrat SemiBold", 19, "bold"), bg="black", fg="gold")  # Setting the foreground color to gold
title_label.place(x=300, y=30)

# Room Details Section
room_frame = LabelFrame(root, text="Room Details", font=("Montserrat", 14), border=0,
                        bg="black", fg="gold")  # Setting the foreground color to gold
room_frame.place(x=0, y=70, width=1000, height=100)

customer_name_label = Label(room_frame, text="Customer Name",
                            font=("Montserrat", 14), bg="black", fg="gold")  # Setting the foreground color to gold
customer_name_label.grid(row=0, column=0, padx=20)

customer_name_entry = Entry(room_frame, width=20, font="Montserrat")
customer_name_entry.grid(row=0, column=1, padx=10)

room_no_label = Label(room_frame, text="Room No.",
                      font=("Montserrat", 14), bg="black", fg="gold")  # Setting the foreground color to gold
room_no_label.grid(row=0, column=2, padx=20)

room_no_entry = Entry(room_frame, width=10, font="Montserrat")
room_no_entry.grid(row=0, column=3, padx=10)

room_price_label = Label(room_frame, text="Room Price",
                         font=("Montserrat", 14), bg="black", fg="gold")  # Setting the foreground color to gold
room_price_label.grid(row=0, column=4, padx=20)

room_price_entry = Entry(room_frame, width=10, font="Montserrat")
room_price_entry.grid(row=0, column=5, padx=10)

check_in_label = Label(room_frame, text="Check-in Date",
                       font=("Montserrat", 14), bg="black", fg="gold")  # Setting the foreground color to gold
check_in_label.grid(row=0, column=6, padx=20)

check_in_entry = Entry(room_frame, width=15, font="Montserrat")
check_in_entry.grid(row=0, column=7, padx=10)

check_out_label = Label(room_frame, text="Check-out Date",
                        font=("Montserrat", 14), bg="black", fg="gold")  # Setting the foreground color to gold
check_out_label.grid(row=0, column=8, padx=20)

check_out_entry = Entry(room_frame, width=15, font="Montserrat")
check_out_entry.grid(row=0, column=9, padx=10)

# Billing Details Section
billing_frame = LabelFrame(root, text="Billing Details", font=("Montserrat", 14), border=0,
                           bg="black", fg="gold")  # Setting the foreground color to gold
billing_frame.place(x=0, y=180, width=1000, height=350)

# Treeview to display billing details
billing_tabel = ttk.Treeview(billing_frame, columns=("customer_name", "room_no", "room_price", "check_in_date", "check_out_date", "paid_amount", "balance_to_pay"), show="headings")
billing_tabel.heading("customer_name", text="Customer Name")
billing_tabel.heading("room_no", text="Room No.")
billing_tabel.heading("room_price", text="Room Price")
billing_tabel.heading("check_in_date", text="Check-in Date")
billing_tabel.heading("check_out_date", text="Check-out Date")
billing_tabel.heading("paid_amount", text="Paid Amount")
billing_tabel.heading("balance_to_pay", text="Balance to Pay")
billing_tabel.pack(fill=BOTH, expand=1)

# Buttons
print_receipt_button = Button(root, text="Print Receipt", font=("Montserrat", 12), bg="#FFA726", activebackground="#FFA726", command=print_receipt, fg="gold")  # Setting the foreground color to gold
print_receipt_button.place(x=150, y=550)

edit_update_button = Button(root, text="Edit and Update", font=("Montserrat", 12), bg="#FFA726", activebackground="#FFA726", command=edit_update, fg="gold")  # Setting the foreground color to gold
edit_update_button.place(x=400, y=550)

# Start the main event loop
root.mainloop()
