from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognition System")


        self.var_name= StringVar()
        self.var_time = StringVar()
        self.var_rollno = StringVar()
        self.var_department = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()
        # Header Images
        img1 = Image.open(r"D:\face recognition attendence system\student management system\images\right1.jpg")
        img1 = img1.resize((860, 200), Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=0, y=0, width=860, height=200)

        img2 = Image.open(r"D:\face recognition attendence system\student management system\images\right2.jpg")
        img2 = img2.resize((860, 200), Image.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=500, y=0, width=860, height=200)

        # Background Image
        img3 = Image.open(r"D:\face recognition attendence system\student management system\images\student5.jpg")
        img3 = img3.resize((1530, 800), Image.BICUBIC)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=800)

        # Title
        title_lbl = Label(bg_img, text="Attendance Management System", font=("Times New Roman", 28, "bold"), bg="darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # Main Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=30, y=50, width=1300, height=515)

        # Left Frame
        left_frame = LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Students Attendance Details", font=("New Times Roman", 12, "bold"))
        left_frame.place(x=10, y=6, width=660, height=500)

       



        # Left Frame Image
        img_left = Image.open(r"D:\face recognition attendence system\student management system\images\student10.jpeg")
        img_left = img_left.resize((660, 130), Image.BICUBIC)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(left_frame, image=self.photoimg_left).place(x=0, y=0, width=660, height=130)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=135, width=650, height=330)

        # Labels and Entries

        Label(left_inside_frame, text="Name:", font=("New Times Roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(left_inside_frame, width=15, textvariable=self.var_name, font=("New Times Roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=10, sticky=W)


        Label(left_inside_frame, text="Time:", font=("New Times Roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(left_inside_frame, width=15, textvariable=self.var_time, font=("New Times Roman", 12, "bold")).grid(row=1, column=1, padx=10, pady=10, sticky=W)


        Label(left_inside_frame, text="Roll:", font=("New Times Roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=10, sticky=W)
        ttk.Entry(left_inside_frame, width=15, textvariable= self.var_rollno, font=("New Times Roman", 12, "bold")).grid(row=0, column=3, padx=10, pady=10, sticky=W)

        Label(left_inside_frame, text="Department:", font=("New Times Roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=10, sticky=W)
        ttk.Entry(left_inside_frame, width=15, textvariable=self.var_department , font=("New Times Roman", 12, "bold")).grid(row=1, column=3, padx=10, pady=10, sticky=W)

        Label(left_inside_frame, text="Date:", font=("New Times Roman", 12, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=10, sticky=W)
        ttk.Entry(left_inside_frame, width=15, textvariable=self.var_date, font=("New Times Roman", 12, "bold")).grid(row=2, column=3, padx=10, pady=10, sticky=W)



        studentgender_label = Label(left_inside_frame,text="Attendance Status :",font=("new times roman",12,"bold"),bg="white")
        studentgender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo = ttk.Combobox(left_inside_frame,  textvariable=self. var_attendance,font=("times new roman",12,"bold"),state="Read Only",width=15)
        gender_combo["values"] = ("Status","Present","Absent")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)


        # Button Frame
        btn_frame = Frame(left_inside_frame,bg="white", bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=290, width=650, height=30) 

        save_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=17, height=1, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv",command=self.exportCsv, width=17, height=1, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", command= self.updateData, width=17, height=1, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command= self.reset_data , width=17, height=1, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)


         #RIGHT FRAME

        Right_frame = LabelFrame(main_frame,bg="White", bd=2,relief=RIDGE,text= "Attendance Details", font=("new times roman",12,"bold"))
        Right_frame.place(x=680,y=5,width=600,height=500)

        table_frame = Frame(Right_frame,bg="White", bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=590,height=445)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient= VERTICAL)
        self.attendance_ReportTable = ttk.Treeview(table_frame, columns=("roll","name","department","time","date","attendance"),xscrollcommand = scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill =X)
        scroll_y.pack(side = RIGHT, fill =Y)
        scroll_x.config(command=self.attendance_ReportTable.xview)
        scroll_y.config(command=self.attendance_ReportTable.yview)


        self.attendance_ReportTable.heading("roll", text="Roll no")
        self.attendance_ReportTable.heading("name", text="Name")
        self.attendance_ReportTable.heading("department", text="Department")
        self.attendance_ReportTable.heading("time", text="Time")
        self.attendance_ReportTable.heading("date", text="Date")
        self.attendance_ReportTable.heading("attendance", text="Attendance Stauts")

        self.attendance_ReportTable["show"] = "headings"


        self.attendance_ReportTable.column("roll", width = 120)
        self.attendance_ReportTable.column("name", width = 120)
        self.attendance_ReportTable.column("department", width = 120)
        self.attendance_ReportTable.column("time", width = 120)
        self.attendance_ReportTable.column("date", width = 120)
        self.attendance_ReportTable.column("attendance", width = 120) 


        self.attendance_ReportTable.pack(fill=BOTH,expand=1)

        self.attendance_ReportTable.bind("<ButtonRelease>", self.get_cursor)


    def fetch_data(self, rows):
        self.attendance_ReportTable.delete(*self.attendance_ReportTable.get_children())
        
        for i in rows:
            self.attendance_ReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
        
        if fln:  
            with open(fln, 'r') as myfile:
                csvread = csv.reader(myfile, delimiter=',')
                mydata.clear() 
                for i in csvread:
                    print(i) 
                    mydata.append(i)
                self.fetch_data(mydata)


    def exportCsv(self):
        try:
            if len(mydata) < 1: 
                messagebox.showerror("No data", "No data to export", parent=self.root)
                return False
                
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
            if fln: 
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i) 
                messagebox.showinfo("Success", f"Your data has been exported to {os.path.basename(fln)} successfully.")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    def get_cursor(self, event = ""):
        cursor_row = self.attendance_ReportTable.focus()
        content = self.attendance_ReportTable.item(cursor_row)
        rows = content['values']
        self.var_rollno.set(rows[0])
        self.var_name.set(rows[1])
        self.var_department.set(rows[2])
        self.var_time.set(rows[3])
        self.var_date.set(rows[4])
        self.var_attendance.set(rows[5])

    def reset_data(self):

        self.var_rollno.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")

    
    def updateData(self):
        try:
            cursor_row = self.attendance_ReportTable.focus()
            if not cursor_row:
                messagebox.showerror("Select Row", "Please select a row to update", parent=self.root)
                return
            
            rollno = self.var_rollno.get()
            name = self.var_name.get()
            department = self.var_department.get()
            time = self.var_time.get()
            date = self.var_date.get()
            attendance = self.var_attendance.get()

            self.attendance_ReportTable.item(cursor_row, values=(rollno, name, department, time, date, attendance))
            
            index = self.attendance_ReportTable.index(cursor_row)
            mydata[index] = [rollno, name, department, time, date, attendance]
            
            messagebox.showinfo("Success", "Attendance record updated successfully", parent=self.root)
            
            self.reset_data()
            
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    
    
                
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()