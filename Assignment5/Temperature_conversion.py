ABSOLUTE_ZERO_FAHRENHEIT = -459.67
ABSOLUTE_ZERO_CELSIUS = -273.15


def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)

def get_temperature_type():
    while (
        temp_type := input(
            "Enter the type of temperature (F for Fahrenheit, C for Celsius): "
        )
        .strip()
        .upper()
    ) not in ("F", "C"):
        print(
            "Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius."
        )
    return temp_type

def get_temperature(temperature_type):
    if temperature_type == "F":
        limit = ABSOLUTE_ZERO_FAHRENHEIT
    else:
        limit = ABSOLUTE_ZERO_CELSIUS

    while (
        temp_val := float(
            input("Enter the temperature you want to convert: ")
        )
    ) < limit:
        print(
            f"Invalid temperature. Please enter a temperature above absolute zero ({limit})."
        )

    return temp_val

def display_conversion(temperature_type, temperature):
    if temperature_type == "F":
        celsius = (temperature - 32) * 5 / 9
        print(f"The temperature in Celsius is: {celsius:.2f}")
    else:
        fahrenheit = (temperature * 9 / 5) + 32
        print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")


if __name__ == "__main__":
    main()