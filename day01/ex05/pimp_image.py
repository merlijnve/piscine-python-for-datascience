import numpy as np
from numpy import ndarray as array
import matplotlib.pyplot as plt


def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    try:
        max_value = np.iinfo(array.dtype).max
        array = max_value - array
        plt.imshow(array)
        plt.show()
    except Exception as e:
        print(e)
    return array


def ft_red(array) -> array:
    """Keeps only the red color of the image received."""
    try:
        copy = array.copy()
        copy[:, :, 1] = 0
        copy[:, :, 2] = 0
        plt.imshow(copy)
        plt.show()
    except Exception as e:
        print(e)
    return copy


def ft_green(array) -> array:
    """Keeps only the green color of the image received."""
    try:
        copy = array.copy()
        copy[:, :, 0] = 0
        copy[:, :, 2] = 0
        plt.imshow(copy)
        plt.show()
    except Exception as e:
        print(e)
    return copy


def ft_blue(array) -> array:
    """Keeps only the blue color of the image received."""
    try:
        copy = array.copy()
        copy[:, :, 0] = 0
        copy[:, :, 1] = 0
        plt.imshow(copy)
        plt.show()
    except Exception as e:
        print(e)
    return copy


def ft_grey(array) -> array:
    """Transforms the image received in a grey scale."""
    try:
        copy = array.copy()
        copy[:, :, 0] = array[:, :, 1]
        copy[:, :, 1] = array[:, :, 1]
        copy[:, :, 2] = array[:, :, 1]
        plt.imshow(copy)
        plt.show()
    except Exception as e:
        print(e)
    return copy
