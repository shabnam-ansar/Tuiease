from tkinter import Tk, Toplevel, Label
from PIL import Image, ImageTk

class About:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x785+0+0")
        self.root.title("WELCOME TO TUIEASE")
        self.root.bind('<Configure>', self.on_resize)
        self.root.resizable(False, False)
        

   
        original_image = Image.open("IMG FOLDER/About pg text.png")
        resized_image = original_image.resize((1500, 755))
        self.background = ImageTk.PhotoImage(resized_image)

        
        # Set the background image
        self.bglabel = Label(self.root, image=self.background)
        self.bglabel.place(x=10, y=30)

        # Add a title label
        self.bg_title = Label(self.root, text="ABOUT TUIEASE", font=("Times New Roman", 25, "bold"), border=12, bg="#FF5757", fg="white")
        self.bg_title.place(x=10, y=10, width=1500)


    def on_resize(self, event):
          print(f"New size: {event.width}x{event.height}")

        

if __name__ == "__main__":
    root = Tk()
    app = About(root)
    root.mainloop()
