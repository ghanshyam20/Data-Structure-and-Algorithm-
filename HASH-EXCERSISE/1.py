# i have made student grade dictorinary , using this
grades = {
    "Anna": 5,
    "Mikko": 4,
    "Sara": 3
}

while True:
    print("\n Student Grade Menu ")
    print("1. Add / Update student grade")
    print("2. Search student grade")
    print("3. Print all students")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = int(input("Enter grade: "))
        grades[name] = grade
        print("Grade added/updated successfully")

    elif choice == "2":
        name = input("Enter student name to search: ")
        if name in grades:
            print(name, "grade is:", grades[name])
        else:
            print("Student not found")

    elif choice == "3":
        print("\nAll students and grades:")
        for student in grades:
            print(student, ":", grades[student])

    elif choice == "0":
        print("Exiting program...")
        break

    else:
        print("bro wrong chocie haha, try again")