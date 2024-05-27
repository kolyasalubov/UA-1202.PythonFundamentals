celsius_temperature = float(input("Enter the temperature in degrees Celsius: "))
fahrenheit_temperature = (celsius_temperature * 9/5) + 32

if celsius_temperature >= -273.15:
      print(f"{celsius_temperature}°C is equivalent to {fahrenheit_temperature}°F")
elif celsius_temperature < -273.15:
      print("Error: Temperature below absolute zero (-273.15°C)")
else:
      print("Syntax error")
