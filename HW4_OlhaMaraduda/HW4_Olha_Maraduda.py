# "Temperature Converter"

# Write a Python program that prompts the user to enter a temperature in Celcius and then converts it to Fahrenheit
# using the formula: F = (C * 9/5) + 32. Your program should then print out the converted te,perature in Fahrenheit.
# However, if the user enters a temperature  below -234.15C (the lowest possible temperature in the universe, also 
# known as absolyre zero), your program should print an error message instead of attempting to comvert the temperature.


celcius_temperature = float(input("Enter temperature in Celsius: "))

if celcius_temperature < -234.15:
    print("You've entered an impossible temperature. The lowest possible temperature is -273.15 Celsius.")
else: 
    fahrenheit_temperature = celcius_temperature * 9/5 + 32

    print(celcius_temperature, "is equivalent to", fahrenheit_temperature, "in Fahrenheit")
