from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from dotenv import load_dotenv
import os
from PIL import Image, ImageTk

load_dotenv()

class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Madina Guest House")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="white")
        # ========= image===========
        img1 = Image.open("Images/WhatsApp Image 2023-06-23 at 16.16.35.jpg")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_image = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbl_image.place(x=0, y=0, width=1550, height=140)
        # ========= image===========
        img2 = Image.open("Images/madinalogo.jpg")
        img2 = img2.resize((230, 230), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_image = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_image.place(x=0, y=0, width=230, height=140)
        # =============title============
        lbl_title = Label(self.root, text="MADINA MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)
        # ============== main frame==========
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)
        # =============Menu============
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 25, "bold"), bg="black", fg="gold", bd=0, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)
        # ======== Button frame========
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)
        # customer button
        cust_btn = Button(btn_frame, text="CUSTOMER", width=25, font=("times new roman", 15, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE, cursor="hand2")
        cust_btn.grid(row=0, column=0, padx=1, sticky="w")
        # details button
        details_btn = Button(btn_frame, text="DETAILS", width=25, font=("times new roman", 15, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE, cursor="hand2")
        details_btn.grid(row=1, column=0, padx=1, sticky="w")
        # ROOM button
        room_btn = Button(btn_frame, text="ROOM", width=25, font=("times new roman", 15, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE, cursor="hand2")
        room_btn.grid(row=2, column=0, padx=1, sticky="w")
        # report button
        report_btn = Button(btn_frame, text="REPORT", width=25, font=("times new roman", 15, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE, cursor="hand2")
        report_btn.grid(row=3, column=0, padx=1, sticky="w")
        # logout button
        logout_btn = Button(btn_frame, text="LOGOUT", width=25, font=("times new roman", 15, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE, cursor="hand2")
        logout_btn.grid(row=0, column=4, padx=1, sticky="w")
        # ======left image=========
        img3 = Image.open("Images/pexels-ylanite-koppens-776656.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lbl_image3 = Label(main_frame, image=self.photoimage3, bd=4, relief=RIDGE)
        lbl_image3.place(x=225, y=0, width=1310, height=590)
        # image 4
        img4 = Image.open(r"C:\Users\Hersi\Videos\madina\Images\pexels-mason-slover-940271.jpg")
        img4 = img4.resize((230, 230), Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        lbl_image4 = Label(main_frame, image=self.photoimage4, bd=4, relief=RIDGE)
        lbl_image4.place(x=0, y=230, width=230, height=140)
        # image 5
        img5 = Image.open(r"C:\Users\Hersi\Videos\madina\Images\wepik-elegant-linear-luxury-homes-group-logo-20230703055917uoyP.png")
        img5 = img5.resize((230, 230), Image.LANCZOS)
        self.photoimage5 = ImageTk.PhotoImage(img5)
        lbl_image5 = Label(main_frame, image=self.photoimage5, bd=4, relief=RIDGE)
        lbl_image5.place(x=0, y=380, width=230, height=140)


if __name__ == "__main__":
    root = Tk()
    obj = MainPage(root)
    root.mainloop()
