
ABSOLUTE_ZERO_CELSIUS = -273.15  

celsius_limit = int(input("Enter a celsius degree: "))

while celsius_limit < ABSOLUTE_ZERO_CELSIUS:
    print(f"Error: Temperature cannot be below absolute zero ({ABSOLUTE_ZERO_CELSIUS}°C).")
    celsius_limit = int(input("Enter a celsius degree: "))


print(f"{'Celsius':<12}{'Fahrenheit':<12}")
print("-" * 28)


for celsius in range(0, celsius_limit + 1):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:<12}{fahrenheit:<12.1f}")