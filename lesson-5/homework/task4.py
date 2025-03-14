import statistics

# List of universities with name, student count, and tuition
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    """Extracts student enrollments and tuition fees from university data."""
    student_enrollments = [uni[1] for uni in universities]
    tuition_fees = [uni[2] for uni in universities]
    return student_enrollments, tuition_fees

def mean(values):
    """Calculates the mean (average) of a list of values."""
    return sum(values) / len(values)

def median(values):
    """Calculates the median of a list of values."""
    return statistics.median(values)

# Get enrollments and tuition data
students, tuition = enrollment_stats(universities)

# Calculate required values
total_students = sum(students)
total_tuition = sum(tuition)
student_mean = mean(students)
student_median = median(students)
tuition_mean = mean(tuition)
tuition_median = median(tuition)

# Display results
print("*" * 30)
print(f"Total students: {total_students:,}")  # Format with commas
print(f"Total tuition: $ {total_tuition:,}\n")

