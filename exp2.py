import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def main():
    print("Choose a geometric figure to calculate the area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {calculate_circle_area(radius):.2f}")
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {calculate_rectangle_area(length, width):.2f}")
    elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {calculate_triangle_area(base, height):.2f}")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()