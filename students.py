import json

try:
    with open('students.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("The file was not found.")
except json.JSONDecodeError:
    print("Error decoding JSON.")

# Accessing the list of students
students = data['students']

# Accessing the first student's name
first_student_name = students[0]['name']
print(first_student_name)  # Output: Alice

# Accessing the first student's age
first_student_age = students[0]['age']
print(first_student_age)  # Output: 20

# Accessing the second student's name
second_student_name = students[1]['name']
print(second_student_name)  # Output

# Iterating through the list of students
for student in students:
    name = student['name']
    age = student['age']
    print(f"Name: {name}, Age: {age}")
# Output:
# Name: Alice, Age: 24
# Name: Bob, Age: 22

# Adding a new student
new_student = {"name": "Charlie", "age": 23}
students.append(new_student)

# Writing the updated list back to the JSON file
with open('students.json', 'w') as file:
    json.dump(students, file, indent=4)

# Removing a student named "Bob"
students = [student for student in students if student['name'] != 'Bob']

# Writing the updated list back to the JSON file
with open('students.json', 'w') as file:
    json.dump(students, file, indent=4)

