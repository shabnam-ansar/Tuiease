from tkinter import Tk ,Label,Button,LabelFrame,Frame,Scrollbar,StringVar
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Entry
from tkcalendar import DateEntry
import pymysql #ignore
import tkinter as tk
from tkinter import messagebox



class student_detail:
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

        # Set the background image
        self.bglabel = Label(self.root, image=self.background)
        self.bglabel.place(x=10, y=0)

        # Add a title label
        self.bg_title = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("Times New Roman", 30, "bold"), border=12, bg="#FF5757", fg="white")
        self.bg_title.place(x=10, y=10, width=1500)

        # Main frame
        frame1 = Frame(self.root, bd=2, bg="white")
        frame1.place(x=15, y=65, width=1495, height=690)

          #-------variable---------
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_std=StringVar()
        self.var_fess=StringVar()
        self.var_In=StringVar()
        self.var_phone=StringVar()
        self.var_subject=StringVar()
        self.var_search=StringVar()
        


         # Left side label frame
        left_frame = LabelFrame(frame1, bd=2, bg="white", relief="groove", font=("Times New Roman", 15, "bold"))
        left_frame.place(x=10, y=5, width=500, height=675)

        # Left frame image
        img_left = Image.open("IMG FOLDER/studentleftframe.png")
        img_left = img_left.resize((495, 210))  # Adjust the size to fit the label frame
        self.Photoimg_left = ImageTk.PhotoImage(img_left)

        # Place the left frame image inside the left_frame
        lbl_left = Label(left_frame, image=self.Photoimg_left)
        lbl_left.place(x=5, y=0, width=500, height=210)  

          #student frame detail left frame 
        student_frame = LabelFrame(left_frame, bd=2, bg="#FF5757", relief="groove", text="Student Information", font=("Times New Roman", 14, "bold"))
        student_frame.place(x=5, y=210, width=480, height=280)

         # Student name
        student_name = Label(student_frame, text="Name", font=("Times New Roman", 13, "bold"), bg="white")
        student_name.grid(row=1, column=0, padx=10, pady=5, sticky="W")

        StudentName_entry = Entry(student_frame,textvariable=self.var_name,  font=("Times New Roman", 13, "bold"), width=30, relief="sunken")
        StudentName_entry.grid(row=1, column=1, padx=10, sticky="W")

        # Roll no (beside name)
        Roll_NO = Label(student_frame, text="Roll NO.", font=("Times New Roman", 13, "bold"), bg="white")
        Roll_NO.grid(row=2, column=0, padx=10, pady=5, sticky="W")

        ROLLNO_entry = Entry(student_frame, textvariable=self.var_roll,font=("Times New Roman", 13, "bold"), width=10, relief="sunken")
        ROLLNO_entry.grid(row=2, column=1, padx=10, sticky="W")

         # Standard
        standard = Label(student_frame, text="Standard", font=("Times New Roman", 13, "bold"), bg="white")
        standard.grid(row=3, column=0, padx=10, pady=5, sticky="W")

        standard_combo = ttk.Combobox(student_frame, textvariable=self.var_std,font=("Times New Roman", 13, "bold"), width=10, state="readonly")
        standard_combo["values"] = ("Select", "I", "II", "III", "IV", "V", "VI", "VII", "VIII","IX","X")
        standard_combo.current(0)

        standard_combo.grid(row=3, column=1, padx=2, pady=5, sticky="W")

        # Fees (beside standard without gap)
        Fees = Label(student_frame, text="Fees", font=("Times New Roman", 13, "bold"), bg="white")
        Fees.grid(row=4, column=0, padx=10, pady=5, sticky="W")

        Fees_entry = Entry(student_frame,textvariable=self.var_fess,  font=("Times New Roman", 13, "bold"), width=10, relief="sunken")
        Fees_entry.grid(row=4, column=1, padx=0, pady=5, sticky="W")

          # DOB Label
        Date = Label(student_frame, text="IN-Date", font=("Times New Roman", 12, "bold"), bg="white")
        Date.grid(row=5, column=0, padx=10, pady=5, sticky="W")

        # DOB Entry Field with Calendar
        Date_entry = DateEntry(student_frame,textvariable=self.var_In,width=15, font=("Times New Roman", 12, "bold"), background='darkblue', foreground='white', date_pattern='dd-mm-y')
        Date_entry.grid(row=5, column=1, padx=10, pady=5, sticky="W")

         # Phone number
        Phone = Label(student_frame, text="Phone No.", font=("Times New Roman", 12, "bold"), bg="white")
        Phone.grid(row=6, column=0, padx=10, pady=5, sticky="W")

        Phone_entry = ttk.Entry(student_frame,textvariable=self.var_phone,font=("Times New Roman", 12, "bold"), width=15)
        Phone_entry.grid(row=6, column=1, padx=10, sticky="W")

        # Standard
        subject = Label(student_frame, text="Subject", font=("Times New Roman", 13, "bold"), bg="white")
        subject.grid(row=7, column=0, padx=10, pady=5, sticky="W")

        subject_combo = ttk.Combobox(student_frame,textvariable=self.var_subject, font=("Times New Roman", 13, "bold"), width=10, state="readonly")
        subject_combo["values"] = ("Select", "All", "English", "Hindi", "Geography", "Science", "Marathi", "Maths", "History")
        subject_combo.current(0)
        subject_combo.grid(row=7, column=1, padx=2, pady=5, sticky="W")

        


      

         # Button frame
        btn_frame = Frame(left_frame, bd=2, relief="ridge", bg="white")
        btn_frame.place(x=6, y=488, width=480, height=180)

        # Save button
        save_btn = Button(btn_frame,text="Save", bd=2, width=41, height=1, font=("Times New Roman", 14, "bold"), bg="#FF5757",fg="white",command=self.add_function)
        save_btn.grid(row=0, column=0,padx=10, pady=2, sticky="W")

         # update button
        update_btn = Button(btn_frame,text="Update", bd=2, width=41, height=1, font=("Times New Roman", 14, "bold"), bg="#FF5757",fg="white",command=self.update_fun)
        update_btn.grid(row=1, column=0,padx=10, pady=2, sticky="W")

         # delete button
        delete_btn = Button(btn_frame,text="Delete", bd=2, width=41, height=1, font=("Times New Roman", 14, "bold"), bg="#FF5757",fg="white",command=self.delete_function)
        delete_btn.grid(row=2, column=0,padx=10, pady=4, sticky="W")

        # reset button
        reset_btn = Button(btn_frame,text="Reset", bd=2, width=41, height=1, font=("Times New Roman", 14, "bold"), bg="#FF5757",fg="white")
        reset_btn.grid(row=3, column=0,padx=10, pady=4, sticky="W")

          #Right side label frame
        right_frame = LabelFrame(frame1, bd=2, bg="white", relief="ridge", font=("Times New Roman", 15, "bold"))
        right_frame.place(x=520, y=3, width=960, height=675)

        # Search system
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief="ridge",text="Search System",  font=("Times New Roman", 14, "bold"))
        search_frame.place(x=5, y=5, width=948, height=80)

        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search,font=("Times New Roman", 13, "bold"), width=25, state="readonly")
        search_combo["values"] = ("Select", "Roll No", "Standard", "Student Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky="W")

        search_entry = ttk.Entry(search_frame, width=25,font=("Times New Roman", 13, "bold") )
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky="W")

        search_btn = Button(search_frame, text="Search", font=("Times New Roman", 12, "bold"), width=23, bg="royal blue", fg="white")
        search_btn.grid(row=0, column=4, padx=5)

        showAll_btn = Button(search_frame, text="Show All", font=("Times New Roman", 12, "bold"), width=22, bg="royal blue", fg="white")
        showAll_btn.grid(row=0, column=6, padx=5)

                # Table frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief="ridge")
        table_frame.place(x=5, y=93, width=945, height=570)

        # Scrollbars for the table
        scroll_x = Scrollbar(table_frame, orient="horizontal")
        scroll_y = Scrollbar(table_frame, orient="vertical")

        self.student_table = ttk.Treeview(table_frame,column=("Name", "RollNo", "Standard", "Fees", "In-Date", "Phone No.", "Subject"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        # Configure and pack the scrollbars
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        

        self.student_table.heading("Name", text="Name")
        self.student_table.heading("RollNo", text="RollNo")
        self.student_table.heading("Standard", text="Standard")
        self.student_table.heading("Fees", text="Fees")
        self.student_table.heading("In-Date", text="In-Date")
        self.student_table.heading("Phone No.", text="Phone No.")
        self.student_table.heading("Subject", text="Subject")
        self.student_table["show"] = "headings"

        # Set column width for each heading
        self.student_table.column("Name", width=100)
        self.student_table.column("RollNo", width=100)
        self.student_table.column("Standard", width=100)
        self.student_table.column("Fees", width=100)
        self.student_table.column("In-Date", width=100)
        self.student_table.column("Phone No.", width=100)
        self.student_table.column("Subject", width=150)
        self.student_table.pack(fill="both", expand=1)
        # Bind the <<TreeviewSelect>> event to the fetch_data method
        self.student_table.bind("<<TreeviewSelect>>", self.fetch_data)
        


        
       
       #calling a function add_data function 

        self.add_data()


    def add_data(self):
    # Establish MySQL connection
     conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
     cursor = conn.cursor()
     cursor.execute("SELECT * from data")
     rows = cursor.fetchall()
    
    # Clear existing rows in the table
     self.student_table.delete(*self.student_table.get_children())
    
    # Insert new rows
     for row in rows:
        self.student_table.insert('', tk.END, values=row)
    
     conn.commit()
     conn.close()

     # adding data from front page
    

    def add_function(self):
        # Check if required fields are filled
        if self.var_roll.get() == "" or self.var_name.get() == "" or self.var_std.get() == "":
            messagebox.showerror("Error!", "Please fill all the required fields")
        else:
            try:
                # Connect to the MySQL database
                conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
                cursor = conn.cursor()
                
                # Modified SQL statement to include 'name' column
                sql = """
                    INSERT INTO data (name, roll, std, fess, date, phone, subject, search)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_std.get(),
                    self.var_fess.get(),
                    self.var_In.get(),
                    self.var_phone.get(),
                    self.var_subject.get(),
                    self.var_search.get()
                )
                
                # Execute SQL command
                cursor.execute(sql, values)
                
                # Commit changes to the database
                conn.commit()
                
                # Confirmation message
                messagebox.showinfo("Success", "Data has been added successfully!")
                
                # Clear input fields if desired
                self.reset_fields()

                # Refresh table
                self.add_data()
                
            except pymysql.MySQLError as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
            finally:
               conn.close()
               
        
    def fetch_data(self, event):
        # Get the selected row from the Treeview
         selected_row = self.student_table.focus()

        # Retrieve the row data
         row_data = self.student_table.item(selected_row)
         row = row_data['values']

        # Set the values in the respective StringVar variables if a row is selected
         if row:
            self.var_name.set(row[0])     # Set 'Name'
            self.var_roll.set(row[1])     # Set 'RollNo'
            self.var_std.set(row[2])      # Set 'Standard'
            self.var_fess.set(row[3])     # Set 'Fees'
            self.var_In.set(row[4])       # Set 'In-Date'
            self.var_phone.set(row[5])    # Set 'Phone No.'
            self.var_subject.set(row[6])  # Set 'Subject'
    def update_fun(self):
    # Check if required fields are filled
     if self.var_roll.get() == "" or self.var_name.get() == "" or self.var_std.get() == "":
        messagebox.showerror("Error!", "Please select a record to update and ensure all fields are filled")
     else:
        try:
            # Connect to the MySQL database
            conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
            cursor = conn.cursor()
            
            # Update SQL query to modify the existing record
            sql = """
                UPDATE data
                SET name=%s, std=%s, fess=%s, date=%s, phone=%s, subject=%s
                WHERE roll=%s
            """
            values = (
                self.var_name.get(),
                self.var_std.get(),
                self.var_fess.get(),
                self.var_In.get(),
                self.var_phone.get(),
                self.var_subject.get(),
                self.var_roll.get()  # Roll No used as identifier
            )
            
            # Execute the SQL command
            cursor.execute(sql, values)
            conn.commit()
            
            # Confirmation message
            messagebox.showinfo("Success", "Data has been updated successfully!")
            
            # Refresh table and clear fields
            self.add_data()
            self.reset_fields()
        
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
        finally:
            conn.close()
    

    def delete_function(self):
     if self.var_name.get() == "":
        messagebox.showerror("Error!", "Please select a student record to delete.")
     else:
        try:
            confirm = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete all records for this student?")
            if confirm:
                # Connect to the MySQL database
                conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
                cursor = conn.cursor()
                
                # Debug: Print the name being used to delete
                print(f"Attempting to delete records for student: {self.var_name.get()}")

                # SQL query to delete all records for the selected student's name
                sql = "DELETE FROM data WHERE name=%s"
                values = (self.var_name.get(),)
                
                # Execute the SQL command
                cursor.execute(sql, values)
                
                # Check if rows were actually deleted
                if cursor.rowcount == 0:
                    messagebox.showerror("Error", "No records found for this student.")
                else:
                    conn.commit()
                    messagebox.showinfo("Success", "All records for the student have been deleted successfully!")
                
                # Refresh table and clear fields
                self.add_data()
                self.reset_fields()
        
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            print(f"Database error: {e}")  # Debug
        finally:
            conn.close()



    
              





    
                    
                
                
    

        




       
    def on_resize(self, event):
      print(f"New size: {event.width}x{event.height}") 
                


if __name__ == "__main__":
    root = Tk()
    obj = student_detail(root)
    root.mainloop()

     

        



        











       


        

       

        





        
        

        
        


        








        




         




       



   
