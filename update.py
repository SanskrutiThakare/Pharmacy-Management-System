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

# Function to update data in the medicines table
def update_medicine():
    medicine_id = int(input("Enter the ID of the medicine to update: "))
    column_to_update = input("Enter the column to update (e.g., name, price, quantity): ").strip()
    new_value = input(f"Enter the new value for {column_to_update}: ")
    
    # Check if the medicine with the given ID exists
    cursor.execute("SELECT * FROM medicines WHERE id = %s", (medicine_id,))
    existing_medicine = cursor.fetchone()
    
    if existing_medicine:
        update_medicine_query = f"UPDATE medicines SET {column_to_update} = %s WHERE id = %s"
        cursor.execute(update_medicine_query, (new_value, medicine_id))
        connection.commit()
        print("Medicine data updated.")
    else:
        print("Medicine with ID", medicine_id, "does not exist.")

# Function to update data from the sales table
def update_sale():
    sale_id = int(input("Enter the ID of the sale to update: "))
    column_to_update1 = input("Enter the column to update (e.g., id, medicine_id, quantity_sold,sale_date): ").strip()
    new_value1 = input(f"Enter the new value for {column_to_update1}: ")

    # Check if the sale with the given ID exists
    cursor.execute("SELECT * FROM sales WHERE id = %s", (sale_id,))
    existing_sale = cursor.fetchone()

    if existing_sale:
        update_sale_query = f"UPDATE sales SET {column_to_update1} = %s WHERE id = %s"
        cursor.execute(update_sale_query, (new_value1, sale_id))
        connection.commit()
        print("Sale data updated.")
    else:
        print("Sale with ID", sale_id, "does not exist.")

# Function to update data from the suppliers table
def update_supplier():
    supplier_id = int(input("Enter the ID of the supplier to update: "))
    column_to_update2 = input("Enter the column to update (e.g., id, contact_name, contact_email): ").strip()
    new_value2 = input(f"Enter the new value for {column_to_update2}: ")
    
    # Check if the sale with the given ID exists
    
    cursor.execute("SELECT * FROM suppliers WHERE id = %s", (supplier_id,))
    existing_supplier = cursor.fetchone()

    if existing_supplier:
        update_supplier_query = f"UPDATE suppliers SET {column_to_update2} = %s WHERE id = %s"
        cursor.execute(update_supplier_query, (new_value2,supplier_id))
        connection.commit()
        print("Supplier data updated.")
    else:
        print("Supplier with ID", supplier_id, "does not exist.")

# Function to update data from the prescriptions table
def update_prescription():
    prescription_id = int(input("Enter the ID of the prescription to update: "))
    column_to_update3 = input("Enter the column to update (e.g., id, patient_name, doctor_name,date_prescribed): ").strip()
    new_value3= input(f"Enter the new value for {column_to_update3}: ")
    
    # Check if the sale with the given ID exists
    cursor.execute("SELECT * FROM prescriptions WHERE id = %s", (prescription_id,))
    existing_prescription = cursor.fetchone()

    if existing_prescription:
        update_prescription_query = f"UPDATE prescriptions SET {column_to_update3} = %s WHERE id = %s"
        cursor.execute(update_prescription_query, (new_value3,prescription_id))
        connection.commit()
        print("Prescription data updated.")
    else:
        print("Prescription with ID", prescription_id, "does not exist.")
        

# Function to delete data from the staff table
def update_staff():
    staff_id = int(input("Enter the ID of the staff member to update: "))
    column_to_update4 = input("Enter the column to update (e.g., id, name, position,contact_email): ").strip()
    new_value4= input(f"Enter the new value for {column_to_update4}: ")
    
    # Check if the sale with the given ID exists
    cursor.execute("SELECT * FROM staff WHERE id = %s", (staff_id,))
    existing_staff = cursor.fetchone()

    if existing_staff:
        update_staff_query = f"UPDATE staff SET {column_to_update4} = %s WHERE id = %s"
        cursor.execute(updatee_staff_query, (new_value4,staff_id))
        connection.commit()
        print("Staff data updated.")
    else:
        print("staff with ID", staff_id, "does not exist.")
        

# Dictionary to handle different cases
options = {
    '1': update_medicine,
    '2': update_sale,
    '3': update_supplier,
    '4': update_prescription,
    '5': update_staff
}

while True:
    print("Choose a table to update data from:")
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
