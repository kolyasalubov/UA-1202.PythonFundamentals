celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

if celsius < -273.15:
    print("Error: Temperature below absolute zero!")
else:
    print(f"{celsius}°C is equivalent to {fahrenheit}°F")