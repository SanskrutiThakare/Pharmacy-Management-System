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

# Function to insert data into the medicines table
def insert_medicine():
    medicine_name = input("Enter medicine name: ")
    medicine_price = float(input("Enter medicine price: "))
    medicine_quantity = int(input("Enter medicine quantity: "))

    new_medicine = (medicine_name, medicine_price, medicine_quantity)
    insert_medicine_query = "INSERT INTO medicines (name, price, quantity) VALUES (%s, %s, %s)"
    cursor.execute(insert_medicine_query, new_medicine)
    connection.commit()
    print("Medicine data inserted.")

# Function to insert data into the sales table
def insert_sale():
    medicine_id = int(input("Enter medicine ID for the sale: "))
    quantity_sold = int(input("Enter quantity sold: "))
    sale_date = input("Enter sale date (YYYY-MM-DD): ")

    new_sale = (medicine_id, quantity_sold, sale_date)
    insert_sale_query = "INSERT INTO sales (medicine_id, quantity_sold, sale_date) VALUES (%s, %s, %s)"
    cursor.execute(insert_sale_query, new_sale)
    connection.commit()
    print("Sale data inserted.")

# Function to insert data into the suppliers table
def insert_supplier():
    supplier_name = input("Enter supplier name: ")
    contact_name = input("Enter contact name: ")
    contact_email = input("Enter contact email: ")

    new_supplier = (supplier_name, contact_name, contact_email)
    insert_supplier_query = "INSERT INTO suppliers (name, contact_name, contact_email) VALUES (%s, %s, %s)"
    cursor.execute(insert_supplier_query, new_supplier)
    connection.commit()
    print("Supplier data inserted.")

# Function to insert data into the prescriptions table
def insert_prescription():
    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    date_prescribed = input("Enter date prescribed (YYYY-MM-DD): ")

    new_prescription = (patient_name, doctor_name, date_prescribed)
    insert_prescription_query = "INSERT INTO prescriptions (patient_name, doctor_name, date_prescribed) VALUES (%s, %s, %s)"
    cursor.execute(insert_prescription_query, new_prescription)
    connection.commit()
    print("Prescription data inserted.")

# Function to insert data into the staff table
def insert_staff():
    staff_name = input("Enter staff name: ")
    position = input("Enter position: ")
    contact_email = input("Enter contact email: ")

    new_staff = (staff_name, position, contact_email)
    insert_staff_query = "INSERT INTO staff (name, position, contact_email) VALUES (%s, %s, %s)"
    cursor.execute(insert_staff_query, new_staff)
    connection.commit()
    print("Staff data inserted.")

# Dictionary to handle different cases
options = {
    '1': insert_medicine,
    '2': insert_sale,
    '3': insert_supplier,
    '4': insert_prescription,
    '5': insert_staff
}

while True:
    print("Choose a table to insert data:")
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
