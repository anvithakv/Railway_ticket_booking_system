
from tkinter import *
from tkinter import messagebox
from database import cursor, conn
import random
import qrcode
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

def open_booking(root, user_id):

    booking = Toplevel(root)

    booking.title("Book Ticket")

    booking.geometry("700x600")

    booking.configure(bg="white")

    Label(
        booking,
        text="Book Ticket",
        font=("Arial", 24, "bold"),
        bg="white"
    ).pack(pady=20)

    labels = [
        "Train Number",
        "Passenger Name",
        "Age",
        "Gender",
        "Journey Date",
        "Number of Tickets"
    ]

    entries = []

    for text in labels:

        Label(
            booking,
            text=text,
            bg="white",
            font=("Arial", 12)
        ).pack()

        e = Entry(
            booking,
            width=40,
            font=("Arial", 12)
        )

        e.pack(pady=8)

        entries.append(e)

    # ==========================================
    # BOOK TICKET
    # ==========================================

    def book_ticket():

        try:

            train_no = entries[0].get()

            passenger = entries[1].get()

            age = entries[2].get()

            gender = entries[3].get()

            journey_date = entries[4].get()

            tickets = int(entries[5].get())

            query = """
            SELECT available_seats, fare
            FROM trains
            WHERE train_no=%s
            """

            cursor.execute(query, (train_no,))

            result = cursor.fetchone()

            if result:

                available_seats = result[0]

                fare = result[1]

                if available_seats >= tickets:

                    total_fare = fare * tickets

                    pnr = str(
                        random.randint(
                            1000000000,
                            9999999999
                        )
                    )

                    # ==========================================
                    # INSERT BOOKINGS
                    # ==========================================

                    for i in range(tickets):

                        seat = "S1-" + str(
                            random.randint(1, 72)
                        )

                        insert_query = """
                        INSERT INTO bookings(
                        user_id,
                        train_no,
                        passenger_name,
                        age,
                        gender,
                        seat_no,
                        journey_date,
                        pnr
                        )
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                        """

                        cursor.execute(
                            insert_query,
                            (
                                user_id,
                                train_no,
                                passenger,
                                age,
                                gender,
                                seat,
                                journey_date,
                                pnr
                            )
                        )

                    # ==========================================
                    # UPDATE SEATS
                    # ==========================================

                    update_query = """
                    UPDATE trains
                    SET available_seats =
                    available_seats - %s
                    WHERE train_no=%s
                    """

                    cursor.execute(
                        update_query,
                        (tickets, train_no)
                    )

                    conn.commit()

                    # ==========================================
                    # GENERATE QR
                    # ==========================================

                    qr_data = f"""
RAILEASE E-TICKET

PNR: {pnr}
Train No: {train_no}
Passenger: {passenger}
Journey Date: {journey_date}
Tickets: {tickets}
Total Fare: ₹{total_fare}
"""

                    qr = qrcode.make(qr_data)

                    assets_path = resource_path("assets")

                    if not os.path.exists(assets_path):
                        os.makedirs(assets_path)

                    qr.save(
                        os.path.join(
                            assets_path,
                            f"{pnr}.png"
                        )
                    )

                    messagebox.showinfo(
                        "Success",
                        f"Booking Successful\n\n"
                        f"PNR: {pnr}\n"
                        f"Total Fare: ₹{total_fare}"
                    )

                else:

                    messagebox.showerror(
                        "Error",
                        "Seats Not Available"
                    )

            else:

                messagebox.showerror(
                    "Error",
                    "Train Not Found"
                )

        except:

            messagebox.showerror(
                "Error",
                "Invalid Details"
            )

    # ==========================================
    # BUTTON
    # ==========================================

    Button(
        booking,
        text="Confirm Booking",
        bg="green",
        fg="white",
        font=("Arial", 14, "bold"),
        width=20,
        command=book_ticket
    ).pack(pady=30)
