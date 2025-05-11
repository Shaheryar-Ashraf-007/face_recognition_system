from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os



class  Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognition system")
        
        #========== vARIABLES ================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_teacher = StringVar()
        self.var_address = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_photo = StringVar()
        
        
        
        img = Image.open(r"D:\face recognition attendence system\student management system\images\student6.jpg")
        img = img.resize((500,130),Image.BICUBIC)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl =Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        img1 = Image.open(r"D:\face recognition attendence system\student management system\images\student8.jpg")
        img1 = img1.resize((500,130),Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl =Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        
        img2 = Image.open(r"D:\face recognition attendence system\student management system\images\student7.jpg")
        img2 = img2.resize((500,130),Image.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl =Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        
        img3 = Image.open(r"D:\face recognition attendence system\student management system\images\student3.jpg")
        img3 = img3.resize((1530,800),Image.BICUBIC)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img =Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=800)
        
        
        title_lbl = Label(bg_img,text= "Students Handling Information",font=("Times new Romen",28,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=50)
        
        #main frame 
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=30,y=50,width=1300,height=515)
        
        #left frame
        
        left_frame = LabelFrame(main_frame,bg="White", bd=2,relief=RIDGE,text= "Students Details", font=("new times roman",12,"bold"))
        left_frame.place(x=10,y=6,width=660,height=500)
        
        
        img_left = Image.open(r"D:\face recognition attendence system\student management system\images\student10.jpeg")
        img_left = img_left.resize((660,130),Image.BICUBIC)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl =Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=50,y=220,width=650,height=130)
        
        #Current Course
        
        current_course_frame = LabelFrame(left_frame,bg="White",text="Current Course Information", bd=2,relief=RIDGE,font=("new times roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=640,height=110)
        
        #departments
        
        dep_label = Label(current_course_frame,text="Departments",font=("new times roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=2,pady=10)
        
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep,font=("times new roman",12,"bold"),state="Read Only")
        dep_combo["values"] = ("Select Departments","Computer Science","IT","Psychology","Public Administration","BBA","Food Science","Intermediate","Commerce")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course
        
        course_label = Label(current_course_frame,text="Course",font=("new times roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=2,pady=10)
        
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,font=("times new roman",12,"bold"),state="Read Only",width=25)
        dep_combo["values"] = ("Select Course","Introduction to Computing","Mathematics-I (Calculus and Analytical Geometry)","English Composition and Comprehension","Introduction to Programming (e.g., Python, Java, C++)","Digital Logic Design","Introduction to Computer Architecture","Professional Ethics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #year
        
        dep_label = Label(current_course_frame,text="Year",font=("new times roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=2,pady=10)
        
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,font=("times new roman",12,"bold"),state="Read Only")
        dep_combo["values"] = ("Select year","2010-12","2012-14","2014-16","2018-20","2020-22","2022-2024")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        
        
        dep_label = Label(current_course_frame,text="Semester",font=("new times roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=2,pady=10)
        
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem,font=("times new roman",12,"bold"),state="Read Only")
        dep_combo["values"] = ("Select Semester","1st","2nd","3rd","4th")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #Class Student Information
        
        class_student_frame = LabelFrame(left_frame,bg="White",text="Class Student Information:", bd=2,relief=RIDGE,font=("new times roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=645,height=225)
        
        #student ID
        
        student_label = Label(class_student_frame,text="Student ID:",font=("new times roman",12,"bold"),bg="white")
        student_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id,width=20,font=("new times roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Student name 
        studentname_label = Label(class_student_frame,text="Student Name:",font=("new times roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=8,pady=5,sticky=W)
        
        studentname_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name,width=14,font=("new times roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=8,pady=5,sticky=W)
        
        
        #teacher
        teacher_label = Label(class_student_frame,text="Teacher:",font=("new times roman",12,"bold"),bg="white")
        teacher_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        studentdevision_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher,width=20,font=("new times roman",12,"bold"))
        studentdevision_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #gender
        
        studentgender_label = Label(class_student_frame,text="Gender :",font=("new times roman",12,"bold"),bg="white")
        studentgender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,font=("times new roman",12,"bold"),state="Read Only",width=20)
        gender_combo["values"] = ("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        #ADDRESS
        studentaddress_label = Label(class_student_frame,text="Address :",font=("new times roman",12,"bold"),bg="white")
        studentaddress_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        studentroll_entry = ttk.Entry(class_student_frame, textvariable=self.var_address,width=14,font=("new times roman",12,"bold"))
        studentroll_entry.grid(row=1,column=3,padx=8,pady=5,sticky=W)
         
        #Email
        
        studentemail_label = Label(class_student_frame,text="Email:",font=("new times roman",12,"bold"),bg="white")
        studentemail_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        studentemail_entry = ttk.Entry(class_student_frame, textvariable=self.var_email,width=20,font=("new times roman",12,"bold"))
        studentemail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #phone
        
        studentphone_label = Label(class_student_frame,text="Phone:",font=("new times roman",12,"bold"),bg="white")
        studentphone_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        studentphone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone,width=14,font=("new times roman",12,"bold"))
        studentphone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
          #radio buttons 
        self.var_radio1 = StringVar()
        radiobtn1= ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample",value=YES)
        radiobtn1.grid(row=3,column=2,pady=0,sticky=W)
        
        radiobtn2= ttk.Radiobutton(class_student_frame, variable= self.var_radio1, text="No photo Sample",value=NO)
        radiobtn2.grid(row=3,column=3,pady=0,sticky=W)
        
        
        #buttons frame 
        
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=140,width=640,height=60)
        
        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=17,height=1,font=("times new roman",12,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=17,height=1,font=("times new roman",12,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=17,height=1,font=("times new roman",12,"bold"),bg="green",fg="white")
        delete_btn.grid(row=0,column=2)
        
        
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=17,height=1,font=("times new roman",12,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)
        
        take_photo_btn = Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=17,height=1,font=("times new roman",12,"bold"),bg="maroon",fg="white")
        take_photo_btn.grid(row=1,column=0,pady=0)
        
        update_photo_btn = Button(btn_frame,text="Update photo Sample",width=17,height=1,font=("times new roman",12,"bold"),bg="maroon",fg="white")
        update_photo_btn.grid(row=1,column=1,pady=0)
        
      
        #right frame 
        
        Right_frame = LabelFrame(main_frame,bg="White", bd=2,relief=RIDGE,text= "Students Details", font=("new times roman",12,"bold"))
        Right_frame.place(x=680,y=5,width=600,height=500)
        
        img_right = Image.open(r"D:\face recognition attendence system\student management system\images\right3.webp")
        img_right = img_right.resize((645,130),Image.BICUBIC)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl =Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=650,height=130)
        
        #==========Search System===================
        
        search_frame = LabelFrame(Right_frame,bg="White",text="Search System:", bd=2,relief=RIDGE,font=("new times roman",12,"bold"))
        search_frame.place(x=5,y=135,width=590,height=70)
        
        search_label = Label(search_frame,text="Search By:",font=("new times roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo = ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="Read Only",width=15)
        search_combo["values"] = ("Select ","id","phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry = ttk.Entry(search_frame,width=14,font=("new times roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=8,pady=5,sticky=W)
        
        search_btn = Button(search_frame,text="Search",width=8,height=1,font=("times new roman",12,"bold"),bg="green",fg="white")
        search_btn.grid(row=0,column=3)
        
        
        show_btn = Button(search_frame,text="Show All",width=7,height=1,font=("times new roman",12,"bold"),bg="green",fg="white")
        show_btn.grid(row=0,column=4,padx=4)
        
        table_frame = Frame(Right_frame,bg="White", bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=590,height=265)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient= VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("dep","course","year","sem","id","name","teacher","address", "gender","phone","email","photo"),xscrollcommand = scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill =X)
        scroll_y.pack(side = RIGHT, fill =Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student_id")
        self.student_table.heading("name", text="Studentname")
        self.student_table.heading("teacher", text="teacher")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("phone", text="Address")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("photo", text="PhotoSample")
        self.student_table["show"] = "headings"
        
        
        
        self.student_table.column("dep", width = 100)
        self.student_table.column("course", width = 100)
        self.student_table.column("year", width = 100)
        self.student_table.column("sem", width = 100)
        self.student_table.column("id", width = 100)
        self.student_table.column("name", width = 100)
        self.student_table.column("teacher", width = 100)
        self.student_table.column("address", width = 100)
        self.student_table.column("gender", width = 100)
        self.student_table.column("phone",width=100)
        self.student_table.column("email", width = 100)
        self.student_table.column("photo", width = 150)
       
    
    
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()
        
        #==========function Decleration===============
        
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Shery@#2003", database="student")
                print("invalid crediential",conn)
                my_cursor = conn.cursor()
                my_cursor.execute("insert into face1 values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_teacher.get(),
                    self.var_address.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                
    #=============data fetch =================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Shery@#2003", database="student")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from face1")
        data = my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())   
            for i in data :
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
        #===========get courser=======================
    
    def get_cursor (self,event = ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_teacher.set(data[6]),
        self.var_address .set(data[7]),
        self.var_gender.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_email.set(data[10]),
        self.var_radio1.set(data[11]) 
        
    def update_data(self):
        if self.var_dep.get() == "" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this data", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Shery@#2003", database="student")
                    if conn.is_connected():
                        print('Connected to MySQL database')
                        my_cursor = conn.cursor()
                        query = """UPDATE face1 
                                    SET dep = %s, Course = %s, Year = %s, sem = %s, 
                                        std_name = %s, teacher = %s, address = %s, gender = %s, 
                                        phone = %s, email = %s , photo = %s
                                    WHERE std_id = %s"""
                        my_cursor.execute(query, (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_std_name.get(),
                            self.var_teacher.get(),
                            self.var_address.get(),
                            self.var_gender.get(),
                            self.var_phone.get(),
                            self.var_email.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get() 
                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Student updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"DUE TO: {str(es)}", parent=self.root)
                
                
    #================= delete function ========================
    
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student", parent = self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Shery@#2003", database="student")
                    my_cursor = conn.cursor()
                    sql = "delete from face1 where std_id = %s"
                    val =(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Delete Student ", parent = self.root)
                
            except Exception as es:
                
                messagebox.showerror("Error", f"DUE TO: {str(es)}", parent=self.root)
                
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_teacher.set("")
        self.var_address.set("")
        self.var_gender.set("Male")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_radio1.set("")
        
        
    
    #============== Generate data set or take photo sample=======================
    
    def generate_dataset(self):         
        if self.var_dep.get() == "" or self.var_std_name.get() == "" or self.var_std_id.get() == "":             
            messagebox.showerror("Error", "All fields are required", parent=self.root)             
            return          

        try:       
            conn = mysql.connector.connect(
                host="localhost", 
                username="root", 
                password="Shery@#2003", 
                database="student"
            )
            my_cursor = conn.cursor()

            # ✅ Only check if student exists
            my_cursor.execute("SELECT * FROM face1 WHERE std_id = %s", (self.var_std_id.get(),))
            existing = my_cursor.fetchone()

            if not existing:
                messagebox.showwarning("Warning", "Student ID not found! Please register student first.", parent=self.root)
                conn.close()
                return

            conn.close()

            # ✅ Load Haar cascade classifier
            cascade_file_path = "D:\\face recognition attendence system\\student management system\\haarcascade_frontalface_default.xml"             
            face_classifier = cv2.CascadeClassifier(cascade_file_path)              

            if face_classifier.empty():                 
                print("Error: Failed to load cascade classifier")                 
                return              

            def face_cropped(img):                 
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                 
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)                 
                for (x, y, w, h) in faces:                     
                    return img[y:y+h, x:x+w]                 
                return None            

            data_folder = "data"             
            if not os.path.exists(data_folder):                
                os.makedirs(data_folder)              

            cap = cv2.VideoCapture(0)             
            img_id = 0              
            student_id = int(self.var_std_id.get())

            while True:    
                ret, my_frame = cap.read()
                if not ret:                     
                    print("Error: Failed to capture frame")                     
                    break                  

                face = face_cropped(my_frame)                 
                if face is not None:                     
                    img_id += 1                     
                    face = cv2.resize(face, (450, 450))                     
                    face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)                     
                    file_name = f"user.{student_id}.{img_id}.jpg"                     
                    file_path = os.path.join(data_folder, file_name)                      

                    cv2.imwrite(file_path, face_gray)                     
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)                     
                    cv2.imshow("Cropped Face", face)                  

                if cv2.waitKey(1) == 13 or img_id == 100:                     
                    break              

            cap.release()             
            cv2.destroyAllWindows()             
            messagebox.showinfo("Result", "Generating data sets completed!")          

        except Exception as es:             
            messagebox.showerror("Error", f"DUE TO: {str(es)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()















    # def generate_dataset(self):         
    # if self.var_dep.get() == "" or self.var_std_name.get() == "" or self.var_std_id.get() == "":             
    #     messagebox.showerror("Error", "All fields are required", parent=self.root)             
    #     return          

    # try:       
    #     conn = mysql.connector.connect(host="localhost", username="root", password="Shery@#2003", database="student")
    #     my_cursor = conn.cursor() 

    #     # Get the next available ID for a new student             
    #     my_cursor.execute("SELECT std_id FROM face1") 
    #     result = my_cursor.fetchone()
    #     id = (result[0] + 1) if result and result[0] is not None else 1  # Handle None safely                      

    #     # Insert new student information             
    #     my_cursor.execute(
    #         "INSERT INTO face1 (std_id, dep, course, year, sem, std_name, teacher, address, gender, phone, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",        
    #         (id, self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_sem.get(), self.var_std_name.get(), self.var_teacher.get(), self.var_address.get(), self.var_gender.get(), self.var_phone.get(), self.var_email.get())
    #     )            
    #     conn.commit()                          
    #     self.fetch_data()             
    #     self.reset_data()             
    #     conn.close()                          

    #     # Load the Haar cascade classifier for face detection             
    #     cascade_file_path = "D:\\face recognition attendence system\\student management system\\haarcascade_frontalface_default.xml"             
    #     face_classifier = cv2.CascadeClassifier(cascade_file_path)              

    #     if face_classifier.empty():                 
    #         print("Error: Failed to load cascade classifier")                 
    #         return              

    #     def face_cropped(img):                 
    #         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                 
    #         faces = face_classifier.detectMultiScale(gray, 1.3, 5)                 
    #         for (x, y, w, h) in faces:                     
    #             return img[y:y+h, x:x+w]                 
    #         return None  # Return None if no face is detected              

    #     data_folder = "data"             
    #     if not os.path.exists(data_folder):                
    #         os.makedirs(data_folder)              

    #     cap = cv2.VideoCapture(0)             
    #     img_id = 0              

    #     while True:                 
    #         ret, my_frame = cap.read()                 
    #         if not ret:                     
    #             print("Error: Failed to capture frame")                     
    #             break                  

    #         face = face_cropped(my_frame)                 
    #         if face is not None:                     
    #             img_id += 1                     
    #             face = cv2.resize(face, (450, 450))                     
    #             face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)                     
    #             file_name = f"user.{id}.{img_id}.jpg"                     
    #             file_path = os.path.join(data_folder, file_name)                      

    #             cv2.imwrite(file_path, face_gray)                     
    #             cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)                     
    #             cv2.imshow("Cropped Face", face)                  

    #         if cv2.waitKey(1) == 13 or img_id == 100:                     
    #             break              

    #     cap.release()             
    #     cv2.destroyAllWindows()             
    #     messagebox.showinfo("Result", "Generating data sets completed!")          

    # except Exception as es:             
    #     messagebox.showerror("Error", f"DUE TO: {str(es)}", parent=self.root)


