from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import numpy as np
from collections import Counter

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognition System")



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()