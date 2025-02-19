def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        salary = input("Enter Employee Salary: ")
        
        record = f"{emp_id}, {name}, {position}, {salary}\n"
        file.write(record)
        print("Employee record added successfully.")

def view_employees():
    with open("employees.txt", "r") as file:
        records = file.readlines()
        for record in records:
            print(record.strip())

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    with open("employees.txt", "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                print("Employee Found:", record.strip())
                return
    print("Employee not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    lines = []
    found = False
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    
    with open("employees.txt", "w") as file:
        for record in lines:
            if record.startswith(emp_id + ","):
                name = input("Enter new Employee Name: ")
                position = input("Enter new Employee Position: ")
                salary = input("Enter new Employee Salary: ")
                file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                file.write(record)
    
    if found:
        print("Employee record updated successfully.")
    else:
        print("Employee not found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    lines = []
    found = False
    with open("employees.txt", "r") as file:
        lines = file.readlines()
    
    with open("employees.txt", "w") as file:
        for record in lines:
            if not record.startswith(emp_id + ","):
                file.write(record)
            else:
                found = True
    
    if found:
        print("Employee record deleted successfully.")
    else:
        print("Employee not found.")

def main():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
