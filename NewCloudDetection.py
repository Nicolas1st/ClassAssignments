import cv2
import numpy as np


file_name = r''
WHITE = 255
BLACK = 0


# нахождение среднего цвета квадрата
def average_color(image, corner_x, corner_y, grid_size):
    total = 0
    for x in range(grid_size):
        for y in range(grid_size):
            total += image[corner_y+y][corner_x+x]
    return total / grid_size**2


# изменение всех пикселей квадрата на средний цвет квадрата
def change_roi_color(image, corner_x, corner_y, convert_to, grid_size):
    for x in range(grid_size):
        for y in range(grid_size):
            image[corner_y + y][corner_x + x] = convert_to
    return image


# нахождение облаков
def detect_clouds(file_name, grid_size=10):

    orig_img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
    modified = orig_img.copy()

    height, width = orig_img.shape
    print(height, width)

    horizontal_tiles = height // grid_size
    vertical_tiles = width // grid_size

    list_representation = [[[] for _ in range(vertical_tiles)] for _ in range(horizontal_tiles)]

    new_height = (height // grid_size) * grid_size
    new_width = (width // grid_size) * grid_size
    print(new_width, new_height)

    for corner_x in range(0, new_width, grid_size):
        for corner_y in range(0, new_height, grid_size):
            average_shade = average_color(modified, corner_x, corner_y, grid_size)
            if average_shade > 150:
                modified = change_roi_color(modified, corner_x, corner_y, WHITE, grid_size)
                hor_tile = corner_x//grid_size
                ver_tile = corner_y//grid_size
                list_representation[ver_tile][hor_tile] = 1
            else:
                modified = change_roi_color(modified, corner_x, corner_y, BLACK, grid_size)
                hor_tile = corner_x // grid_size
                ver_tile = corner_y // grid_size
                list_representation[ver_tile][hor_tile] = 0

    return orig_img, modified, list_representation


orig_img, modified, list_repr = detect_clouds(file_name)
for line in list_repr:
    print(line)

cv2.imshow('Original', orig_img)
cv2.imshow('Modified', modified)
cv2.waitKey(0)
cv2.destroyAllWindows()
