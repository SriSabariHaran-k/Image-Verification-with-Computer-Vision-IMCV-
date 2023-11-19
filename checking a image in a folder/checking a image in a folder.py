import cv2
import os
import numpy as np

image1 = cv2.imread("boat.jpg")
image1_resize = cv2.resize(image1,(1000, 1000))
cv2.imshow('The image to  be comnpared is:',image1_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

folder_path = "images"
image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif"))]
m=0

for image_file in image_files:
    image_path = os.path.join(folder_path,image_file)
    image2 = cv2.imread(image_path)

    hist1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0, 256])

    cv2.normalize(hist1, hist1, 0, 1, cv2.NORM_MINMAX)
    cv2.normalize(hist2, hist2, 0, 1, cv2.NORM_MINMAX)

    correlation = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    score = correlation

    threshold = 1

    if score >= threshold:
        m+=1
        image2_resize = cv2.resize(image2, (1000, 1000))
        cv2.imshow('Similar images:',image2_resize)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
print("Images found similar = ",m)     
