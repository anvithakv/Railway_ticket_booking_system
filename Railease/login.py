from tkinter import *
from tkinter import messagebox
from database import cursor
from dashboard import open_dashboard


def open_login(root):

    login_window = Toplevel(root)
    login_window.title("RailEase Login")
    login_window.geometry("500x400")
    login_window.configure(bg="#0A2342")
    

    Label(
        login_window,
        text="User Login",
        font=("Arial", 24, "bold"),
        bg="white"
    ).pack(pady=30)

    Label(login_window, text="Email", bg="white").pack()
    email = Entry(login_window, width=35)
    email.pack(pady=10)

    Label(login_window, text="Password", bg="white").pack()
    password = Entry(login_window, show="*", width=35)
    password.pack(pady=10)

    def login_user():

        query = "SELECT * FROM users WHERE email=%s AND password=%s"

        cursor.execute(query, (
            email.get(),
            password.get()
        ))

        user = cursor.fetchone()
        

        if user:
            messagebox.showinfo("Success", "Login Successful")
            open_dashboard(root, user[0])
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    Button(
        login_window,
        text="Login",
        bg="#005eff",
        fg="white",
        font=("Arial", 14, "bold"),
        width=20,
        command=login_user
    ).pack(pady=30)


