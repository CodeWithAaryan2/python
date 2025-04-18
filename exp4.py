def add(a, b):
    c = a + b
    return c
def sub(a, b):
    c = a - b
    return c
def mul(a, b):
    c = a * b
    return c
def div(a, b):
    c = a / b
    return c
def mod(a, b):
    c = a % b
    return c

a = int(input("Enter No1: "))
b = int(input("Enter No2: "))
z = add(a, b)
print("Addition:", z)
a = int(input("Enter No1: "))
b = int(input("Enter No2: "))
z = sub(a, b)
print("Subtraction:", z)
a = int(input("Enter No1: "))
b = int(input("Enter No2: "))
z = mul(a, b)
print("Multiplication:", z)
a = int(input("Enter No1: "))
b = int(input("Enter No2: "))
z = div(a, b)
print("Division:", z)

a = int(input("Enter No1: "))
b = int(input("Enter No2: "))
z = mod(a, b)
print("Mod:", z)