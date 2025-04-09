import cx_Oracle

# Database configuration
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'dsn': 'localhost/orclpdb1',  # Replace with your Oracle DSN
}

# Connect to Oracle Database
def connect_to_database():
    try:
        conn = cx_Oracle.connect(**db_config)
        print("Connected to the database")
        return conn
    except cx_Oracle.DatabaseError as err:
        print(f"Error: {err}")
        return None

# Create a new record
def create_employee(name, salary):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO employees (name, salary) VALUES (:name, :salary)"
        data = {'name': name, 'salary': salary}
        try:
            cursor.execute(query, data)
            conn.commit()
            print("Employee added successfully")
        except cx_Oracle.DatabaseError as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

# Read records
def read_employees():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM employees"
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except cx_Oracle.DatabaseError as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

# Update a record
def update_employee(employee_id, name, salary):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE employees SET name = :name, salary = :salary WHERE id = :id"
        data = {'name': name, 'salary': salary, 'id': employee_id}
        try:
            cursor.execute(query, data)
            conn.commit()
            if cursor.rowcount:
                print("Employee updated successfully")
            else:
                print("Employee not found")
        except cx_Oracle.DatabaseError as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

# Delete a record
def delete_employee(employee_id):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        query = "DELETE FROM employees WHERE id = :id"
        data = {'id': employee_id}
        try:
            cursor.execute(query, data)
            conn.commit()
            if cursor.rowcount:
                print("Employee deleted successfully")
            else:
                print("Employee not found")
        except cx_Oracle.DatabaseError as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

# Main function to demonstrate CRUD operations
def main():
    # Create a new employee
    create_employee("Alice", 50000)
    
    # Read employees
    print("Employees List:")
    read_employees()
    
    # Update an employee
    update_employee(1, "Alice Johnson", 55000)
    
    # Delete an employee
    delete_employee(1)

if __name__ == "__main__":
    main()
