To compile Java Program
javac -cp ".;../lib/mysql-connector-java-8.0.33.jar" src/db/DBConnection.java

creating DB
create database student_info;
use student_info;


CREATE TABLE students_info (
    stud_id INT PRIMARY KEY,
    stud_name VARCHAR(50),
    class VARCHAR(10),
    division VARCHAR(10),
    city VARCHAR(50)
);

INSERT INTO students_info (stud_id, stud_name, class, division, city) VALUES
(1, 'Rohan Sharma', 'FE', 'Comp1', 'Mumbai'),
(2, 'Ankit Verma', 'SE', 'Comp2', 'Pune'),
(3, 'Amitabh Joshi', 'TE', 'Comp1', 'Delhi'),
(4, 'Vikram Singh', 'BE', 'Comp3', 'Chennai'),
(5, 'Sahil Khan', 'FE', 'Comp2', 'Ahmedabad'),
(6, 'Rahul Nair', 'SE', 'Comp3', 'Kochi'),
(7, 'Manish Deshmukh', 'TE', 'Comp1', 'Nagpur'),
(8, 'Nikhil Pandey', 'BE', 'Comp2', 'Lucknow'),
(9, 'Arjun Reddy', 'FE', 'Comp3', 'Hyderabad'),
(10, 'Karan Kapoor', 'SE', 'Comp1', 'Bangalore');

