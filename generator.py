# School Management System

students = []

while True:
    print("\n--- School Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Student Name: ")
        roll_no = input("Enter Roll Number: ")

        m1 = int(input("Enter English Marks: "))
        m2 = int(input("Enter Maths Marks: "))
        m3 = int(input("Enter Science Marks: "))

        total = m1 + m2 + m3
        average = total / 3

        if m1 >= 35 and m2 >= 35 and m3 >= 35:
            result = "Pass"
        else:
            result = "Fail"

        students.append([name, roll_no, total, average, result])

        print("Student record added successfully!")

    elif choice == 2:
        print("\n--- Student Records ---")
        for student in students:
            print("Name:", student[0])
            print("Roll No:", student[1])
            print("Total Marks:", student[2])
            print("Average:", student[3])
            print("Result:", student[4])
            print("----------------------")

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")