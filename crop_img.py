# D:\photo\_DIPLOMKA\Segmentation\data\train_images

# Import packages
import os
import cv2

image_num = 1
for root, dirs, files in os.walk("D:\\photo\\_DIPLOMKA\\Segmentation\\data\\train_masks"):
    for name in files:
        path = os.path.join(root, name)
        img = cv2.imread(path, 0)
        print(img.shape)  # Print image shape
        # Cropping an image
        cropped_image = img[0:2560, 676:3236]
        # Save the cropped image
        cv2.imwrite("D:\\photo\\_DIPLOMKA\\Segmentation\\data\\cropped_masks\\img"+str(image_num)+".png", cropped_image)
        image_num +=1
