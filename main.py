
while True:
    print("Choose an operation:")
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    print("4. Read")
    print("5. Create")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        import insert 
    elif choice == '2':
        import delete
    elif choice == '3':
        import update
    elif choice == '4':
        import read
    elif choice == '5':
        import create
    elif choice=='6':
        break;
    else:
        print("Invalid choice. Please select a valid option.")
