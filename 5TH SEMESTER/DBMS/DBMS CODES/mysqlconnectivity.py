import mysql.connector

# Establish a database connection
def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",      # Replace with your host
            user="root",           # Replace with your username
            password="root@123",   # Replace with your password
            database="khushal"      # Replace with your database name
        )
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
        return None



# Function to insert data into the table
def insert_data():
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            insert_query = "INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (name, quantity, price))
            connection.commit()
            print("Data inserted successfully.")
        else:
            print("Failed to insert data due to connection issues.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to update a record in the table
def update_data():
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            product_id = input("Enter the name of the product to update: ")
            new_quantity = int(input("Enter the new quantity: "))
            new_price = float(input("Enter the new price: "))
            update_query = "UPDATE products SET quantity = %s, price = %s WHERE name = %s"
            cursor.execute(update_query, (new_quantity, new_price, product_id))
            connection.commit()
            if cursor.rowcount > 0:
                print("Data updated successfully.")
            else:
                print("No product found with that ID.")
        else:
            print("Failed to update data due to connection issues.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to delete a record from the table
def delete_data():
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            product_id = input("Enter the name of the product to delete: ")
            delete_query = "DELETE FROM products WHERE name = %s"
            cursor.execute(delete_query, (product_id,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Data deleted successfully.")
            else:
                print("No product found with that ID.")
        else:
            print("Failed to delete data due to connection issues.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def display_data():
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            select_query = "SELECT * FROM products"
            cursor.execute(select_query)
            records = cursor.fetchall()
            if records:
                print("\nProduct Records:")
                print(" Name       | Quantity | Price")
                print("--------------------------------------")
                for row in records:
                    print(f"{row[0]:<3} | {row[1]:<10} | {row[2]:<8}")
            else:
                print("No records found.")
        else:
            print("Failed to retrieve data due to connection issues.")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Menu to interact with the CRUD functions
def main_menu():
    while True:
        print("\nChoose an operation:")
       
        print("1. Insert data")
        print("2. Update data")
        print("3. Delete data")
        print("4. Display all data")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            insert_data()
        elif choice == '2':
            update_data()
        elif choice == '3':
            delete_data()
        elif choice == '4':
            display_data()
        elif choice == '5':
            print("Exiting...")
            break          
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
