from Area_calculator import area_of_rectangle, area_of_triangle, area_of_circle

def user_choosing_options():
    while True:
        print("Choose the figure to calculate the area:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            a = float(input("Enter the length of the rectangle: "))
            b = float(input("Enter the width of the rectangle: "))
            print(f"The area of the rectangle is: {area_of_rectangle(a, b)}")
        elif choice == '2':
            h = float(input("Enter the height of the triangle: "))
            a = float(input("Enter the base of the triangle: "))
            print(f"The area of the triangle is: {area_of_triangle(h, a)}")
        elif choice == '3':
            r = float(input("Enter the radius of the circle: "))
            print(f"The area of the circle is: {area_of_circle(r)}")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the program
if __name__ == "__main__":
    user_choosing_options()
