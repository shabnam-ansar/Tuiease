from tkinter import Tk ,Label,Frame,LabelFrame,Button,StringVar
from PIL import Image, ImageTk 
from tkinter import ttk
import pymysql
from tkinter import messagebox

class report:
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

        self.var_search=StringVar()
        self.var_search_by=StringVar()

        # bg size
        self.bglabel = Label(self.root, image=self.background)
        self.bglabel.place(x=10, y=0)

        # Add a title label
        self.bg_title = Label(self.root, text="View Result", font=("Times New Roman", 30, "bold"), border=15, bg="white", fg="#FF5757")
        self.bg_title.place(x=10, y=10, height=40,width=1500)


          ##-----widgets-------
         # Main frame
        frame1 = Frame(self.root, bd=2, bg="white")
        frame1.place(x=15, y=70, width=1495, height=690)

        
      # LabelFrame for Search Section
        search_frame = LabelFrame(frame1, bd=2, bg="#FF5757", relief="groove", text="SEARCH BY", font=("Times New Roman", 25, "bold"), fg="white")
        search_frame.place(x=20, y=30, width=1450, height=140)

      # ComboBox for Search Options
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search_by,font=("Times New Roman", 19, "bold"), width=30, state="readonly")
        search_combo["values"] = ("Select", "Roll No", "Subject", "Student Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=0, padx=10, pady=10, sticky="W")

      # Entry Field for Search Input
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search, width=40, font=("Times New Roman", 19, "bold"))
        search_entry.grid(row=0, column=1, padx=10, pady=10, sticky="W")

      # Search Button
        search_btn = Button(search_frame, text="Search", font=("Times New Roman", 15, "bold"), width=35, bg="royal blue", fg="white",command=self.search)
        search_btn.grid(row=0, column=2, columnspan=2, pady=20)  # Center the button

         # New Frame for Labels
        data_frame = Frame(frame1, bd=2, bg="white", relief="groove")
        data_frame.place(x=20, y=200, width=1450, height=470)

    
        headers = ["Roll No.", "Name", "Standard", "Semester", "Obt. Marks", "Full Marks", "Subject"]
        col_widths = [205, 205, 205, 205, 205, 205, 209]

        for i, header in enumerate(headers):
            Label(
                data_frame,
                text=header,
                font=("Times New Roman", 15, "bold"),
                bg="white",
                bd=2,
                relief="groove",
            ).place(x=sum(col_widths[:i]), y=5, width=col_widths[i], height=50)

        # Dynamic Rows
        self.row_labels = []
        for row in range(7):  # Number of rows
            row_widgets = []
            for col, width in enumerate(col_widths):
                lbl = Label(
                    data_frame,
                    font=("Times New Roman", 15, "bold"),
                    bg="white",
                    bd=2,
                    relief="groove",
                )
                lbl.place(x=sum(col_widths[:col]), y=55 + row * 51, width=width, height=50)
                row_widgets.append(lbl)
            self.row_labels.append(row_widgets)

                # delete Button
        delete_btn = Button(data_frame, text="Delete", font=("Times New Roman", 15, "bold"), width=35, bg="red", fg="black",command=self.delete)
        delete_btn.place(x=5,y=413,width=710,height=50)
        clear_btn = Button(data_frame, text="Clear", font=("Times New Roman", 15, "bold"), width=35, bg="grey", fg="black",command=self.clear)
        clear_btn.place(x=712,y=413,width=725,height=50)




    def search(self):
       """Search for a record in the database and display it."""
       search_by = self.var_search_by.get()
       search_value = self.var_search.get().strip()

       if search_by == "Select" or not search_value:
        messagebox.showerror("Error", "Please select a search criteria and enter a search term!")
        return

       column_map = {
        "Roll No": "roll",
        "Subject": "subject",
        "Student Name": "name",
         }
       db_column = column_map.get(search_by)
       try:
           # Connect to the database
            conn = pymysql.connect(
                host="localhost",  # Replace with your host
                user="root",       # Replace with your username
                password="",       # Replace with your password
                database="result"  # Replace with your database name
            )
            cur = conn.cursor()
            query = f"SELECT roll, name, std, sem, obt, full, subject FROM result WHERE {db_column} LIKE %s"
            cur.execute(query, (f"%{search_value}%",))
            rows = cur.fetchall()

             # Clear previous rows
            for row_widgets in self.row_labels:
                for lbl in row_widgets:
                    lbl.config(text="")

            if rows:
                # If records found, update the UI
                for idx, row in enumerate(rows):
                    for col_idx, value in enumerate(row):
                        self.row_labels[idx][col_idx].config(text=value)
            else:
                # If no records are found
                messagebox.showinfo("No Records", "No records found matching the search criteria.")

            conn.close()
       

           
       except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")



    def delete(self):
        """Delete selected record from the database."""
        selected_roll = self.var_search.get().strip()

        if not selected_roll:
            messagebox.showerror("Error", "Please enter a Roll No. to delete!")
            return

        try:
            # Connect to the database
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="result"
            )
            cur = conn.cursor()
            # Query to delete the record based on roll number
            cur.execute("DELETE FROM result WHERE roll = %s", (selected_roll,))
            conn.commit()
            messagebox.showinfo("Success", f"Record with Roll No. {selected_roll} deleted successfully!")

            conn.close()
            self.clear()  # Clear the fields after deletion
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    
    def clear(self):
        """Clear the search input and results."""
        self.var_search.set("")  # Clear search input
        self.var_search_by.set("Select")  # Reset search combo box
        # Clear all result rows
        for row_widgets in self.row_labels:
            for lbl in row_widgets:
                lbl.config(text="")

   





    def on_resize(self, event):
      print(f"New size: {event.width}x{event.height}") 
                


if __name__ == "__main__":
    root = Tk()
    obj = report(root)
    root.mainloop()