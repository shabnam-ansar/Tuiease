from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from student_detail import student_detail
from result import resultclass
from tkinter import Toplevel
from feesmanage import fees
from report import report
from about import About
from tkinter import messagebox


class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x785+0+0")
        self.root.title("WELCOME TO TUIEASE")
        self.root.bind('<Configure>', self.on_resize)
        self.root.resizable(False, False)

       # Load and resize the background image
        original_image = Image.open("IMG FOLDER/mainpg.png")
        resized_image = original_image.resize((1500, 755))
        self.background = ImageTk.PhotoImage(resized_image)

        # student details
        self.bglabel = Label(self.root, image=self.background)
        self.bglabel.place(x=10, y=0)
        #img placement of student detail
        image1 = Image.open("IMG FOLDER/student detail.png")
        image1 = image1.resize((300, 210))
        self.Photoimg1 = ImageTk.PhotoImage(image1)

        #img button of student detail button
        b1 = Button(self.root,command=self.student, image=self.Photoimg1)
        b1.place(x=130, y=170, width=300, height=210)

        #text button for student detail button
        b1_1 = Button(self.root,command=self.student, text="Student Details", cursor="hand2",  font=("Times New Roman", 15, "bold"), bg="white", fg="black", bd=5,  relief="solid" )
        b1_1.place(x=113, y=390, width=328, height=40)

        # image for resize fees record
        image2 = Image.open("IMG FOLDER/fees details.png")
        image2 = image2.resize((300, 210))
        self.Photoimg2 = ImageTk.PhotoImage(image2)
       #  image placement of  Fees record 
        b2 = Button(self.root,command=self.fees, image=self.Photoimg2)
        b2.place(x=600, y=170, width=300, height=210)
       # Add a text button for fees record
        b2_1 = Button(self.root, text="Fees Record", cursor="hand2", font=("Times New Roman", 15, "bold"), bg="white", fg="black",bd=5,command=self.fees, relief="solid" )
        b2_1.place(x=582, y=390, width=330, height=40)


         #button image for result
        image3= Image.open("IMG FOLDER/result.png")
        image3 = image3.resize((300, 210))
        self.Photoimg3 = ImageTk.PhotoImage(image3)
        # button image for result placement
        b3 = Button(self.root,command=self.result, image=self.Photoimg3)
        b3.place(x=1095, y=170, width=300, height=210)
        # Add a text button for result
        b3_1 = Button(self.root, text="Result", cursor="hand2", font=("Times New Roman", 15, "bold"), bg="white",command=self.result, fg="black",bd=5, relief="solid" )
        b3_1.place(x=1075, y=390, width=330, height=40)

        # Load and resize the button image for report
        image4= Image.open("IMG FOLDER/report.png")
        image4 = image4.resize((300, 210))
        self.Photoimg4 = ImageTk.PhotoImage(image4)
        # Add a button with the image for report
        b4 = Button(self.root,command=self.report, image=self.Photoimg4)
        b4.place(x=130, y=480, width=300, height=210)
        # Add a text button for report
        b4_1 = Button(self.root, text="Report", cursor="hand2", font=("Times New Roman", 15, "bold"), bg="white", command=self.report,fg="black",bd=5, relief="solid")
        b4_1.place(x=112, y=700, width=330, height=40)

        # Load and resize the button image for about
        image5 = Image.open("IMG FOLDER/schedule.png")
        image5 = image5.resize((300, 210))
        self.Photoimg5 = ImageTk.PhotoImage(image5)
      # Add a button with the image for about
        b5 = Button(self.root, command=self.about , image=self.Photoimg5)
        b5.place(x=600, y=480, width=300, height=210)
       # Add a text button for about
        b5_1 = Button(self.root, text="About", cursor="hand2", font=("Times New Roman", 15, "bold"), bg="white",  command=self.about,fg="black",bd=5, relief="solid")
        b5_1.place(x=582, y=700, width=330, height=40)

         # Load and resize the button image for exit
        image6 = Image.open("IMG FOLDER/exit.png")
        image6 = image6.resize((300, 210))
        self.Photoimg6 = ImageTk.PhotoImage(image6)
        # Add a button with the image for exit
        b6 = Button(self.root, command=self.exit,image=self.Photoimg6)
        b6.place(x=1095, y=480, width=300, height=210)
       # Add a text button for exit
        b6_1 = Button(self.root, text="Exit",command=self.exit, cursor="hand2", font=("Times New Roman", 15, "bold"), bg="white", fg="black",bd=5, relief="solid")
        b6_1.place(x=1075, y=700, width=330, height=40)


    def student(self):
       self.new_window=Toplevel(self.root)
       self.app=student_detail(self.new_window)

    def fees(self):
       self.new_window=Toplevel(self.root)
       self.app=fees(self.new_window)

    def result(self):
       self.new_window=Toplevel(self.root)
       self.app=resultclass(self.new_window)

    def report(self):
       self.new_window=Toplevel(self.root)
       self.app=report(self.new_window)

    
    def about(self):
       self.new_window=Toplevel(self.root)
       self.app=About(self.new_window)
   

    def exit(self):
        """Exit the application after showing a confirmation dialog."""
        result = messagebox.askquestion("Exit", "Are you sure you want to exit?")
        if result == "yes":
            self.root.quit()





















        




       

    def on_resize(self, event):
        print(f"New size: {event.width}x{event.height}")

   

if __name__ == "__main__":
    root = Tk()
    app = student(root)
    root.mainloop()
