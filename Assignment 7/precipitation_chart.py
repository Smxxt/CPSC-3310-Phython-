import os # for handle file reading flexibly
import matplotlib.pyplot as plt # for using matplotlib to create graphs

# Name of the text file created by precipitation_analysis.py.
INPUT_FILE = 'precipitation.txt'


def main():
    months, precipitation = read_precipitation_file(INPUT_FILE)

    if len(months) > 0:
        show_bar_chart(months, precipitation)


def read_precipitation_file(filename):
    # Read lines in the form month,amount and return two lists: months and precipitation
    months = []
    precipitation = []

    # Look for the file in the same folder as this program.
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    try:
        with open(path, 'r') as input_file:
            # read the lines from file and get month and precipitation respectively from each line using tuple unpacking
            for line in input_file:
                # Strip newline and split the CSV line into month and amount strings
                month_str, amount_str = line.strip().split(',')
                # add the readings to two lists respectively
                months.append(month_str)
                precipitation.append(float(amount_str))
    except FileNotFoundError:
        print(f"Could not find '{filename}'. Run precipitation_analysis.py first.")
    except ValueError:
        print(f"'{filename}' is not in the expected 'month,amount' format.")
        months = []
        precipitation = []

    return months, precipitation


def show_bar_chart(months, precipitation):
    # Use the first three letters of each month name so the labels fit.
    short_names = [month[:3] for month in months]

    # Use MatPlotLib to draw the bar chart as you learned from the lecture
    plt.bar(short_names, precipitation, color="steelblue")
    
    # Add title and axis labels matching assignment specifications
    plt.title("Monthly Precipitation")
    plt.xlabel("Month")
    plt.ylabel("Precipitation")
    
    # Display the graph window
    plt.show()


# Call the main function only if this file is run directly.
if __name__ == '__main__':
    main()