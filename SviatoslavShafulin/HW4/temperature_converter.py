TempInCels = float(input("Enter the temperature in Celsius: "))

if TempInCels >= -273.15:
    print(f"{TempInCels} °C is equivalent to",(TempInCels*9/5)+32,"°F")
else:
    print("Error: Temperature below absolute zero (-273.15°C)")