import cv2


def ft_load(path: str) -> cv2.Mat:
    """Load an image from a path and return it as a numpy array"""
    try:
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        print("The shape of image is: ", str(img.shape))
        print(img)
    except Exception as e:
        print("An exception occurred: ", e)
    return img
