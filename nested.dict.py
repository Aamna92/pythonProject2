#Nested Dictionaries:
#Basic Creation: Create a dictionary of students.
#Each student (key) should have another dictionary as a value containing their age and grade.
students = {'Ali': {'age': 10, 'grade': 5},
            'Bob': {'age': 12, 'grade': 7},
            'Musab': {'age': 15, 'grade': 9}
            }
print(students)

#Accessing Nested Elements: Fetch the age of a specific student.
print(students['Musab']['age'])

#Updating Nested Dictionary: Update the grade of a student.
students['Ali']['grade'] = 6
print(students['Ali']['grade'])

#Looping through Nested Dictionaries: Print out each student's name along with their age and grade.
for students, info in students.items():
    age = info["age"]
    grade = info["grade"]
    print(f"{students}: Age - {age}, Grade - {grade}")


