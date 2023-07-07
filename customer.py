from tkinter import *
class Cust_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM:")
        #self.root.geometry("1295x550+230+220")
        self.root.geometry("1295x550+0+0")
        #=====title===========
        lbl_title = Label(self.root,text="CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        # ======= Logo =====
        img0 = Image.open(r"C:\Users\Hersi\Videos\madina\Images\logo2.png")
        img0 = img0.resize((100, 40), Image.LANCZOS)
        self.photoimg0 = Tk.PhotoImage(img0)
        lbl_image = Label(root, image=img0, bd=4, relief=RIDGE)
        lbl_image.place(x=0, y=0, width=100, height=40)


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()