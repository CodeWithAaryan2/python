import re

def validate_phone(phone):
	phone_pattern = re.compile(r'^(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}$')
	return bool(phone_pattern.match(phone))

def validate_email(email):
	email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
	return bool(email_pattern.match(email))

def main():
	phone_number = input("Enter your phone number: ")
	email_id = input("Enter your email ID: ")

	if validate_phone(phone_number):
		print("✅ Valid phone number.")
	else:
		print("❌ Invalid phone number.")

	if validate_email(email_id):
		print("✅ Valid email ID.")
	else:
		print("❌ Invalid email ID.")

if __name__ == "__main__":
	main()