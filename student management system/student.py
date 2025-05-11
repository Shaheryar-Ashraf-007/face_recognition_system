from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student_detail import Student
import os
from train import Train
from tkinter import messagebox
from face_recognition import FaceRecognition
from attendance import Attendance
from developer import Developer
from help import Help

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognition System")
        
        # Constants for image sizes
        self.HEADER_IMAGE_SIZE = (500, 130)
        self.BG_IMAGE_SIZE = (1530, 800)
        self.BUTTON_IMAGE_SIZE = (180, 180)

        # Load images
        self.load_images()

        # Create UI components
        self.create_ui()

    def load_images(self):
        try:
            self.header_images = [
                ImageTk.PhotoImage(Image.open(r"D:\face recognition attendence system\student management system\images\recog5.jpg").resize(self.HEADER_IMAGE_SIZE, Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open(r"D:\face recognition attendence system\student management system\images\face.jpg").resize(self.HEADER_IMAGE_SIZE, Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open(r"D:\face recognition attendence system\student management system\images\recog11.jpg").resize(self.HEADER_IMAGE_SIZE, Image.BICUBIC))
            ]
            self.bg_image = ImageTk.PhotoImage(Image.open(r"D:\face recognition attendence system\student management system\images\recog13.jpg").resize(self.BG_IMAGE_SIZE, Image.BICUBIC))
            self.button_images = [
                ImageTk.PhotoImage(Image.open(r"D:\face recognition attendence system\student management system\images\recog14.jpg").resize(self.BUTTON_IMAGE_SIZE, Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open(r"D:\face recognition attendence system\student management system\images\pic3.jpg").resize(self.BUTTON_IMAGE_SIZE, Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open(r"D:\face recognition attendence system\student management system\images\pic4.jpg").resize(self.BUTTON_IMAGE_SIZE, Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open(r"D:\face recognition attendence system\student management system\images\pic7.jpg").resize(self.BUTTON_IMAGE_SIZE, Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open(r"D:\face recognition attendence system\student management system\images\pic8.jpg").resize(self.BUTTON_IMAGE_SIZE, Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open(r"D:\face recognition attendence system\student management system\images\pic1.jpg").resize(self.BUTTON_IMAGE_SIZE, Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open(r"D:\face recognition attendence system\student management system\images\pic6.jpg").resize(self.BUTTON_IMAGE_SIZE, Image.BICUBIC)),
                ImageTk.PhotoImage(Image.open(r"D:\face recognition attendence system\student management system\images\pic5.jpg").resize((200, 145), Image.BICUBIC))
            ]
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load images: {e}")

    def create_ui(self):
        # Header images
        for idx, img in enumerate(self.header_images):
            Label(self.root, image=img).place(x=idx * 500, y=0, width=500, height=130)
        
        # Background image
        Label(self.root, image=self.bg_image).place(x=0, y=130, width=1530, height=800)
        
        # Title label
        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SOFTWARE SYSTEM", font=("Times New Roman", 28, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # Buttons
        self.create_buttons()

    def create_buttons(self):
        button_details = [
            ("Student Details", self.student_details, 100, 90),
            ("Face Detector", self.face_data, 400, 90),
            ("Attendance", self.Attendance_data, 740, 90),
            ("Help", self.Help_desk, 1070, 90),
            ("Train Data", self.train_data, 100, 350),
            ("Photos", self.open_img, 400, 350),
            ("Developer", self.Developer_data, 740, 350),
            ("Exit", None, 1070, 350)
        ]
        
        for idx, (text, command, x, y) in enumerate(button_details):
            img = self.button_images[idx] if idx < len(self.button_images) else None
            Button(self.root, image=img, command=command, cursor="hand2").place(x=x, y=y, width=180, height=180)
            Button(self.root, text=text, command=command, cursor="hand2", font=("Times New Roman", 15, "bold"), bg="darkblue", fg="white").place(x=x, y=y + 150, width=180, height=40)

    def open_img(self):
        os.startfile(r"D:\face recognition attendence system\student management system\data")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)

    def Attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def Developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def Help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()