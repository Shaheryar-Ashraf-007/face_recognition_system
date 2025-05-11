from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import time
from collections import Counter

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="Train Data Set", font=("Times New Roman", 28, "bold"), bg="teal", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=50)
        
        img_top = Image.open(r"D:\face recognition attendence system\student management system\images\top1.jpg")
        img_top = img_top.resize((1530, 325), Image.BICUBIC)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1530, height=325)
        
        # Button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
                      font=("Times New Roman", 30, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=325, width=1530, height=50)
        
        img_bottom = Image.open(r"D:\face recognition attendence system\student management system\images\top4.jpg")
        img_bottom = img_bottom.resize((1530, 350), Image.BICUBIC)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=375, width=1530, height=350)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient=HORIZONTAL, length=1530, mode='determinate')
        self.progress.place(x=0, y=740, width=1530, height=20)
        
        # Status label
        self.status_var = StringVar()
        self.status_var.set("Ready to train...")
        self.status_label = Label(self.root, textvariable=self.status_var, font=("Times New Roman", 14), bg="white", fg="blue")
        self.status_label.place(x=0, y=760, width=1530, height=40)
    
    def update_status(self, message):
        self.status_var.set(message)
        self.root.update_idletasks()
    
    def train_classifier(self):
        data_dir = "D:\\face recognition attendence system\\student management system\\data"
        
        # Check if directory exists
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found!")
            return
        
        # Get all image paths
        image_paths = []
        for root_dir, _, files in os.walk(data_dir):
            for file in files:
                if file.endswith('.jpg') or file.endswith('.png'):
                    image_paths.append(os.path.join(root_dir, file))
        
        if not image_paths:
            messagebox.showerror("Error", "No images found in the data directory!")
            return
        
        # Reset progress bar
        self.progress['value'] = 0
        self.progress['maximum'] = len(image_paths)
        
        faces = []
        ids = []
        failed_images = []
        
        # Process each image
        for count, image_path in enumerate(image_paths):
            try:
                # Update progress and status
                self.progress['value'] = count + 1
                self.update_status(f"Processing image {count+1}/{len(image_paths)}: {os.path.basename(image_path)}")
                
                # Open and process image
                img = Image.open(image_path).convert('L')  # Convert to grayscale
                image_np = np.array(img, 'uint8')
                
                # Extract ID from filename (assuming format like name.1.jpg where 1 is the ID)
                id_part = os.path.split(image_path)[1].split('.')
                if len(id_part) < 2:
                    failed_images.append((image_path, "Invalid filename format"))
                    continue
                
                try:
                    id = int(id_part[1])
                except ValueError:
                    failed_images.append((image_path, "ID is not a valid integer"))
                    continue
                
                # Add to training data
                faces.append(image_np)
                ids.append(id)
                
                # Show image being processed
                cv2.imshow("Training", cv2.resize(image_np, (200, 200)))
                cv2.waitKey(1)
                
                # Small delay to allow GUI to update
                time.sleep(0.01)
                
            except Exception as e:
                failed_images.append((image_path, str(e)))
        
        # Check if we have enough data
        if len(faces) == 0:
            cv2.destroyAllWindows()
            messagebox.showerror("Error", "No valid faces found for training!")
            return
        
        # Count images per ID
        id_counts = Counter(ids)
        
        # Check if any ID has too few images
        low_count_ids = [id for id, count in id_counts.items() if count < 5]
        
        # Train the classifier
        self.update_status("Training the classifier...")
        ids = np.array(ids)
        
        clf = cv2.face.LBPHFaceRecognizer_create(
            radius=3,
            neighbors=8,
            grid_x=8,
            grid_y=8,
            threshold=100
        )
        
        clf.train(faces, ids)
        clf.write("classifier.xml")
        
        cv2.destroyAllWindows()
        
        # Report results
        result_message = f"Training completed successfully!\n\n"
        result_message += f"Total images processed: {len(image_paths)}\n"
        result_message += f"Successfully trained with: {len(faces)} images\n"
        result_message += f"Failed images: {len(failed_images)}\n"
        result_message += f"Number of unique IDs: {len(id_counts)}\n\n"
        
        if low_count_ids:
            result_message += f"WARNING: The following IDs have fewer than 5 images, which may lead to poor recognition:\n"
            result_message += ", ".join(map(str, low_count_ids)) + "\n\n"
            
        if failed_images:
            result_message += "First 5 failed images:\n"
            for i, (path, error) in enumerate(failed_images[:5]):
                result_message += f"- {os.path.basename(path)}: {error}\n"
        
        messagebox.showinfo("Training Results", result_message)
        
        # Create a log file
        with open("training_log.txt", "w") as log_file:
            log_file.write(f"Training Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            log_file.write(result_message + "\n\n")
            
            log_file.write("=== DETAILS ===\n\n")
            log_file.write("Images per ID:\n")
            for id, count in sorted(id_counts.items()):
                log_file.write(f"ID {id}: {count} images\n")
            
            if failed_images:
                log_file.write("\nFailed Images:\n")
                for path, error in failed_images:
                    log_file.write(f"{os.path.basename(path)}: {error}\n")
        
        self.update_status("Training completed. Log saved to training_log.txt")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()