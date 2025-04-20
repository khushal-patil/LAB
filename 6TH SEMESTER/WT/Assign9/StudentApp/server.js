const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());
app.use(express.static(__dirname));

// Database connection
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Root@123',
    database: 'student_portal'
});

db.connect((err) => {
    if (err) throw err;
    console.log('Connected to database');
});

db.on('error', (err) => {
    console.error('Database error:', err);
    if (err.code === 'PROTOCOL_CONNECTION_LOST') {
        handleDisconnect();
    } else {
        throw err;
    }
});
// Register endpoint
// ...existing code...

app.post('/api/register', (req, res) => {
    const student = req.body;
    
    // Format the date to YYYY-MM-DD format
    const formattedDate = new Date(student.date_of_birth).toISOString().split('T')[0];
    
    const query = `
        INSERT INTO students (
            name, email, password, registration_number, 
            branch, semester, phone, date_of_birth, 
            address, gender, batch_year, blood_group, 
            parent_name, parent_phone
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `;
    
    const values = [
        student.name, 
        student.email, 
        student.password,
        student.registration_number, 
        student.branch,
        student.semester, 
        student.phone, 
        formattedDate,  // Use formatted date here
        student.address, 
        student.gender, 
        student.batch_year,
        student.blood_group, 
        student.parent_name, 
        student.parent_phone
    ];

    db.query(query, values, (err, result) => {
        if (err) {
            if (err.code === 'ER_DUP_ENTRY') {
                if (err.message.includes('email')) {
                    res.status(400).json({ error: 'Email already registered' });
                } else if (err.message.includes('registration_number')) {
                    res.status(400).json({ error: 'Registration number already exists' });
                } else {
                    res.status(400).json({ error: 'Duplicate entry found' });
                }
            } else {
                console.error('Registration error:', err);
                res.status(500).json({ error: 'Database error' });
            }
            return;
        }
        res.json({ message: 'Registration successful' });
    });
});

// Login endpoint
app.post('/api/login', (req, res) => {
    const { email, password } = req.body;
    const query = 'SELECT * FROM students WHERE email = ? AND password = ?';
    
    db.query(query, [email, password], (err, results) => {
        if (err) {
            res.status(500).json({ error: 'Database error' });
            return;
        }
        if (results.length > 0) {
            res.json({ success: true });
        } else {
            res.status(401).json({ error: 'Invalid credentials' });
        }
    });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});