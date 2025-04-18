def grossSalary():
    try:
        bs = float(input("Enter Basic Salary: "))
        if bs < 0:
            raise ValueError("Basic Salary cannot be negative.")
            return
        da = (bs * 70) / 100
        ta = (bs * 30) / 100
        hra = (bs * 10) / 100  

        grossSal = bs + da + ta + hra
        print("Gross Salary is: ", grossSal)
    except ValueError:
        print("Invalid input. Please enter a valid number for Basic Salary.")

grossSalary()