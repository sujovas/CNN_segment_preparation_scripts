import numpy as np
from matplotlib import pyplot as plt
from patchify import patchify
import cv2
import os

mainimg_num = 1
for root, dirs, files in os.walk("D:\\photo\\_DIPLOMKA\\Segmentation\\data\\cropped_masks"):
    for name in files:
        path = os.path.join(root, name)
        img = cv2.imread(path, 0)
        # print(img.shape)  # Print image shape
        # patchifying
        patches_img = patchify(img, (512,512), step=384)
        image_num = 1
        for i in range(patches_img.shape[0]):
            for j in range(patches_img.shape[1]):
                single_patch_img = patches_img[i,j,:,:]
                cv2.imwrite("D:\\photo\\_DIPLOMKA\\Segmentation\\data\\cropped_patches_masks\\img" + str(mainimg_num) + '_' + str(image_num) + ".png", single_patch_img)
                image_num += 1
        mainimg_num += 1
        # Save the cropped image

