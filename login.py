from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

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
        
        # Load and display the background image
        #self.background_image = ImageTk.PhotoImage(Image.open("madinalogo.jpg"))
        #self.canvas.create_image(200, 200, image=self.background_image, anchor=NW)
    
    def create_gradient_background(self):
        # Create a rectangular gradient background on the canvas
        for y in range(700):
            r = int((y / 700) * int(self.color2[1:3], 16) + ((700 - y) / 700) * int(self.color1[1:3], 16))
            g = int((y / 700) * int(self.color2[3:5], 16) + ((700 - y) / 700) * int(self.color1[3:5], 16))
            b = int((y / 700) * int(self.color2[5:7], 16) + ((700 - y) / 700) * int(self.color1[5:7], 16))
            color = f"#{hex(r)[2:].zfill(2)}{hex(g)[2:].zfill(2)}{hex(b)[2:].zfill(2)}"
            self.canvas.create_line(0, y, 1350, y, fill=color, width=1)
        # =============login frame=================
        #frame.place(x=480, y=100, width=400, height=390)
        frame = Frame(self.root, bg="black")
        frame.place(x=480, y=100, width=400, height=390)


if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()
