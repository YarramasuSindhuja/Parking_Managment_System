import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="c7g85hmx",  # 👈 Replace with your MySQL password
        database="parking_db"
    )
    print("✅ Connected to MySQL successfully!")
except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
