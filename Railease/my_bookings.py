from tkinter import *
from tkinter import ttk
from database import cursor
from PIL import Image, ImageTk
import os
import sys

# ==========================================
# RESOURCE PATH
# ==========================================

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# ==========================================

def open_my_bookings(root, user_id):

    bookings_window = Toplevel(root)

    bookings_window.title("My Bookings")

    bookings_window.geometry("1500x600")

    bookings_window.configure(bg="white")

    # ==========================================
    # COLUMNS
    # ==========================================

    columns = (
        "PNR",
        "Train No",
        "Train Name",
        "From",
        "To",
        "Passenger",
        "Seat",
        "Date",
        "Fare"
    )

    # ==========================================
    # TABLE
    # ==========================================

    booking_table = ttk.Treeview(
        bookings_window,
        columns=columns,
        show="headings",
        height=20
    )

    for col in columns:

        booking_table.heading(col, text=col)

        booking_table.column(
            col,
            width=160,
            anchor=CENTER
        )

    booking_table.pack(
        fill=BOTH,
        expand=True,
        pady=20
    )

    # ==========================================
    # QUERY
    # ==========================================

    query = """
    SELECT
    b.pnr,
    b.train_no,
    t.train_name,
    t.source,
    t.destination,
    b.passenger_name,
    b.seat_no,
    b.journey_date,
    t.fare
    FROM bookings b
    JOIN trains t
    ON b.train_no = t.train_no
    WHERE b.user_id=%s
    """

    cursor.execute(query, (user_id,))

    bookings = cursor.fetchall()

    # ==========================================
    # INSERT DATA
    # ==========================================

    for booking in bookings:

        booking_table.insert(
            '',
            END,
            values=booking
        )

    # ==========================================
    # SHOW TICKET
    # ==========================================

    def show_ticket(event):

        selected = booking_table.focus()

        values = booking_table.item(
            selected,
            'values'
        )

        if not values:
            return

        pnr = values[0]

        # ==========================================
        # TICKET WINDOW
        # ==========================================

        ticket_window = Toplevel()

        ticket_window.title("E-Ticket")

        ticket_window.geometry("550x750")

        ticket_window.configure(bg="white")

        # ==========================================
        # HEADING
        # ==========================================

        Label(
            ticket_window,
            text="🚄 RAILEASE E-TICKET",
            font=("Arial", 22, "bold"),
            bg="white",
            fg="#002244"
        ).pack(pady=20)

        # ==========================================
        # DETAILS
        # ==========================================

        details = [
            f"PNR : {values[0]}",
            f"Train No : {values[1]}",
            f"Train Name : {values[2]}",
            f"From : {values[3]}",
            f"To : {values[4]}",
            f"Passenger : {values[5]}",
            f"Seat : {values[6]}",
            f"Journey Date : {values[7]}"
        ]

        for detail in details:

            Label(
                ticket_window,
                text=detail,
                font=("Arial", 14),
                bg="white"
            ).pack(pady=5)

        Label(
            ticket_window,
            text=f"Fare : ₹ {values[8]}",
            font=("Arial", 16, "bold"),
            fg="green",
            bg="white"
        ).pack(pady=10)

        # ==========================================
        # QR IMAGE
        # ==========================================

        try:

            qr_image = Image.open(
                resource_path(
                    f"assets/{pnr}.png"
                )
            )

            qr_image = qr_image.resize((220, 220))

            qr_photo = ImageTk.PhotoImage(qr_image)

            qr_label = Label(
                ticket_window,
                image=qr_photo,
                bg="white"
            )

            qr_label.image = qr_photo

            qr_label.pack(pady=20)

        except:

            Label(
                ticket_window,
                text="QR Code Not Found",
                font=("Arial", 14, "bold"),
                fg="red",
                bg="white"
            ).pack(pady=20)

    # ==========================================
    # DOUBLE CLICK EVENT
    # ==========================================

    booking_table.bind(
        "<Double-1>",
        show_ticket
    )
