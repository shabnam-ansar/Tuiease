from tkinter import Tk ,Label, Button,Frame,Entry,LabelFrame,StringVar
from PIL import Image, ImageTk
from tkinter import ttk
import pymysql #ignore
import tkinter as tk
from tkinter import messagebox



class resultclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x785+0+0")
        self.root.title("WELCOME TO TUIEASE")
        self.root.bind('<Configure>', self.on_resize)
        self.root.resizable(False, False)

       # Load and resize the background image
        original_image = Image.open("IMG FOLDER/stu_bg.png")
        resized_image = original_image.resize((1500, 755))
        self.background = ImageTk.PhotoImage(resized_image)

        # student details
        self.bglabel = Label(self.root, image=self.background)
        self.bglabel.place(x=10, y=0)

        # Add a title label
        self.bg_title = Label(self.root, text="Result Managemnt System", font=("Times New Roman", 30, "bold"), border=15, bg="#FF5757", fg="white")
        self.bg_title.place(x=10, y=10, height=40,width=1500)

        ##-----widgets-------
         # Main frame
        frame1 = Frame(self.root, bd=2, bg="white")
        frame1.place(x=15, y=65, width=1495, height=690)

        ##varaiable

        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_std=StringVar()
        self.var_sem=StringVar()
        self.var_obt=StringVar()
        self.var_full=StringVar()
        self.var_subject=StringVar()
        

         #  label frame
        main_frame = LabelFrame(frame1, bd=2, bg="#FF5757", relief="groove",  text="Add Student Result", font=("Times New Roman", 30, "bold"),fg="white")
        main_frame.place(x=45, y=20, width=1400, height=650)

        ## image for frame
        img_front = Image.open("IMG FOLDER/resultmanage.png")
        img_front = img_front.resize((600, 600))  # Adjust the size to fit the label frame
        self.Photoimg_left = ImageTk.PhotoImage(img_front)

        # Place the left frame image inside the left_frame
        lbl_left = Label(main_frame, image=self.Photoimg_left)
        lbl_left.place(x=750, y=30, width=600, height=500)  



         #roll
        roll= Label(main_frame, text="Roll No.", font=("Times New Roman", 17, "bold"), bg="white", fg="black")
        roll.grid(row=3, column=0, padx=20, pady=(70, 10), sticky="W")  # Add top padding

        roll_entry = Entry(main_frame,textvariable=self.var_roll, font=("Times New Roman", 17, "bold"), width=10, relief="sunken")
        roll_entry.grid(row=3, column=1, padx=5, pady=(70, 10), sticky="W")

        #name
        name = Label(main_frame, text="Name", font=("Times New Roman", 17, "bold"), bg="white", fg="black")
        name.grid(row=4, column=0, padx=20, pady=10, sticky="W")

        name_entry = Entry(main_frame, textvariable=self.var_name,font=("Times New Roman", 17, "bold"), width=35, relief="sunken")
        name_entry.grid(row=4, column=1, padx=10, pady=10, sticky="W")

        

        # Standard
        standard = Label(main_frame, text="Standard", font=("Times New Roman", 17, "bold"), bg="white", fg="black")
        standard.grid(row=5, column=0, padx=20, pady=10, sticky="W")

        standard_combo = ttk.Combobox(main_frame,textvariable=self.var_std, font=("Times New Roman", 17, "bold"), width=10, state="readonly")
        standard_combo["values"] = ("Select", "I", "II", "III", "IV", "V", "VI","VII","VIII","IX","X")
        standard_combo.current(0)
        standard_combo.grid(row=5, column=1, padx=10, pady=10, sticky="W")


       
         # Semester
        semester = Label(main_frame, text="Semester", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
        semester.grid(row=6, column=0, padx=20, pady=10, sticky="W")

        semester_combo = ttk.Combobox(main_frame, textvariable=self.var_sem,font=("Times New Roman", 17, "bold"), width=10, state="readonly")
        semester_combo["values"] = ("Select", "Unit-I", "Unit-II", "I", "II", "III", "IV")
        semester_combo.current(0)
        semester_combo.grid(row=6, column=1, padx=10, pady=10, sticky="W")

         # Marks Obtained
        obtained = Label(main_frame, text="Marks Obtained", font=("Times New Roman", 17, "bold"), bg="white", fg="black")
        obtained.grid(row=7, column=0, padx=20, pady=10, sticky="W")

        obtained_entry = Entry(main_frame, textvariable=self.var_obt,font=("Times New Roman", 17, "bold"), width=15, relief="sunken")
        obtained_entry.grid(row=7, column=1, padx=10, pady=10, sticky="W")

          # Full Marks
        full = Label(main_frame, text="Full Marks", font=("Times New Roman", 17, "bold"), bg="white", fg="black")
        full.grid(row=8, column=0, padx=20, pady=10, sticky="W")

        full_entry = Entry(main_frame, textvariable=self.var_full,font=("Times New Roman", 17, "bold"), width=15, relief="sunken")
        full_entry.grid(row=8, column=1, padx=10, pady=10, sticky="W")

        
         # subject
        subject = Label(main_frame, text="Subject", font=("Times New Roman", 17, "bold"), bg="white", fg="black")
        subject.grid(row=9, column=0, padx=20, pady=10, sticky="W")

        subject_combo = ttk.Combobox(main_frame, textvariable=self.var_subject,font=("Times New Roman", 17, "bold"), width=25, state="readonly")
        subject_combo["values"] = ("Select", "All", "English", "Maths", "Geography", "History", "Hindi","Marathi","Physics","Chemistry","Science","Arts","EVS1","EVS2")
        subject_combo.current(0)
        subject_combo.grid(row=9, column=1, padx=10, pady=10, sticky="W")


    

        # Save button
        save_btn = Button(main_frame, text="Save", bd=2, width=20, height=1, font=("Times New Roman", 14, "bold"), bg="white", fg="black",command=self.add_function)
        save_btn.grid(row=10, column=0, padx=10, pady=20, sticky="W")

       # Update button
        clear_btn = Button(main_frame, text="clear", bd=2, width=20, height=1, font=("Times New Roman", 14, "bold"), bg="white", fg="black")
        clear_btn.grid(row=10, column=1, padx=10, pady=20, sticky="W")

      #add function
    def add_function(self):
        if self.var_roll.get() == "" or self.var_name.get() == "" or self.var_std.get() == "":
            messagebox.showerror("Error", "Please fill all fields")
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="", database="result")
                cursor = conn.cursor()
                sql = "INSERT INTO result (roll, name, std, sem, obt, full, subject) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (self.var_roll.get(), self.var_name.get(), self.var_std.get(), self.var_sem.get(),
                          self.var_obt.get(), self.var_full.get(), self.var_subject.get())
                cursor.execute(sql, values)
                conn.commit()
                messagebox.showinfo("Success", "Data added successfully!")
                self.reset_fields()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        #reset function
    def reset_fields(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_std.set("Select")
        self.var_sem.set("Select")
        self.var_obt.set("")
        self.var_full.set("")
        self.var_subject.set("Select")












































    def on_resize(self, event):
      print(f"New size: {event.width}x{event.height}") 
                


if __name__ == "__main__":
    root = Tk()
    obj = resultclass(root)
    root.mainloop()