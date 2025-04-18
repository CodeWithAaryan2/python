students = {}

def add_student():
	name = input("Enter student name: ")
	grade = input("Enter grade: ")
	attendance = int(input("Enter attendance percentage: "))
	students[name] = {"grade": grade, "attendance": attendance}
	print("Student added successfully.")

def update_student():
	name = input("Enter student name to update: ")
	if name in students:
		grade = input("Enter new grade: ")
		attendance = int(input("Enter new attendance percentage: "))
		students[name] = {"grade": grade, "attendance": attendance}
		print("Record updated successfully.")
	else:
		print("Student not found.")

def display_students():
	for name, info in students.items():
		print(f"{name}: Grade - {info['grade']}, Attendance - {info['attendance']}%")

while True:
	print("\n1. Add Student\n2. Update Student\n3. Display Students\n4. Exit")
	choice = int(input("Enter your choice: "))
	if choice == 1:
		add_student()
	elif choice == 2:
		update_student()
	elif choice == 3:
		display_students()
	elif choice == 4:
		print("Exiting...")
		break
	else:
		print("Invalid choice. Try again.")