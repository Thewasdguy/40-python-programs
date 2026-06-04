# Student Manager

def student_manager():
    students = {}

    print("--- Student Manager ---")

    while True:
        print("\n1. Add Student  2. Find Student  3. Remove Student  4. View All  5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":

            # Roll Number Validation
            try:
                roll = int(input("Roll Number: "))
            except ValueError:
                print("Roll Number must be an integer.")
                continue

            # Name Validation
            name = input("Student Name: ").strip()

            if not name.replace(" ", "").isalpha():
                print("Name should contain only letters.")
                continue

            students[roll] = name
            print("Student added.")

        elif choice == "2":
            try:
                roll = int(input("Enter Roll Number: "))
                print(f"Student Name: {students.get(roll, 'Student not found')}")
            except ValueError:
                print("Roll Number must be an integer.")

        elif choice == "3":
            try:
                roll = int(input("Enter Roll Number to Remove: "))

                if students.pop(roll, None):
                    print("Student removed.")
                else:
                    print("Student not found.")

            except ValueError:
                print("Roll Number must be an integer.")

        elif choice == "4":
            print(f"\nTotal Students: {len(students)}")

            for roll, name in students.items():
                print(f"Roll No: {roll} | Name: {name}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

student_manager()
