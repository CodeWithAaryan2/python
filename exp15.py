import pdb

def divide_numbers(a, b):
	pdb.set_trace()  # Set a breakpoint here
	try:
		result = a / b  # Possible division by zero error
	except ZeroDivisionError:
		return "Error: Division by zero is not allowed."
	return result

def main():
	num1 = 10
	num2 = 0  # Intentional error (division by zero)
	print("Starting Debugging...")
	output = divide_numbers(num1, num2)  # This will cause an error
	print(f"Result: {output}")

if __name__ == "__main__":
	main()