from typing import Any


def ft_std(*args: Any) -> float:
    """Function for calculating Standard Deviation"""
    std = ft_var(*args) ** 0.5
    return std


def ft_var(*args: Any) -> float:
    """Function for calculating Variance"""
    mean = ft_mean(*args)
    var = (sum([(x - mean) ** 2 for x in args]) / len(args))
    return var


def ft_quartile(*args: Any) -> float:
    """Function for calculating Quartile"""
    first_quartile = float(sorted(args)[len(args) // 4])
    third_quartile = float(sorted(args)[len(args) // 4 * 3])
    quartiles = [first_quartile, third_quartile]
    return quartiles


def ft_median(*args: Any) -> float:
    """Function for calculating Median"""
    median = sorted(args)[len(args) // 2]
    return median


def ft_mean(*args: Any) -> float:
    """Function for calculating Mean"""
    mean = sum(args) / len(args)
    return mean


def calculate(value: Any, *args: Any) -> None:
    """Function for executing the right functions"""
    if value == 'mean':
        print("mean : ", ft_mean(*args))
    elif value == 'median':
        print("median : ", ft_median(*args))
    elif value == 'quartile':
        print("quartile : ", ft_quartile(*args))
    elif value == 'std':
        print("std : ", ft_std(*args))
    elif value == 'var':
        print("var : ", ft_var(*args))


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Function for calculating Mean, Median, Quartile, Standard Deviation and\
         Variance"""
    try:
        functions = ['mean', 'median', 'quartile', 'std', 'var']
        if not args or not kwargs:
            print("ERROR")
            return
        for _, value in kwargs.items():
            if value not in functions:
                print("ERROR")
            else:
                calculate(value, *args)
    except Exception as e:
        print(e)
