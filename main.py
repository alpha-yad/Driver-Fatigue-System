# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load an image from a file
image = cv2.imread('R.jpeg')

# Check if the image was loaded successfully
if image is None:
    print("Image not found")
else:
    # Display the original image
    # cv2.imshow('Original Image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    width,height=320,480
    resize_image=cv2.resize(image,(width,height))
    # cv2.imshow('resized img',resize_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    cv2.imshow('Grayscale Image', grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite('preprocessed_image.jpg', grayscale_image)
    ret,thresh1=cv2.threshold(resize_image,140,255,cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(resize_image, 140, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(resize_image, 140, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(resize_image, 140, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(resize_image, 140, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('Binary Threshold', thresh1)
    cv2.imshow('Binary Threshold Inverted', thresh2)
    cv2.imshow('Truncated Threshold', thresh3)
    cv2.imshow('Set to 0', thresh4)
    cv2.imshow('Set to 0 Inverted', thresh5)

    # De-allocate any associated memory usage
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
    # cv2.imwrite('thresh1.jpg', thresh1)
    # cv2.imwrite('thresh2.jpg', thresh2)
    # cv2.imwrite('thresh3.jpg', thresh3)
    # cv2.imwrite('thresh4.jpg', thresh4)
    # cv2.imwrite('thresh5.jpg', thresh5)
    plt.figure(figsize=(16, 16))
    ret1, th1 = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY)
    # Otsu's thresholding
    ret2, th2 = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # Otsu's thresholding after Gaussian filtering
    blur = cv2.


    (grayscale_image, (5, 5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # plot all the images and their histograms
    images = [image, 0, thresh1,
              resize_image, 0, thresh2,
              grayscale_image, 0, thresh3]
    titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
              'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
              'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
    for i in range(3):
        plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
        plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)

        plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
        plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
    plt.show()

