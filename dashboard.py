import tkinter as tk
import cv2
import os
from PIL import Image, ImageTk
#import cameradete
from  tkinter import PhotoImage
from datetime import datetime
#import human19try



# Define the main window
root = tk.Tk()
root.title("DEFENCE SYSTEM")
root.iconphoto(False,PhotoImage(file="images\\logo.png"))

# Set the size of the window
root.geometry("10000x12000")



# menu frame
user_frame = tk.Frame(root, bg='#1F1F1F', width=20, height=20)
user_frame.pack(side='left', fill='y')

user_image = Image.open("images\\logo.png")
user_image = user_image.resize((150, 150), Image.ANTIALIAS) 
user_photo = ImageTk.PhotoImage(user_image)

user_photo_label = tk.Label(user_frame, image=user_photo,bg='#1F1F1F')
user_photo_label.pack(side='top', padx=25, pady=25)

# open detected image folder
def open_folder():
    folder_path = "Detected Images\\"
    os.startfile(folder_path)

def detect_human():
    #root.destroy()
    import human19try

    
    
                
# menus button with icons
photo1 = Image.open("images\\home.png")
photo1 = photo1.resize((25, 25), Image.ANTIALIAS) 
photo1 = ImageTk.PhotoImage(photo1)
home_button = tk.Button(user_frame, text="Home", font=("Arial", 12,'bold'), bg='#363636',fg='white', padx=10, pady=10,image=photo1,compound='left')
home_button.pack(pady=13)

photo4 = Image.open("images\\captured.png")
photo4 = photo4.resize((25, 25), Image.ANTIALIAS) 
photo4 = ImageTk.PhotoImage(photo4)
detect = tk.Button(user_frame, text="Detection", font=("Arial", 12,'bold'),bg='#363636', fg='white', padx=10, pady=10,image=photo4,compound='left',command=detect_human)
detect.pack(pady=13)

photo3 = Image.open("images\\update.png")
photo3 = photo3.resize((25, 25), Image.ANTIALIAS) 
photo3 = ImageTk.PhotoImage(photo3)
contact_button = tk.Button(user_frame, text="Images",command=open_folder, font=("Arial", 12,'bold'),bg='#363636',fg='white', padx=10, pady=10,image=photo3,compound='left')
contact_button.pack(pady=13)

photo5 = Image.open("images\\logout.png")
photo5 = photo5.resize((25, 25), Image.ANTIALIAS) 
photo5 = ImageTk.PhotoImage(photo5)
detect = tk.Button(user_frame, text="Logout", font=("Arial", 12,'bold'),command=exit, bg='#363636', fg='white', padx=10, pady=10,image=photo5,compound='left')
detect.pack(pady=13)

# stream section
camera_frame = tk.Frame(root, bg='#363636', width=500, height=500)
camera_frame.pack(side='right', fill='both', expand=True)

photo = Image.open('images\\main.png')
photo = photo.resize((50, 50), Image.ANTIALIAS) 
photo = ImageTk.PhotoImage(photo)
camera_label = tk.Label(camera_frame, text="Live Monitoring", font=("Arial", 20,'bold'), fg='white',bg='black',bd=10,image=photo,padx=10,compound='left')
camera_label.pack(side='top', pady=20,padx=20)

camera_panel = tk.Label(camera_frame,height=1000,width=1000,bg='black')
camera_panel.pack(side='top', padx=10, pady=10)

# Define the camera function
def show_frame():
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    camera_panel.imgtk = imgtk
    camera_panel.configure(image=imgtk)
    camera_panel.after(10, show_frame)
    
    #import human19try
    


# Start the camera stream
cap = cv2.VideoCapture(0)
show_frame()

# Start the application
root.mainloop()