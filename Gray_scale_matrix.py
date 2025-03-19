# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 11:43:34 2025

@author: USER
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np 

# Create a 3x3 grayscale image matrix
gray_image = np.array([[0, 50, 100],
                       [150, 200, 255],
                       [80, 120, 180]], dtype = np.uint8)

print(gray_image)
plt.imshow(gray_image, cmap = 'gray')
plt.axis("Off")
plt.show()