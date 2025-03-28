from flask import Flask, request, jsonify
from flask_cors import CORS # type: ignore
import mysql.connector

app = Flask(__name__)
CORS(app)

# MySQL connection
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="c7g85hmx",  # ⬅️ Replace this!
        database="parking_db"
    )
    print("✅ Connected to MySQL successfully!")
except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
cursor = conn.cursor(dictionary=True)

# Route to get all vehicle booking records (for admin dashboard)
@app.route("/get-vehicles", methods=["GET"])
def get_vehicles():
    cursor.execute("SELECT * FROM vehicles")
    data = cursor.fetchall()
    result = []
    for row in data:
        result.append({
            "ID": row["id"],
            "Vehicle Number": row["vehicle_number"],
            "Date": str(row["date"]),
            "Entry Time": str(row["entry_time"]),
            "Exit Time": str(row["exit_time"]) if row["exit_time"] else "N/A",
            "Slot Number": row["slot_number"]
        })
    return jsonify(result)

# ✅ New route to get real-time slot status
@app.route("/slots-status", methods=["GET"])
def slots_status():
    cursor.execute("SELECT slot_number FROM vehicles WHERE exit_time IS NULL")
    occupied_slots = cursor.fetchall()

    occupied_set = {slot["slot_number"] for slot in occupied_slots}
    all_slots = [f"Slot {i}" for i in range(1, 11)]  # Example: 10 total slots

    slots_data = []
    for slot in all_slots:
        slots_data.append({
            "slot": slot,
            "occupied": slot in occupied_set
        })

    return jsonify(slots_data)

# ✅ Route to book a slot (inserts into database)
@app.route("/book-slot", methods=["POST"])
def book_slot():
    data = request.json
    vehicle_number = data["vehicle_number"]
    date = data["date"]
    entry_time = data["entry_time"]

    # Find first available slot
    cursor.execute("SELECT slot_number FROM vehicles WHERE exit_time IS NULL")
    occupied = {row["slot_number"] for row in cursor.fetchall()}
    all_slots = [f"Slot {i}" for i in range(1, 11)]

    available_slots = [slot for slot in all_slots if slot not in occupied]

    if not available_slots:
        return jsonify({"status": "fail", "message": "No available slots"}), 400

    assigned_slot = available_slots[0]

    # Insert into DB
    insert_query = """
        INSERT INTO vehicles (vehicle_number, date, entry_time, slot_number)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (vehicle_number, date, entry_time, assigned_slot))
    conn.commit()

    return jsonify({"status": "success", "slot_assigned": assigned_slot})

# ✅ Route to update exit time (from exit.html)
@app.route("/exit", methods=["POST"])
def update_exit_time():
    data = request.json
    vehicle_number = data["vehicle_number"]
    exit_time = data["exit_time"]

    update_query = """
        UPDATE vehicles
        SET exit_time = %s
        WHERE vehicle_number = %s AND exit_time IS NULL
    """
    cursor.execute(update_query, (exit_time, vehicle_number))
    conn.commit()

    return jsonify({"status": "success", "message": "Exit time updated"})

# Home route
@app.route("/")
def home():
    return "Parking Management Backend Running"

if __name__ == "__main__":
    app.run(debug=True)
