import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anvi@243",
    database="Railway_system"
)

cursor = conn.cursor()