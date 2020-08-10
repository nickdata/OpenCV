import cv2
import numpy as np

image = cv2.imread('Pyraminx.jpeg')
image_rotate = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
image_flip = cv2.flip(image_rotate, 1)
def getContours(img):
    orgImage = img.copy()
    obj = np.array([])
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        print("area",area)
        if area>5000:
            cv2.drawContours(imgErode, contour, -1, (255, 0, 0), 7)
            peri = cv2.arcLength(contour,True)
            approx = cv2.approxPolyDP(contour,0.02*peri,True)
            if len(approx) > 3:
                obj = approx
    cv2.drawContours(orgImage, obj, -1, (255, 0, 0), 20)
    cv2.imshow("Object Highlighted", orgImage)
    return obj

kernel=np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDialation = cv2.dilate(imgCanny, kernel,iterations=1)
imgErode = cv2.erode(imgDialation,kernel,iterations=1)

obj = getContours(imgErode)
print("Object Coordinates", obj)
cv2.waitKey(0)