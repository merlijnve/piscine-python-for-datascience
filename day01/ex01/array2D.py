import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print shape of a list of lists, \
        slice it and return it as a list of lists"""
    try:
        fam = np.array(family)
        print("My shape is : ", fam.shape)
        fam = fam[start:end]
        print("My new shape is : ", fam.shape)
    except Exception as e:
        print("An exception occurred: ", e)
    return fam.tolist()
