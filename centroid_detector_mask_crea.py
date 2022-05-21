import cv2
# import the necessary packages
import numpy as np
import argparse
import glob
import cv2
from matplotlib import pyplot as plt
import random as rng
from PIL import Image
import math
import os


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    # return the edged image
    return edged


image_num = 1
for root, dirs, files in os.walk("D:\\photo\\_DIPLOMKA\\uNetTrain\\train_masks"):
    for name in files:
        path = os.path.join(root, name)
        img = cv2.imread(path, 0)
# img = img.resize((1920,1080))
        blurred = cv2.GaussianBlur(img, (3, 3), 0)

# wide = cv2.Canny(blurred, 10, 200)
# tight = cv2.Canny(blurred, 225, 250)
        auto = auto_canny(blurred)

        contours, hierarchy = cv2.findContours(auto, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Approximate contours to polygons + get bounding rects and circles
        contours_poly = [None] * len(contours)
        boundRect = [None] * len(contours)
        centers = [None] * len(contours)
        radius = [None] * len(contours)
        for i, c in enumerate(contours):
            contours_poly[i] = cv2.approxPolyDP(c, 3, True)
            boundRect[i] = cv2.boundingRect(contours_poly[i])
            centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])

        drawing = np.zeros((auto.shape[0], auto.shape[1], 3), dtype=np.uint8)

# Draw polygonal contour + bonding rects + circles
        for i in range(len(contours)):
    # color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
            color = (255,255,255)
    # cv2.drawContours(drawing, contours_poly, i, color)
    # cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)
            if radius[i]>20:
                cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(1), color, thickness=(math.ceil(radius[i])) + 10)
            else:
                cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(1), color, thickness=(math.ceil(radius[i])) + 20)

        blurred_drawing = cv2.GaussianBlur(drawing, (35, 35), 30)
        cv2.imwrite("D:\\photo\\_DIPLOMKA\\uNetTrain\\train_masks_gauss\\img" + str(image_num) + ".png", blurred_drawing)

        # print(centers)
        # print(radius)
        # cv2.imshow('Contours', blurred_drawing)
        # cv2.waitKey(0)
        image_num += 1
# # show the images
# cv2.imshow("Original", img)
# cv2.imshow("Edges wide", wide)
# cv2.imshow("Edges tight", tight)
# cv2.imshow("Edges auto", auto)
# cv2.waitKey(0)
