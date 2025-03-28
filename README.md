# 🚗 **Parking Lot Management System**

## 📌 **Introduction**
The Parking Lot Management System is a web-based application designed to streamline parking slot management. It allows users to book and exit parking slots efficiently, while administrators can monitor slot availability and vehicle records in real-time.

---

## 🛠️ **Technologies Used**
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python), Express (Node.js)
- **Database:** MySQL
- **Environment:** Virtual Environment using Python

---

## ✨ **Features**
- **User Slot Booking:** Reserve a parking slot through the web interface.
- **Slot Availability Monitoring:** View available and occupied slots.
- **Admin Dashboard:** Access and manage parking records.
- **Vehicle Entry and Exit Management:** Record vehicle details on entry and exit.
- **Secure Login:** User authentication for dashboard access.

---

## 🚀 **Installation and Setup**
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/parking-lot-management.git
   cd parking-lot-management
   ```
2. **Set Up Virtual Environment:**
   ```bash
   python -m venv .venv
   ```
3. **Activate Virtual Environment:**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source .venv/bin/activate
     ```
4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Configure MySQL Database:**
   Edit the `app.py` file to include your MySQL credentials:
   ```python
   conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="your_password",
       database="parking_db"
   )
   ```
6. **Run the Application:**
   ```bash
   python app.py
   ```
7. **Access the Web Application:**
   Open the browser and visit:
   ```
   http://localhost:5000
   ```

---

## 📝 **Usage**
1. **Login:** Access the dashboard with your credentials.
2. **Book a Slot:** Reserve an available slot.
3. **View Slots:** Check the status of all parking slots.
4. **Exit Parking:** Mark a slot as vacant upon exit.
5. **Admin Access:** View and manage all parked vehicle details.

---

## 📂 **Project Structure**
```
parking-lot-management/
├── .venv/                 # Virtual environment files
├── js/                    # JavaScript scripts
├── pages/                 # HTML pages
├── app.py                 # Flask backend
├── server.js              # Express server (for API handling)
├── style.css              # CSS styles
├── parking_data.xlsx      # Data storage file
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 📝 **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 **Contributing**
Contributions are welcome! Feel free to fork the repository and submit pull requests. For major changes, please open an issue to discuss your ideas.

---

## 💬 **Contact**
For any questions or feedback, please reach out to [your email].

