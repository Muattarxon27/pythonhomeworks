import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee(employee):
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    @staticmethod
    def view_all_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
        print("Employee Records:")
        for record in records:
            print(record.strip())

    @staticmethod
    def search_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for record in file:
                if record.startswith(str(employee_id)):
                    print("Employee Found:")
                    print(record.strip())
                    return
        print("Employee not found.")

    @staticmethod
    def update_employee(employee_id, name, position, salary):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        updated_records = []
        found = False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for record in file:
                if record.startswith(str(employee_id)):
                    updated_records.append(f"{employee_id}, {name}, {position}, {salary}\n")
                    found = True
                else:
                    updated_records.append(record)
        if found:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee record updated successfully!")
        else:
            print("Employee not found.")

    @staticmethod
    def delete_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        updated_records = []
        found = False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for record in file:
                if not record.startswith(str(employee_id)):
                    updated_records.append(record)
                else:
                    found = True
        if found:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee record deleted successfully!")
        else:
            print("Employee not found.")

    @staticmethod
    def menu():
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                employee = Employee(emp_id, name, position, salary)
                EmployeeManager.add_employee(employee)
            elif choice == "2":
                EmployeeManager.view_all_employees()
            elif choice == "3":
                emp_id = input("Enter Employee ID to search: ")
                EmployeeManager.search_employee(emp_id)
            elif choice == "4":
                emp_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name: ")
                position = input("Enter new Position: ")
                salary = input("Enter new Salary: ")
                EmployeeManager.update_employee(emp_id, name, position, salary)
            elif choice == "5":
                emp_id = input("Enter Employee ID to delete: ")
                EmployeeManager.delete_employee(emp_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    EmployeeManager.menu()
