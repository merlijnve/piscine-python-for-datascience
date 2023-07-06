import pandas as pd
from pandas import DataFrame as Dataset


def load(path: str) -> Dataset:
    """
    Load a csv file from the given path and return a pandas DataFrame.
    """
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(e)
    return
