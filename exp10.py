def check_prime(number):
	count = 0
	limit = number // 2  # The largest possible divisor of a number is half of the number.

	# Check for divisors from 2 to number//2
	for i in range(2, limit + 1):
		if number % i == 0:  # If number is divisible by i
			count += 1  # Increment count because it's divisible by i
			break  # No need to check further, we know the number is not prime.

	# If count is 1 or more, it's not a prime
	if count >= 1:
		print(f"{number} is not a prime number.")
	else:
		print(f"{number} is a prime number.")

# Function call
check_prime(29)
check_prime(8)