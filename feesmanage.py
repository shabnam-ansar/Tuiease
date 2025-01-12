from tkinter import Tk, Label, Button,LabelFrame,Frame,Entry,Scrollbar,StringVar
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
import pymysql #ignore
import tkinter as tk
from tkinter import messagebox




class fees:
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
        self.bg_title = Label(self.root, text="FEES RECORD", font=("Times New Roman", 30, "bold"), border=12, bg="#FF5757", fg="white")
        self.bg_title.place(x=10, y=10, width=1500)

        # Main frame
        frame1 = Frame(self.root, bd=2, bg="white")
        frame1.place(x=15, y=65, width=1495, height=690)

        #-------variable---------
        self.var_name=StringVar()
        self.var_month=StringVar()
        self.var_paid=StringVar()
        self.var_amount=StringVar()
        self.var_mode=StringVar()
        self.var_note=StringVar()
        self.var_date=StringVar()
        self.var_search=StringVar()
        

        # Left side label frame
        left_frame = LabelFrame(frame1, bd=2, bg="white", relief="groove", font=("Times New Roman", 15, "bold"))
        left_frame.place(x=10, y=5, width=500, height=675)

        # Left frame image
        img_left = Image.open("IMG FOLDER/feesmanage.png")
        img_left = img_left.resize((495, 210))  # Adjust the size to fit the label frame
        self.Photoimg_left = ImageTk.PhotoImage(img_left)

        # Place the left frame image inside the left_frame
        lbl_left = Label(left_frame, image=self.Photoimg_left)
        lbl_left.place(x=5, y=0, width=500, height=210)  

        #student frame detail left frame 
        student_frame = LabelFrame(left_frame, bd=2, bg="#FF5757", relief="groove", text="Student Information", font=("Times New Roman", 14, "bold"))
        student_frame.place(x=5, y=210, width=500, height=280)
        # Student name
        student_name = Label(student_frame, text="Name", font=("Times New Roman", 13, "bold"), bg="white")
        student_name.grid(row=1, column=0, padx=10, pady=5, sticky="W")
        StudentName_entry = Entry(student_frame, font=("Times New Roman", 13, "bold"), width=30, relief="sunken", textvariable=self.var_name)
        StudentName_entry.grid(row=1, column=1, padx=10, sticky="W")

        # Month
        month = Label(student_frame, text="Month", font=("Times New Roman", 13, "bold"), bg="white")
        month.grid(row=2, column=0, padx=10, pady=5, sticky="W")
        month_combo = ttk.Combobox(student_frame, font=("Times New Roman", 13, "bold"), width=10, state="readonly", textvariable=self.var_month)
        month_combo["values"] = ("Select", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        month_combo.current(0)
        month_combo.grid(row=2, column=1, padx=2, pady=5, sticky="W")

        # Paid
        paid = Label(student_frame, text="Is fee paid", font=("Times New Roman", 13, "bold"), bg="white")
        paid.grid(row=3, column=0, padx=10, pady=5, sticky="W") 
        paid_combo = ttk.Combobox(student_frame, font=("Times New Roman", 13, "bold"), width=10, state="readonly", textvariable=self.var_paid)
        paid_combo["values"] = ("Select", "Yes", "No")
        paid_combo.current(0)
        paid_combo.grid(row=3, column=1, padx=2, pady=5, sticky="W")

      # Amount
        amount = Label(student_frame, text="Amount", font=("Times New Roman", 13, "bold"), bg="white")
        amount.grid(row=4, column=0, padx=10, pady=5, sticky="W")
        amount_entry = Entry(student_frame, font=("Times New Roman", 13, "bold"), width=10, relief="sunken", textvariable=self.var_amount)
        amount_entry.grid(row=4, column=1, padx=10, sticky="W")

     # Payment mode
        mode = Label(student_frame, text="Payment Mode", font=("Times New Roman", 13, "bold"), bg="white")
        mode.grid(row=5, column=0, padx=10, pady=5, sticky="W")

        mode_combo = ttk.Combobox(student_frame, font=("Times New Roman", 13, "bold"), width=10, state="readonly", textvariable=self.var_mode)
        mode_combo["values"] = ("Select", "Online", "Offline")
        mode_combo.current(0)
        mode_combo.grid(row=5, column=1, padx=2, pady=5, sticky="W")

     # Note = roll no.  
        note = Label(student_frame, text="Roll no.", font=("Times New Roman", 13, "bold"), bg="white")
        note.grid(row=6, column=0, padx=10, pady=5, sticky="W")

        note_entry = Entry(student_frame, font=("Times New Roman", 13, "bold"), width=10, relief="sunken", textvariable=self.var_note)
        note_entry.grid(row=6, column=1, padx=10, sticky="W")

     # Payment Date
        Date = Label(student_frame, text="Payment-Date", font=("Times New Roman", 12, "bold"), bg="white")
        Date.grid(row=7, column=0, padx=10, pady=5, sticky="W")

        Date_entry = DateEntry(student_frame, width=15, font=("Times New Roman", 12, "bold"), background='darkblue', foreground='white', date_pattern='dd-mm-y', textvariable=self.var_date)
        Date_entry.grid(row=7, column=1, padx=10, pady=5, sticky="W")


         

         # Button frame
        btn_frame = Frame(left_frame, bd=2, relief="ridge", bg="white")
        btn_frame.place(x=6, y=500, width=480, height=170)

        # Save button
        save_btn = Button(btn_frame,text="Save", bd=2, width=41, height=1, font=("Times New Roman", 14, "bold"), bg="#FF5757",fg="white",command=self.add_function)
        save_btn.grid(row=0, column=0,padx=10, pady=1, sticky="W")

         # update button
        update_btn = Button(btn_frame,text="Update", bd=2, width=41, height=1, font=("Times New Roman", 14, "bold"), bg="#FF5757",fg="white",command=self.update_fun)
        update_btn.grid(row=1, column=0,padx=10, pady=1, sticky="W")

         # delete button
        delete_btn = Button(btn_frame,text="Delete", bd=2, width=41, height=1, font=("Times New Roman", 14, "bold"), bg="#FF5757",fg="white",command=self.delete_function)
        delete_btn.grid(row=2, column=0,padx=10, pady=1, sticky="W")

        # reset button
        reset_btn = Button(btn_frame,text="Reset", bd=2, width=41, height=1, font=("Times New Roman", 14, "bold"), bg="#FF5757",fg="white",command=self.reset_function)
        reset_btn.grid(row=3, column=0,padx=10, pady=1, sticky="W")

        #Right side label frame
        right_frame = LabelFrame(frame1, bd=2, bg="white", relief="ridge", font=("Times New Roman", 15, "bold"))
        right_frame.place(x=520, y=3, width=960, height=675)

        # Search system
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief="ridge",text="Search System",  font=("Times New Roman", 14, "bold"))
        search_frame.place(x=5, y=5, width=948, height=80)

        #amount
        search_name= Label(search_frame, text="Student name ", font=("Times New Roman", 13, "bold"), bg="white")
        search_name.grid(row=0, column=0, padx=10, pady=5, sticky="W")

        search_entry = Entry(search_frame, font=("Times New Roman", 13, "bold"), width=35, relief="sunken")
        search_entry.grid(row=0, column=1, padx=10, sticky="W")

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

        self.student_table = ttk.Treeview(table_frame,column=("Name", "Month", "Paid-or-Not", "Amount", "Payment-mode", "Note", "Year"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        # Configure and pack the scrollbars
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Month", text="Month")
        self.student_table.heading("Paid-or-Not", text="Paid-or-Not")
        self.student_table.heading("Amount", text="Amount")
        self.student_table.heading("Payment-mode", text="Payment-mode")
        self.student_table.heading("Note", text="Roll NO")
        self.student_table.heading("Year", text="Date")
        self.student_table["show"] = "headings"

        # Set column width for each heading
        self.student_table.column("Name", width=100)
        self.student_table.column("Month", width=100)
        self.student_table.column("Paid-or-Not", width=100)
        self.student_table.column("Amount", width=100)
        self.student_table.column("Payment-mode", width=100)
        self.student_table.column("Note", width=100)
        self.student_table.column("Year", width=150)
        self.student_table.pack(fill="both", expand=1)

        # bindding data

        self.student_table.bind("<<TreeviewSelect>>", self.select_data)

        #caliing fetch function
        self.fetch_data()


    def fetch_data(self):
      conn = pymysql.connect(host="localhost", user="root", password="", database="fees")
      cursor = conn.cursor()
      cursor.execute("SELECT * from fees")
      rows = cursor.fetchall()
    
    # Clear existing rows in the table
      self.student_table.delete(*self.student_table.get_children())
    
    # Insert new rows
      for row in rows:
        self.student_table.insert('', tk.END, values=row)
    
      conn.commit()
      conn.close()

      #add function
    def add_function(self):
        # Check if required fields are filled
        if self.var_name.get() == "" or self.var_paid.get() == "" or self.var_month.get() == "":
            messagebox.showerror("Error!", "Please fill all the required fields")
        else:
            conn = pymysql.connect(host="localhost", user="root", password="", database="fees")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO fees(name, month, paid ,amount,mode,note,date) VALUES(%s,%s,%s,%s,%s,%s,%s)",(self.var_name.get(),self.var_month.get(),self.var_paid.get(),self.var_amount.get(),self.var_mode.get(),self.var_note.get(),self.var_date.get()))
            conn.commit()
            conn.close()
            self.fetch_data()
    def add_function(self):
        # Check if required fields are filled
        
        if (self.var_name.get() == "" or
        self.var_month.get() == "Select" or
        self.var_paid.get() == "Select" or
        self.var_amount.get() == "" or
        self.var_mode.get() == "Select" or
        self.var_date.get() == ""):
         messagebox.showerror("Error!", "Please fill all the required fields!")
   
        else:
            try:
                # Connect to the MySQL database
                conn = pymysql.connect(host="localhost", user="root", password="", database="fees")
                cursor = conn.cursor()
                
                # Modified SQL statement to include 'name' column
                sql = """
                    INSERT INTO fees (name,month,paid,amount,mode, note,date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                values = (
                    self.var_name.get(),
                    self.var_month.get(),
                    self.var_paid.get(),
                    self.var_amount.get(),
                    self.var_mode.get(),
                    self.var_note.get(),
                    self.var_date.get(),
                    
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
    def reset_function(self):
             self.var_name.set("")
             self.var_month.set("Select")
             self.var_paid.set("Select")
             self.var_amount.set("")
             self.var_mode.set("Select")
             self.var_note.set("")
             self.var_date.set("")
    def select_data(self, event):
        # Get the selected row from the Treeview
         selected_row = self.student_table.focus()

        # Retrieve the row data
         row_data = self.student_table.item(selected_row)
         row = row_data['values']

        # Set the values in the respective StringVar variables if a row is selected
         if row:
            self.var_name.set(row[0])     # Set 'Name'
            self.var_month.set(row[1])     # Set 'RollNo'
            self.var_paid.set(row[2])      # Set 'Standard'
            self.var_amount.set(row[3])     # Set 'Fees'
            self.var_mode.set(row[4])       # Set 'In-Date'
            self.var_note.set(row[5])    # Set 'Phone No.'
            self.var_date.set(row[6])  # 
    def update_fun(self):
    # Check if required fields are filled
     if (self.var_name.get() == "" or
        self.var_month.get() == "Select" or
        self.var_paid.get() == "Select"):
        messagebox.showerror("Error!", "Please fill all the required fields")
     else:
        try:
            # Connect to the MySQL database
            conn = pymysql.connect(host="localhost", user="root", password="", database="fees")
            cursor = conn.cursor()

            # Modified SQL statement to update the record
            sql = """
                UPDATE fees
                SET name=%s,month=%s, paid=%s, amount=%s, mode=%s, date=%s
                Where note=%s
                
            """
            values = (
                self.var_month.get(),
                self.var_paid.get(),
                self.var_amount.get(),
                self.var_mode.get(),
                self.var_note.get(),
                self.var_date.get(),
                self.var_name.get()  # Unique identifier
            )

            # Execute SQL command
            cursor.execute(sql, values)

            # Commit changes to the database
            conn.commit()

            # Confirmation message
            messagebox.showinfo("Success", "Data has been updated successfully!")

            # Clear input fields
            self.reset_function()

            # Refresh table
            self.fetch_data()

        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
        finally:
            conn.close()


    def delete_function(self):
    # Check if a student is selected
     if self.var_note.get() == "":
        messagebox.showerror("Error!", "Please select a student to delete!")
     else:
        try:
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
            if confirm:
                # Connect to the database
                conn = pymysql.connect(host="localhost", user="root", password="", database="fees")
                cursor = conn.cursor()

                # Delete the record based on the unique identifier (note/roll number)
                sql = "DELETE FROM fees WHERE note=%s"
                cursor.execute(sql, (self.var_note.get(),))

                # Commit changes
                conn.commit()
                conn.close()

                # Confirmation message
                messagebox.showinfo("Deleted", "Record deleted successfully!")

                # Refresh table
                self.fetch_data()

                # Clear the fields
                self.reset_function()
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

   



    
    

        
         
    



       
      


    
        

    

        

        




      


































 
   

      
    def on_resize(self, event):
      print(f"New size: {event.width}x{event.height}") 
                


if __name__ == "__main__":
    root = Tk()
    obj = fees(root)
    root.mainloop()

