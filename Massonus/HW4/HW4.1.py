def temperature_converter(celsius):
    if celsius < -273.15:
        return "Error: Temperature below absolute zero (273.15°C)"

    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C is equivalent to {fahrenheit}°F"


print(temperature_converter(float(input("Enter temperature in Celsius: "))))
