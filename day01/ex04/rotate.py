import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt
import cv2


def main():
    """Main function which loads an image, \
            converts it to grayscale, zooms it and displays it"""
    try:
        np_img = ft_load("animal.jpeg")
        # print(np_img)
        gray = cv2.cvtColor(np_img, cv2.COLOR_BGR2GRAY)
        x_offset = 450
        y_offset = 100
        gray = gray[0+y_offset:400+y_offset, 0+x_offset:400+x_offset]
        gray = gray.reshape(400, 400, 1)
        print("The shape of image is: ", str(gray.shape) + " or (400, 400)")
        print(gray)

        transposed_image = np.empty((400, 400), dtype=gray.dtype)
        for i in range(400):
            for j in range(400):
                transposed_image[i][j] = gray[j][i][0]
        print("New shape after Transpose: ", transposed_image.shape)
        print(transposed_image)
        plt.imshow(transposed_image, cmap="gray")
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
