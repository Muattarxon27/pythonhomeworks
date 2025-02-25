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
    def load_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            return []
        with open(EmployeeManager.FILE_NAME, "r") as file:
            return [line.strip().split(", ") for line in file.readlines()]

    @staticmethod
    def save_employees(employees):
        with open(EmployeeManager.FILE_NAME, "w") as file:
            for emp in employees:
                file.write(", ".join(emp) + "\n")

    @staticmethod
    def add_employee(employee):
        employees = EmployeeManager.load_employees()
        if any(emp[0] == employee.employee_id for emp in employees):
            print("Error: Employee ID must be unique.")
            return
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    @staticmethod
    def view_all_employees():
        employees = EmployeeManager.load_employees()
        if not employees:
            print("No employee records found.")
            return
        print("Employee Records:")
        for emp in sorted(employees, key=lambda x: x[1]):  # Sort by name
            print(", ".join(emp))

    @staticmethod
    def search_employee(employee_id):
        employees = EmployeeManager.load_employees()
        for emp in employees:
            if emp[0] == employee_id:
                print("Employee Found:")
                print(", ".join(emp))
                return
        print("Employee not found.")

    @staticmethod
    def update_employee(employee_id, name, position, salary):
        employees = EmployeeManager.load_employees()
        for emp in employees:
            if emp[0] == employee_id:
                emp[1], emp[2], emp[3] = name, position, salary
                EmployeeManager.save_employees(employees)
                print("Employee record updated successfully!")
                return
        print("Employee not found.")

    @staticmethod
    def delete_employee(employee_id):
        employees = EmployeeManager.load_employees()
        new_employees = [emp for emp in employees if emp[0] != employee_id]
        if len(new_employees) == len(employees):
            print("Employee not found.")
        else:
            EmployeeManager.save_employees(new_employees)
            print("Employee record deleted successfully!")

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

