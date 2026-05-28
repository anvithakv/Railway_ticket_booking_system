
from tkinter import *

# ==========================================
# SPLASH WINDOW
# ==========================================

splash = Tk()

splash.title("RailEase")

splash.geometry("900x500")

splash.configure(bg="#002244")

splash.overrideredirect(True)

# ==========================================
# CENTER WINDOW
# ==========================================

screen_width = splash.winfo_screenwidth()

screen_height = splash.winfo_screenheight()

x = (screen_width // 2) - (900 // 2)

y = (screen_height // 2) - (500 // 2)

splash.geometry(f"900x500+{x}+{y}")

# ==========================================
# TITLE
# ==========================================

Label(
    splash,
    text="🚄 RailEase",
    font=("Arial", 42, "bold"),
    bg="#002244",
    fg="white"
).pack(pady=80)

# ==========================================
# SUBTITLE
# ==========================================

Label(
    splash,
    text="Smart Railway Reservation System",
    font=("Arial", 20),
    bg="#002244",
    fg="white"
).pack()

# ==========================================
# LOADING TEXT
# ==========================================

loading = Label(
    splash,
    text="Loading...",
    font=("Arial", 16, "bold"),
    bg="#002244",
    fg="#38BDF8"
)

loading.pack(pady=50)

# ==========================================
# OPEN MAIN WINDOW
# ==========================================

def open_main():

    splash.destroy()

    import main

# ==========================================
# TIMER
# ==========================================

splash.after(2000, open_main)

splash.mainloop()
