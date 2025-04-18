# Function for addition
# Function for addition
def add(a, b):
	return a + b

# Function for subtraction
def subtract(a, b):
	return a - b

# Function for multiplication
def multiply(a, b):
	return a * b

# Function for division
def divide(a, b):
	if b == 0:
		return "Error! Division by zero."
	return a / b

# Main function to perform calculations
def calculator():
	while True:
		print("\nSimple Calculator")
		print("1. Addition (+)")
		print("2. Subtraction (-)")
		print("3. Multiplication (*)")
		print("4. Division (/)")
		print("5. Exit")

		# User choice
		choice = input("Enter your choice (1/2/3/4/5): ")

		if choice == '5':
			print("Exiting the calculator. Goodbye!")
			break

		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))

		if choice == '1':
			print(f"Result: {add(num1, num2)}")
		elif choice == '2':
			print(f"Result: {subtract(num1, num2)}")
		elif choice == '3':
			print(f"Result: {multiply(num1, num2)}")
		elif choice == '4':
			print(f"Result: {divide(num1, num2)}")
		else:
			print("Invalid choice! Please enter a valid option.")

# Run the calculator
calculator()