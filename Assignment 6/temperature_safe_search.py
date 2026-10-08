from pathlib import Path

MIN_CELSIUS = 0
MAX_CELSIUS = 50

TEMPERATURE_FILE = Path(__file__).resolve().parent / "temperature_forloop.txt"


def main():
    celsius = get_celsius()

    fahrenheit_forloop = find_match_forloop(celsius)
    print(f"For-loop search result:   {fahrenheit_forloop}")

    if fahrenheit_forloop is not None:
        print(f"Match found: {celsius} Celsius is {fahrenheit_forloop:.2f} Fahrenheit.")
    else:
        fahrenheit = (celsius * 1.8) + 32
        append_record(celsius, fahrenheit)
        print(f"No match found. New record added: {celsius} Celsius = {fahrenheit:.2f} Fahrenheit.")


def get_celsius():
    good_value_received = False
    while not good_value_received:
        celsius_text = input(f"Enter a celsius degree ({MIN_CELSIUS}-{MAX_CELSIUS}): ")
        try:
            celsius = int(celsius_text)
            if celsius < MIN_CELSIUS or celsius > MAX_CELSIUS:
                print(f"Invalid input. Please enter a temperature between {MIN_CELSIUS} and {MAX_CELSIUS}.")
            else:
                good_value_received = True
        except ValueError:
            print(f"Invalid input. '{celsius_text}' is not a whole number.")

    return celsius


def find_match_forloop(celsius):
    fahrenheit = None
    try:
        with open(TEMPERATURE_FILE, "r") as infile:
            skip_header(infile)
            for line in infile:
                degree_text, fahrenheit_text = line.split("\t\t")
                if int(degree_text) == celsius:
                    fahrenheit = float(fahrenheit_text)
    except FileNotFoundError:
        print(f"Could not find the data file: {TEMPERATURE_FILE}")

    return fahrenheit


def skip_header(infile):
    infile.readline()  
    infile.readline() 


def append_record(celsius, fahrenheit):
    try:
        with open(TEMPERATURE_FILE, "a") as outfile:
            outfile.write(f"{celsius:>8}\t\t{fahrenheit:>8.2f}\n")
    except OSError as error:
        print(f"Could not write to the data file: {error}")


if __name__ == "__main__":
    main()