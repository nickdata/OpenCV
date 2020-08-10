# OpenCV
Computer Vision Repository


I will try different openCV functions used for Image processing.

*1. making_Mask.py:* 
- By adjusting Hue and Saturation level of the Image, we can obatain masks of simple images. Download the file, change the input image path in line 42 and run!
- Functions used: 
    1. cv2.createTrackbar
    2. cv2.getTrackbarPos
    3. cv2.inRange
    4. cv2.bitwise_and
    5. np.hstack
    6. cv2.resize
    7. cv2.cvtColor
    8. cv2.namedWindow
    9. cv2.resizeWindow

*2. small_object_detection.py:*
- By finding and drawing contours in the Image, we can obtain the position of the object. Download the file, change the input image path in line 4 and run!
- Functions used: 
    1. cv2.findContours
    2. cv2.contourArea
    3. cv2.drawContours
    4. cv2.cv2.arcLength
    5. cv2.Canny
    6. cv2.approxPolyDP
    7. cv2.GaussianBlur
    8. cv2.dilate
    9. cv2.erode
    10. cv2.cvtColor
    
*3. mask_and_detection.py:*
- By adjusting Hue and Saturation level of the Image, we can make the desired contours more prominent. Now you can make the mask of desired object in the image. Download the file, change the input image path in line 60 and run!
- Functions used: 
    1. cv2.createTrackbar
    2. cv2.getTrackbarPos
    3. cv2.inRange
    4. cv2.bitwise_and
    5. np.hstack
    6. cv2.resize
    7. cv2.cvtColor
    8. cv2.namedWindow
    9. cv2.resizeWindow
    10. cv2.findContours
    11. cv2.erode
    12. cv2.contourArea
    13. cv2.drawContours
    14. cv2.cv2.arcLength
    15. cv2.Canny
    16. cv2.approxPolyDP
    17. cv2.GaussianBlur
    18. cv2.dilate
    
