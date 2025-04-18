class ListManager:
	def __init__(self):
		# Initializes an empty list
		self.data = []

	def display_list(self):
		# Displays the current list
		if not self.data:
			print("The list is currently empty.")
		else:
			print("Current List: ", self.data)

	def add_element(self, element):
		# Adds an element to the end of the list
		self.data.append(element)
		print(f"Element '{element}' has been added to the list.")

	def remove_element(self, element):
		# Removes an element from the list (if exists)
		if element in self.data:
			self.data.remove(element)
			print(f"Element '{element}' has been removed from the list.")
		else:
			print(f"Element '{element}' not found in the list.")

	def update_element(self, old_element, new_element):
		# Updates an element in the list (replaces old with new)
		if old_element in self.data:
			index = self.data.index(old_element)
			self.data[index] = new_element
			print(f"Element '{old_element}' has been updated to '{new_element}'.")
		else:
			print(f"Element '{old_element}' not found in the list.")

	def clear_list(self):
		# Clears all elements from the list
		self.data.clear()
		print("All elements have been removed from the list.")

def main():
	list_manager = ListManager()

	while True:
		print("\nList Manager Menu:")
		print("1. View list")
		print("2. Add an element")
		print("3. Remove an element")
		print("4. Update an element")
		print("5. Clear the list")
		print("6. Exit")

		choice = input("Enter your choice (1-6): ")

		if choice == "1":
			list_manager.display_list()
		elif choice == "2":
			element = input("Enter the element to add: ")
			list_manager.add_element(element)
		elif choice == "3":
			element = input("Enter the element to remove: ")
			list_manager.remove_element(element)
		elif choice == "4":
			old_element = input("Enter the element to update: ")
			new_element = input("Enter the new value: ")
			list_manager.update_element(old_element, new_element)
		elif choice == "5":
			list_manager.clear_list()
		elif choice == "6":
			print("Exiting the List Manager.")
			break
		else:
			print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
	main()