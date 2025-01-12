from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from firstpg import student
from tkinter import Toplevel


class Tuitease:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x785+0+0")
        self.root.title("WELCOME TO TUIEASE")
        self.root.bind('<Configure>', self.on_resize)
        self.root.resizable(False, False)

       # Load and resize the background image
        original_image = Image.open("IMG FOLDER/front pg.png")
        resized_image = original_image.resize((1500, 755))
        self.background = ImageTk.PhotoImage(resized_image)

        # Set the background image
        self.bglabel = Label(self.root, image=self.background)
        self.bglabel.place(x=10, y=0)

        image1 = Image.open("IMG FOLDER/frontbtn.png")
        image1 = image1.resize((550, 370))
        self.Photoimg1 = ImageTk.PhotoImage(image1)

        b1 = Button(self.root, command=self.student_details ,image=self.Photoimg1)
        b1.place(x=562, y=255, width=380, height=350)


        #=======Function=========
    def student_details(self):
       self.new_window=Toplevel(self.root)
       self.app=student(self.new_window)





       

    def on_resize(self, event):
        print(f"New size: {event.width}x{event.height}")

   

if __name__ == "__main__":
    root = Tk()
    app = Tuitease(root)
    root.mainloop()
