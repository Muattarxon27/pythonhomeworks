import os
import string
from collections import Counter

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

def manage_sample_file():
    if not os.path.exists("sample.txt"):
        print("sample.txt does not exist. Please create it by typing a paragraph:")
        with open("sample.txt", "w") as file:
            paragraph = input("Enter paragraph: ")
            file.write(paragraph)
            print("sample.txt created successfully.")
    else:
        with open("sample.txt", "r") as file:
            print("Contents of sample.txt:")
            print(file.read())

def count_word_frequency():
    if not os.path.exists("sample.txt"):
        print("sample.txt does not exist. Please create it first.")
        return
    
    with open("sample.txt", "r") as file:
        text = file.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        word_count = Counter(words)
        
        total_words = sum(word_count.values())
        print(f"Total number of words: {total_words}")
        
        top_words = word_count.most_common(5)
        print("Top 5 most common words:")
        for word, count in top_words:
            print(f"{word}: {count}")
        
        with open("word_count_report.txt", "w") as report:
            report.write(f"Total number of words: {total_words}\n")
            report.write("Top 5 most common words:\n")
            for word, count in top_words:
                report.write(f"{word}: {count}\n")
        
        print("Word frequency report saved to word_count_report.txt")

def main():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Manage sample.txt")
        print("7. Count word frequency in sample.txt")
        print("8. Exit")
        
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
            manage_sample_file()
        elif choice == "7":
            count_word_frequency()
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
