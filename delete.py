import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL server's host
    user="root",  # Replace with your MySQL username
    password="mysql@2023",  # Replace with your MySQL password
    database="pharmacy_db"  # Specify the database you want to connect to
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Function to delete data from the medicines table
def delete_medicine():
     medicine_id = int(input("Enter the ID of the medicine to delete: "))
     cursor.execute("SELECT * FROM medicines WHERE id = %s", (medicine_id,))
     existing_medicine = cursor.fetchone()
    
     if existing_medicine:
         delete_medicine_query = "DELETE FROM medicines WHERE id = %s"
         cursor.execute(delete_medicine_query, (medicine_id,))
         connection.commit()
         print("Medicine data deleted.")
     else:
         print("Medicine with ID", medicine_id, "does not exist.")

# Function to delete data from the sales table
def delete_sale():
    sale_id = int(input("Enter the ID of the sale to delete: "))

    cursor.execute("SELECT * FROM sales WHERE id = %s", (sale_id,))
    existing_sale = cursor.fetchone()

    if existing_sale:
        delete_sale_query = "DELETE FROM sales WHERE id = %s"
        cursor.execute(delete_sale_query, (sale_id,))
        connection.commit()
        print("Sale data deleted.")
    else:
        print("Sale with ID", sale_id, "does not exist.")

# Function to delete data from the suppliers table
def delete_supplier():
    supplier_id = int(input("Enter the ID of the supplier to delete: "))

    cursor.execute("SELECT * FROM suppliers WHERE id = %s", (supplier_id,))
    existing_supplier = cursor.fetchone()

    if existing_supplier:
        delete_supplier_query = "DELETE FROM suppliers WHERE id = %s"
        cursor.execute(delete_supplier_query, (supplier_id,))
        connection.commit()
        print("Supplier data deleted.")
    else:
        print("Supplier with ID", supplier_id, "does not exist.")

# Function to delete data from the prescriptions table
def delete_prescription():
    prescription_id = int(input("Enter the ID of the prescription to delete: "))

    cursor.execute("SELECT * FROM prescriptions WHERE id = %s", (prescription_id,))
    existing_prescription = cursor.fetchone()

    if existing_prescription:
        delete_prescription_query = "DELETE FROM prescriptions WHERE id = %s"
        cursor.execute(delete_prescription_query, (prescription_id,))
        connection.commit()
        print("Prescription data deleted.")
    else:
        print("Prescription with ID", prescription_id, "does not exist.")
        

# Function to delete data from the staff table
def delete_staff():
    staff_id = int(input("Enter the ID of the staff member to delete: "))

    cursor.execute("SELECT * FROM staff WHERE id = %s", (staff_id,))
    existing_staff = cursor.fetchone()

    if existing_staff:
        delete_staff_query = "DELETE FROM staff WHERE id = %s"
        cursor.execute(delete_staff_query, (staff_id,))
        connection.commit()
        print("Staff data deleted.")
    else:
        print("staff with ID", staff_id, "does not exist.")
        

# Dictionary to handle different cases
options = {
    '1': delete_medicine,
    '2': delete_sale,
    '3': delete_supplier,
    '4': delete_prescription,
    '5': delete_staff
}

while True:
    print("Choose a table to delete data from:")
    print("1. Medicines")
    print("2. Sales")
    print("3. Suppliers")
    print("4. Prescriptions")
    print("5. Staff")
    print("6. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '6':
        break

    selected_option = options.get(choice)
    if selected_option:
        selected_option()
    else:
        print("Invalid choice. Please select a valid option.")

# Close the cursor and connection when done
cursor.close()
connection.close()
