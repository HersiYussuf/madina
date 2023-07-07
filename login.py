from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from dotenv import load_dotenv
import os
from PIL import Image, ImageTk
#from customer import Cust_Win
#from home_page import MainPage

load_dotenv()

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Madina Guest House")
        self.root.geometry("1350x700+0+0")
        # Create a canvas to display the background gradient
        self.canvas = Canvas(root, width=1350, height=700)
        self.canvas.pack()
        # Define the gradient colors
        self.color1 = "#ff0000"  # Red color
        self.color2 = "#ffffff"  # White color
        # Create a gradient background
        self.create_gradient_background()
        # ==============login frame=================
        frame = Frame(self.root, bg="black")
        frame.place(x=480, y=100, width=400, height=390)
        # Username label and entry
        lbl_user = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="black", fg="white")
        lbl_user.place(x=50, y=100)
        self.txt_user = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_user.place(x=50, y=130, width=250)
        # Password label and entry
        lbl_password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="black", fg="white")
        lbl_password.place(x=50, y=170)
        self.txt_pass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txt_pass.place(x=50, y=200, width=250)
        # Login button
        btn_login = Button(frame, text="Login", font=("times new roman", 15, "bold"), bg="black", fg="white", command=self.login)
        btn_login.place(x=50, y=250, width=100, height=35)

    def create_gradient_background(self):
        # Create a rectangular gradient background on the canvas
        for y in range(700):
            r = int((y / 700) * int(self.color2[1:3], 16) + ((700 - y) / 700) * int(self.color1[1:3], 16))
            g = int((y / 700) * int(self.color2[3:5], 16) + ((700 - y) / 700) * int(self.color1[3:5], 16))
            b = int((y / 700) * int(self.color2[5:7], 16) + ((700 - y) / 700) * int(self.color1[5:7], 16))
            color = f"#{hex(r)[2:].zfill(2)}{hex(g)[2:].zfill(2)}{hex(b)[2:].zfill(2)}"
            self.canvas.create_line(0, y, 1350, y, fill=color, width=1)

    def login(self):
        if self.txt_user.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            username = os.getenv("MYSQL_USERNAME")
            password = os.getenv("MYSQL_PASSWORD")
            host = os.getenv("MYSQL_HOST")
            conn = mysql.connector.connect(host=host, username=username, password=password, database="madina")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM login WHERE username=%s AND password=%s", (self.txt_user.get(), self.txt_pass.get()))
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username & Password", parent=self.root)
            else:
                open = messagebox.showinfo("Welcome to Madina Guest House Management system", parent=self.root)
                if open:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                    self.root.destroy()


    def reset(self):
        self.txt_user.delete(0, END)
        self.txt_pass.delete(0, END)
    #/usr/bin/env python3def home_page(self):
        #self.root.destroy()
        #self.new_window = Toplevel(self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()
