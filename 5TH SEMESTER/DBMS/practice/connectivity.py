import mysql.connector

# Database configuration
db_config = {
    'user': 'root',
    'password': 'root@123',
    'host': 'localhost',
    'database': 'khushal',
    'auth_plugin': 'mysql_native_password'
}

# Connect to MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Connected to the database")
            return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create a new record
def create_employee(rollno,name):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO student (rollno, name) VALUES (%s, %s)"
        data = (rollno, name)
        try:
            cursor.execute(query, data)
            conn.commit()
            print("Employee added successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

# Read records
def read_employees():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM student"
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

# Update a record
def update_employee(employee_id, name):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE student SET name = %s WHERE rollno = %s"
        data = (name,employee_id )
        try:
            cursor.execute(query, data)
            conn.commit()
            if cursor.rowcount:
                print("Employee updated successfully")
            else:
                print("Employee not found")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

# Delete a record
def delete_employee(employee_id):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "DELETE FROM student WHERE rollno = %s"
        data = (employee_id,)
        try:
            cursor.execute(query, data)
            conn.commit()
            if cursor.rowcount:
                print("Employee deleted successfully")
            else:
                print("Employee not found")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

# Main function to demonstrate CRUD operations
def main():
    # Create a new employee
    create_employee(1, "Alice")
  
    print("Employees List:")
    read_employees()
    
    # Update an employee
    update_employee(1,"KHUSHAL")
    read_employees()
    # Delete an employee
    delete_employee(1)

if __name__ == "__main__":
    main()
