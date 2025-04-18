# Sample data: List of students enrolled in various entrance exams
students_CET = set(["Vishal", "Rohan", "Jay", "David", "Eva", "Pooja","Dev"])
students_JEE = set(["Vishal", "Jay", "Kiran", "Pooja", "Hena", "Ivy"])
students_NEET = set(["David", "Eva", "Jay", "Kiran", "Neha", "Vishal"])
# 1. Union: Students who are enrolled in at least one exam (CET, JEE, or NEET)
def union_student():
	union_students = students_CET.union(students_JEE, students_NEET)
	print("Students enrolled in at least one exam (Union):")
	print(union_students)

# 2. Intersection: Students who are enrolled in all three exams (CET, JEE, NEET)
def intersection_student():
	intersection_students = students_CET.intersection(students_JEE, students_NEET)
	print("\nStudents enrolled in all three exams (Intersection):")
	print(intersection_students)

# 3. Difference: Students who are enrolled only in CET but not in JEE or NEET
def difference_student():
	only_CET_students = students_CET.difference(students_JEE, students_NEET)
	print("\nStudents enrolled only in CET (Difference):")
	print(only_CET_students)

while True:
	n = int(input('1.Union \n2.Intersection\n3.difference\n4.Exit : '))
	if n == 1:
		union_student()
	elif n == 2:
		intersection_student()
	elif n == 3:
		difference_student()
	else:
		break
'''
s={4,5,6,7}
print(type(s))
s=set((4,5,6,7))
print(type(s))
'''