def personalized_greeting(name):
	greeting = f"Hello, {name}! Welcome to our community."
	return greeting

# Main program
if __name__ == "__main__":
	# Ask the user for their name
	user_name = input("Please enter your name: ")

	# Generate and print the personalized greeting
	greeting_message = personalized_greeting(user_name)
	print(greeting_message)