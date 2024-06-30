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

# Function to create a new column in a table
def create_new_column():
    table_name = input("Enter the name of the table where you want to create a new column: ")
    new_column_name = input("Enter the name of the new column: ")
    new_column_data_type = input("Enter the data type of the new column (e.g., INT, VARCHAR(255), DECIMAL(10, 2)): ")

    # Check if the table exists
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    table_exists = cursor.fetchone()

    if table_exists:
        # Create the new column
        alter_table_query = f"ALTER TABLE {table_name} ADD COLUMN {new_column_name} {new_column_data_type}"
        cursor.execute(alter_table_query)
        connection.commit()
        print(f"New column {new_column_name} with data type {new_column_data_type} added to table {table_name}.")
    else:
        print(f"Table {table_name} does not exist.")

# Dictionary to handle different cases
options = {
    '1': create_new_column,
}

while True:
    print("Choose an option:")
    print("1. Create a new column in a table")
    print("2. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '2':
        break

    selected_option = options.get(choice)
    if selected_option:
        selected_option()
    else:
        print("Invalid choice. Please select a valid option.")

# Close the cursor and connection when done
cursor.close()
connection.close()
