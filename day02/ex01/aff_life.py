from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Creates a plot of the life expectancy of the Netherlands."""
    try:
        df = load("life_expectancy_years.csv")
        nl = df.loc[df["country"] == "Netherlands"]
        x = nl.columns[1:].astype(int)
        y = nl.values[0][1:]
        plt.plot(x, y)
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title("Netherlands Life expectancy Projections")
        plt.show()

    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    main()
