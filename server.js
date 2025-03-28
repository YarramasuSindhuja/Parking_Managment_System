const express = require("express");
const cors = require("cors");
const ExcelJS = require("exceljs");
const fs = require("fs");

const app = express();
const PORT = 5000; // Keeping one consistent port

app.use(cors());
app.use(express.json());

// File to store booking data
const DATA_FILE = "bookings.json";

// Load existing bookings from file
let bookings = [];
if (fs.existsSync(DATA_FILE)) {
    bookings = JSON.parse(fs.readFileSync(DATA_FILE, "utf8"));
}

// 📌 **API: Get Vehicle Records from Excel**
app.get("/get-vehicles", async (req, res) => {
    try {
        const workbook = new ExcelJS.Workbook();
        await workbook.xlsx.readFile("data.xlsx"); // Read Excel file
        const worksheet = workbook.getWorksheet(1);
        let vehicles = [];

        worksheet.eachRow((row, rowNumber) => {
            if (rowNumber !== 1) { // Skip header row
                vehicles.push({
                    vehicleNumber: row.getCell(1).value,
                    date: row.getCell(2).value,
                    entryTime: row.getCell(3).value,
                    exitTime: row.getCell(4).value,
                });
            }
        });

        res.json(vehicles);
    } catch (error) {
        res.status(500).json({ message: "Error reading Excel file", error });
    }
});

// 📌 **API: Book a Parking Slot (User)**
app.post("/book-slot", (req, res) => {
    const { vehicleNumber, date, entryTime, exitTime } = req.body;

    const newBooking = {
        id: bookings.length + 1,
        vehicleNumber,
        date,
        entryTime,
        exitTime,
    };

    bookings.push(newBooking);

    // Save bookings to file
    fs.writeFileSync(DATA_FILE, JSON.stringify(bookings, null, 2));

    res.status(201).json({ message: "Slot booked successfully", booking: newBooking });
});

// 📌 **API: Get All Bookings (Admin)**
app.get("/get-bookings", (req, res) => {
    res.json(bookings);
});

// Start the server
app.listen(PORT, () => {
    console.log(`🚀 Server running on http://localhost:${PORT}`);
});
