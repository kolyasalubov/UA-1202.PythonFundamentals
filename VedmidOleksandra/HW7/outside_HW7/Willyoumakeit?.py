# You were camping with your friends far away from home, but when it's time to go back,
# you realize that your fuel is running out and the nearest pump is 50 miles away!
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
#
# Function should return true if it is possible and false if not.

# Distance you can travel=Fuel left (in gallons)×Miles per gallon
# In this case, you know:
#
# The nearest pump is 50 miles away. Your car runs on 25 miles per gallon. You have 2 gallons left.
# So, using the formula:
# Distance you can travel = 2 gallons × 25 miles per gallon
# Distance you can travel=2 gallons×25 miles per gallon
#
# Distance you can travel = 50 miles
# Distance you can travel=50 miles
#
# Since the distance you can travel (50 miles) is equal to the distance to the nearest pump (50 miles),
# you have just enough fuel to reach the nearest pump.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    distance_you_can_travel = fuel_left * mpg
    if distance_you_can_travel >= distance_to_pump:
        return True
    else:
        return False


# Example usage:
print(zero_fuel(50, 25, 2))  # Output: True
print(zero_fuel(60, 25, 2))  # Output: False
