from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Creates a plot of the life expectancy of the Netherlands."""
    try:
        df_life = load("life_expectancy_years.csv")
        df_gdp = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life = df_life["1900"]
        gdp = df_gdp["1900"]

        print(life)
        print(gdp)

        plt.scatter(gdp, life)
        plt.xlabel("Gross domestic product")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])

        plt.ylabel("Population")
        plt.title("1900")

        plt.show()

    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    main()
