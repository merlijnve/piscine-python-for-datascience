import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
                -> list[int | float]:
    """Calculate BMI from height and weight."""
    try:
        h = np.array(height)
        w = np.array(weight)
        bmi = w / (h ** 2)
    except Exception as e:
        print(e)
        return
    return list(bmi)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply limit to BMI."""
    try:
        b = np.array(bmi)
        return b > limit
    except Exception as e:
        print(e)
        return
