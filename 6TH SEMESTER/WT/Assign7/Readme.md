Database Name
Registration

CREATE TABLE students (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(50),
    mname VARCHAR(50),
    lname VARCHAR(50),
    address TEXT,
    email VARCHAR(100),
    state VARCHAR(50),
    district VARCHAR(50),
    city VARCHAR(50),
    gender ENUM('Male', 'Female'),
    dob DATE,
    mobile VARCHAR(15),
    branch VARCHAR(50),
    qualification TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
