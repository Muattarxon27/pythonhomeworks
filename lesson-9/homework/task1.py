import csv
from collections import defaultdict

def read_grades(filename):
    grades = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])  # Convert grade to integer
            grades.append(row)
    return grades

def calculate_average(grades):
    subject_totals = defaultdict(list)
    
    for entry in grades:
        subject_totals[entry['Subject']].append(entry['Grade'])
    
    averages = {subject: sum(grades) / len(grades) for subject, grades in subject_totals.items()}
    return averages

def write_averages(filename, averages):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 1)])

# File names
grades_file = "grades.csv"
averages_file = "average_grades.csv"

# Process the CSV files
grades = read_grades(grades_file)
averages = calculate_average(grades)
write_averages(averages_file, averages)

print("Average grades have been calculated and saved to average_grades.csv.")
