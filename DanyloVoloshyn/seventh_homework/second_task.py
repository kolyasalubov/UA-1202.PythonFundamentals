def rectangle_area(length, width):
      area = length * width
      return area


def triangle_area(base, height):
      area = 0.5 * base * height
      return area


def circle_area(radius):
      area = 3.14159 * radius**2
      return area


while True:
      choose_function = input("Hello, please select the function you need(rectangle, triangle, circle) or type 'exit' to quit: ")
      
      if choose_function == "exit":
            print("\nGoodbye!")
            break
      elif choose_function == "rectangle":
            length = float(input("\nEnter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print(f"The area of the rectangle is: {rectangle_area(length, width)}\n")
      elif choose_function == "triangle":
            base = float(input("\nEnter the base of the triangle: "))
            height = float(input("Enter the height of the triangel: "))
            print(f"The are of the triangle is: {triangle_area(base, height)}\n")
      elif choose_function == "circle":
            radius = float(input("\nEnter the radius of the circle: "))
            print(f"The area of the circle is: {circle_area(radius)}\n")
      else:
            print("\nInvalid selection, please choose rectangle, triangle, or circle.\n")
