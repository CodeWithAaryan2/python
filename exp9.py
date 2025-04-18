num = int(input("Enter a number: "))

# Check if number is negative
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        print(f"The factorial of {num} is {fact}")