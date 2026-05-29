# 🚆 RailEase – Smart Railway Reservation System

RailEase is a desktop-based Railway Reservation System developed using **Python**, **Tkinter**, and **MySQL**.
The application provides a simple and user-friendly graphical interface for railway ticket booking, passenger management, ticket cancellation, and reservation handling.

The project also includes:

* 📱 QR Code Generation
* 🖼️ Image Handling using Pillow
* ⚡ Executable (.exe) File Creation using PyInstaller

---

# 📌 Features

* 🔐 User Login System
* 🎫 Railway Ticket Booking
* 📋 View My Bookings
* ❌ Cancel Ticket Feature
* 🗄️ MySQL Database Integration
* 🎨 Attractive Tkinter GUI
* 🖼️ Image Integration using Pillow
* 📱 QR Code Generation using qrcode Library
* ⚡ Executable File Creation using PyInstaller
* 🚄 Smart Railway Reservation Management

---

# 🛠️ Technologies Used

* Python
* Tkinter
* MySQL
* Pillow (PIL) – For Image Handling
* qrcode – For QR Code Generation
* PyInstaller – For EXE File Creation

---

# 📂 Project Structure

```bash
Railease/
│
├── assets/
├── build/
├── dist/
├── booking.py
├── cancel_ticket.py
├── dashboard.py
├── database.py
├── database.sql
├── login.py
├── main.py
├── my_bookings.py
├── splash.py
├── splash.spec
└── README.md
```

---

# ▶️ How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/anvithakv/Railway_ticket_booking_system.git
```

---

## 2️⃣ Open Project Folder

```bash
cd Railway_ticket_booking_system/Railease
```

---

## 3️⃣ Install Required Libraries

```bash
pip install pillow qrcode
```

---

## 4️⃣ Configure MySQL Database

* Create a MySQL database
* Import the `database.sql` file
* Update database credentials in `database.py`

---

## 5️⃣ Run the Application

```bash
python splash.py
```

---

# ⚡ Create Executable File

```bash
pyinstaller splash.spec
```

The executable file will be generated inside the `dist` folder.

---

# 💡 Future Enhancements

* Live Train Status
* Online Payment Integration
* Seat Availability Tracking
* Admin Dashboard
* Email Ticket Confirmation

---



