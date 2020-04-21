import cv2
import numpy as np


filename = ''

def average_color(image, corner_x, corner_y, size=10):
    total = 0
    for x in range(size):
        for y in range(size):
            total += image[corner_y+y][corner_x+x]
    return total / size**2


def change_roi_color(image, corner_x, corner_y, convert_to, size=10):
    for x in range(size):
        for y in range(size):
            image[corner_y + y][corner_x + x] = convert_to
    return image


# load the image
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# check the image resolution
height, width = img.shape
interval = 10

# copying the image
modified_img = img.copy()

# colors to convert to
WHITE = 255
BLACK = 0


# iterating over the image using rectangles
for corner_x in range(0, width-interval, interval):
    for corner_y in range(0, height-interval, interval):
        average_shade = average_color(modified_img, corner_x, corner_y)
        print(average_shade)
        if average_shade > 100:
            modified_img = change_roi_color(modified_img, corner_x, corner_y, WHITE)
        else:
            modified_img = change_roi_color(modified_img, corner_x, corner_y, BLACK)


cv2.imshow('Cloud', img)
cv2.imshow('Altered', modified_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
