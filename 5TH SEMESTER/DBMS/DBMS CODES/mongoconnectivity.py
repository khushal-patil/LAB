
#sudo python3 -m pip install pymongo

###Open mongo
#use test1 
#db.createCollection("emp")
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://127.0.0.1:27017")
database = client.test1
collection = database.emp

# Function to insert a new document
def create_document():
    name = input("Enter product name: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")
    collection.insert_one({"name": name, "quantity": quantity, "price": price})
    print("Document inserted successfully.")

# Function to read documents
def read_documents():
    print("All documents in the collection:")
    for doc in collection.find():
        print(doc)

# Function to update a document
def update_document():
    name = input("Enter the name of the product to update: ")
    new_quantity = input("Enter the new quantity: ")
    new_price = input("Enter the new price: ")
    result = collection.update_one(
        {"name": name}, 
        {"$set": {"quantity": new_quantity, "price": new_price}}
    )
    if result.matched_count > 0:
        print("Document updated successfully.")
    else:
        print("No document found with that name.")

# Function to delete a document
def delete_document():
    name = input("Enter the name of the product to delete: ")
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print("Document deleted successfully.")
    else:
        print("No document found with that name.")

# Main menu for CRUD operations
def main_menu():
    while True:
        print("\nChoose an operation:")
        print("1. Insert a document")
        print("2. Read all documents")
        print("3. Update a document")
        print("4. Delete a document")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_document()
        elif choice == '2':
            read_documents()
        elif choice == '3':
            update_document()
        elif choice == '4':
            delete_document()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()

# Close the connection
client.close()
