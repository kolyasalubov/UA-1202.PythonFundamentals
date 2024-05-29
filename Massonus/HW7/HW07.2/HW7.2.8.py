def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg >= distance_to_pump:
        return True
    else:
        return False


print("Is it possible?", zero_fuel(int(input("Input distance: ")), int(input("Input miles per gallon: ")), int(input("Input fuel left: "))))
