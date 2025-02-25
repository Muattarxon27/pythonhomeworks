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
    def view_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            employees = file.readlines()
        print("Employee Records:")
        for emp in employees:
            print(emp.strip())

    @staticmethod
    def search_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    print("Employee Found:")
                    print(line.strip())
                    return
        print("Employee not found.")

    @staticmethod
    def update_employee(employee_id, name=None, position=None, salary=None):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        updated = False
        employees = []
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(", ")
                if data[0] == employee_id:
                    if name:
                        data[1] = name
                    if position:
                        data[2] = position
                    if salary:
                        data[3] = str(salary)
                    updated = True
                employees.append(", ".join(data))
        if updated:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.write("\n".join(employees) + "\n")
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    @staticmethod
    def delete_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        employees = []
        deleted = False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if not line.startswith(employee_id + ","):
                    employees.append(line.strip())
                else:
                    deleted = True
        if deleted:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.write("\n".join(employees) + "\n")
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

if __name__ == "__main__":
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
            EmployeeManager.add_employee(Employee(emp_id, name, position, salary))
        elif choice == "2":
            EmployeeManager.view_employees()
        elif choice == "3":
            emp_id = input("Enter Employee ID to search: ")
            EmployeeManager.search_employee(emp_id)
        elif choice == "4":
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name (or press Enter to keep current): ") or None
            position = input("Enter new Position (or press Enter to keep current): ") or None
            salary = input("Enter new Salary (or press Enter to keep current): ") or None
            EmployeeManager.update_employee(emp_id, name, position, salary)
        elif choice == "5":
            emp_id = input("Enter Employee ID to delete: ")
            EmployeeManager.delete_employee(emp_id)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
