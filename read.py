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

# Function to read data from the medicines table
def read_medicine():
    cursor.execute("SELECT * FROM medicines")
    medicines = cursor.fetchall()
    
    if medicines:
        print("Medicines table:")
        for medicine in medicines:
            print(f" ID: {medicine[0]}\n Name: {medicine[1]}\n Price: {medicine[2]}\n Quantity: {medicine[3]}")
    else:
        print("Medicines table is empty.")

# Function to read data from the medicines table
def read_sale():
    cursor.execute("SELECT * FROM sales")
    sales = cursor.fetchall()

    if sales:
        print("sales table:")
        for sales in sales:
             print(f" ID: {sales[0]}\n medicine_id: {sales[1]}\n Price: {sales[2]}\n quantity_sold: {sales[3]}\n sale_date: {sales[4]}")
    else:
        print("sales table is empty.")

# Function to read data from the suppliers table
def read_suppliers():
    cursor.execute("SELECT * FROM suppliers")
    suppliers = cursor.fetchall()

    if suppliers:
        print("suppliers table:")
        for suppliers in suppliers:
             print(f" ID: {suppliers[0]}\n contact_name: {suppliers[1]}\n contact_email: {suppliers[2]}")
    else:
        print("suppliers table is empty.")

# Function to read data from the prescriptions table
def read_prescriptions():
    cursor.execute("SELECT * FROM prescriptions")
    prescriptions = cursor.fetchall()

    if prescriptions:
        print("prescriptions table:")
        for prescriptions in prescriptions:
             print(f" ID: {prescriptions[0]}\n patient_name: {prescriptions[1]}\n doctor_name: {prescriptions[2]}\n date_prescribed: {prescriptions[3]}")
    else:
        print("prescriptions table is empty.")

# Function to read data from the prescriptions table
def read_staff():
    cursor.execute("SELECT * FROM staff")
    staff = cursor.fetchall()

    if staff:
        print("staff table:")
        for staff in staff:
             print(f" ID: {staff[0]}\n name: {staff[1]}\n position: {staff[2]}\n contact_email: {staff[3]}")
    else:
        print("staff table is empty.")
# Dictionary to handle different cases
options = {
    '1': read_medicine,
    '2': read_sale,
    '3': read_suppliers,
    '4': read_prescriptions,
    '5': read_staff
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
