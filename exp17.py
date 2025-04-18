import re

def extract_data(filename):
	with open(filename, 'r') as file:
		text = file.read()

	names = re.findall(r'\b([A-Z][a-z]+\s[A-Z][a-z]+)\b', text)  # Extracting Indian names
	emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)  # Extracting emails
	phones = re.findall(r'\+91[-.\s]?\d{10}|\d{5}[-.\s]?\d{5}', text)  # Indian phone numbers
	dates = re.findall(r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})\b', text)  # DD/MM/YYYY format

	print("Extracted Indian Names:", names)
	print("Extracted Emails:", emails)
	print("Extracted Phone Numbers:", phones)
	print("Extracted Dates:", ["/".join(date) for date in dates])

# Run the extraction function with a sample text file
extract_data("sample.txt")