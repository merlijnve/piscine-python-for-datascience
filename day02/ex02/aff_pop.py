from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator


def parse_int(string):
    if 'k' in string:
        return int(float(string[:-1]) * 1000)
    elif 'M' in string:
        return int(float(string[:-1]) * 1000000)


def millions_formatter(x, pos):
    return f'{x / 1000000}M'


def main():
    """Creates a plot of the life expectancy of the Netherlands."""
    try:
        df = load("population_total.csv")
        nl = df.loc[df["country"] == "Netherlands"]
        fr = df.loc[df["country"] == "France"]

        timeframe = 2050 - 1800 + 2
        # add 2 because of the country column and to include the last

        x = nl.columns[1:timeframe].astype(int)
        y_nl = nl.values[0][1:timeframe]
        for y in range(len(y_nl)):
            y_nl[y] = parse_int(y_nl[y])
        y_fr = fr.values[0][1:timeframe]
        for y in range(len(y_fr)):
            y_fr[y] = parse_int(y_fr[y])

        plt.plot(x, y_fr, label="France")
        plt.plot(x, y_nl, label="Netherlands")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population Projections")

        # Set millions formatter for the y-axis
        formatter = FuncFormatter(millions_formatter)
        plt.gca().yaxis.set_major_formatter(formatter)

        locator = MaxNLocator(nbins=4)
        plt.gca().yaxis.set_major_locator(locator)

        plt.legend()
        plt.show()

    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    main()
