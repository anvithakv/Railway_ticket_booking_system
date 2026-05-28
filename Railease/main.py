from tkinter import *
from PIL import Image, ImageTk
from login import open_login
import os
import sys

# =========================================
# RESOURCE PATH
# =========================================

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# =========================================

root = Tk()

root.title("RailEase - Smart Railway Reservation System")

root.geometry("1600x800")

# =========================================
# BACKGROUND IMAGE
# =========================================

bg_image = Image.open(resource_path("assets/train.png"))

bg_image = bg_image.resize((1600, 800))

bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg_photo)

bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# =========================================
# BUTTON
# =========================================

Button(
    root,
    text="Explore RailEase",
    font=("Arial", 18, "bold"),
    bg="#2563EB",
    fg="white",
    padx=20,
    pady=10,
    activebackground="#2563EB",
    activeforeground="white",
    cursor="hand2",
    relief=FLAT,
    bd=0,
    command=lambda: open_login(root),
).place(x=650, y=620)

# =========================================

root.mainloop() 