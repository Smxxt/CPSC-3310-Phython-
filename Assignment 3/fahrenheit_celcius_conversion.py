ABSOLUTE_ZERO = -459.67

temp_input = float(input("Enter the temperature you want to convert: "))
temp_type = input("Enter the type of temperature (F for Fahrenheit, C for Celsius): ")

if temp_type == 'F':
    if temp_input >= ABSOLUTE_ZERO:
        celcius = (temp_input - 32) * 5 / 9
        print(f"The temperature in Celsius is: {celcius:.2f}")
    else:
        print("Invalid temperature. Please enter a temperature above absolute zero.")
elif temp_type == 'C':
    if temp_input >= ABSOLUTE_ZERO:
        fahrenheit = (temp_input * 9 / 5) + 32
        print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")
    else:
        print("Invalid temperature. Please enter a temperature above absolute zero.")
else:
    print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.")