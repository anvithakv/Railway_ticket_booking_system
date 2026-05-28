from tkinter import *
from tkinter import messagebox
from database import cursor, conn


def open_cancel_ticket(root):

    cancel = Toplevel(root)
    cancel.title("Cancel Ticket")
    cancel.geometry("500x400")
    cancel.configure(bg="white")

    Label(
        cancel,
        text="Cancel Ticket",
        font=("Arial", 24, "bold"),
        bg="white"
    ).pack(pady=30)

    Label(cancel, text="Enter PNR Number", bg="white").pack()

    pnr_entry = Entry(cancel, width=40)
    pnr_entry.pack(pady=20)

    def cancel_booking():

        pnr = pnr_entry.get()

        query = "SELECT train_no FROM bookings WHERE pnr=%s"
        cursor.execute(query, (pnr,))

        result = cursor.fetchone()

        if result:

            train_no = result[0]

            delete_query = "DELETE FROM bookings WHERE pnr=%s"
            cursor.execute(delete_query, (pnr,))

            update_query = """
            UPDATE trains
            SET available_seats = available_seats + 1
            WHERE train_no=%s
            """

            cursor.execute(update_query, (train_no,))

            conn.commit()

            messagebox.showinfo("Success", "Ticket Cancelled")

        else:
            messagebox.showerror("Error", "Invalid PNR")

    Button(
        cancel,
        text="Cancel Ticket",
        bg="red",
        fg="white",
        width=20,
        font=("Arial", 14, "bold"),
        command=cancel_booking
    ).pack(pady=20)
