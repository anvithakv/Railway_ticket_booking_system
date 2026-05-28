from tkinter import *
from tkinter import ttk
from database import cursor
from booking import open_booking 
from my_bookings import open_my_bookings
from cancel_ticket import open_cancel_ticket


def open_dashboard(root, user_id):

    # ==========================================
    # DASHBOARD WINDOW
    # ==========================================

    dashboard = Toplevel(root)

    dashboard.title("RailEase Dashboard")

    dashboard.geometry("1400x800")

    dashboard.configure(bg="#e9e7f4")
    

    # ==========================================
    # SIDEBAR
    # ==========================================

    sidebar = Frame(
        dashboard,
        bg="#002244",
        width=250
    )

    sidebar.pack(side=LEFT, fill=Y)

    Label(
        sidebar,
        text="🚄 RailEase",
        font=("Arial", 22, "bold"),
        bg="#002244",
        fg="white"
    ).pack(pady=30)

    # ==========================================
    # CONTENT AREA
    # ==========================================

    content = Frame(
        dashboard,
        bg="#f4f7ff"
    )

    content.pack(side=LEFT, fill=BOTH, expand=True)
    

    Label(
        content,
        text="Available Trains",
        font=("Arial", 24, "bold"),
        bg="#f4f7ff"
    ).pack(pady=20)

    # ==========================================
    # TABLE
    # ==========================================

    columns = (
        "Train No",
        "Train Name",
        "From",
        "To",
        "Seats",
        "Fare"
    )

    table = ttk.Treeview(
        content,
        columns=columns,
        show="headings",
        height=12
    )

    for col in columns:

        table.heading(col, text=col)

        table.column(col, width=180)

    table.pack(pady=20)

    # ==========================================
    # LOAD TRAINS
    # ==========================================

    cursor.execute("SELECT * FROM trains")

    trains = cursor.fetchall()

    for train in trains:

        table.insert(
            '',
            END,
            values=(
                train[0],
                train[1],
                train[2],
                train[3],
                train[7],
                f"₹ {train[8]}"
            )
        )

    # ==========================================
    # SIDEBAR BUTTONS
    # ==========================================

    Button(
        sidebar,
        text="🎫 Book Ticket",
        bg="#005eff",
        fg="white",
        width=20,
        pady=10,
        font=("Arial", 12, "bold"),
        command=lambda: open_booking(root, user_id)
    ).pack(pady=10)

    Button(
        sidebar,
        text="📖 My Bookings",
        bg="#005eff",
        fg="white",
        width=20,
        pady=10,
        font=("Arial", 12, "bold"),
        command=lambda: open_my_bookings(root, user_id)
    ).pack(pady=10)

    Button(
        sidebar,
        text="❌ Cancel Ticket",
        bg="#ff3b30",
        fg="white",
        width=20,
        pady=10,
        font=("Arial", 12, "bold"),
        command=lambda: open_cancel_ticket(root)
    ).pack(pady=10)