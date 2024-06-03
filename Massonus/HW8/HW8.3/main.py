import calculations as calc


def main():
    print("Make your choice")
    print("1. To calculate area of a rectangle")
    print("2. To calculate area of a triangle")
    print("3. To calculate area of a circle")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            print(calc.area_of_rectangle(float(input("Enter a length: ")), float(input("Enter a width: "))))
        case "2":
            print(calc.area_of_triangle(float(input("Enter your length: ")), float(input("Enter your width: "))))
        case "3":
            print(calc.area_of_circle(float(input("Enter your radius: "))))
        case _:
            print("Invalid choice, try again \n")
            main()


main()
