# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:42:39 2020

@author: hp
"""

import cv2
import imutils
#load the input image and show its dimensions, keeping in mind that
#image are represented as multi-dimensional NumPy array with
#shape no. rows (height) x no. column (width) x no. channels (depth)
image = cv2.imread("download.jpeg")
(h,w,d) = image.shape
print("width={}, height={}, depth{}0".format(w,h,d))
#dispaly the screen to our screen -- we will need to click the window
#open by OpenCV and press a key to our keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imwrite('OpenCV_Out_jpg', image)