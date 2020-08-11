import cv2
import numpy as np
frameWidth = 340
frameHeight = 140
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
def empty(a):
    pass

def getContours(img):
    orgImage = img.copy()
    kernel = np.ones((5, 5), np.uint8)
    imgGray = cv2.cvtColor(orgImage, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
    imgCanny = cv2.Canny(imgBlur, 100, 200)
    imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
    imgErode = cv2.erode(imgDialation, kernel, iterations=1)
    cv2.imshow("Object Highlighted", imgErode)
    object = np.array([])
    contours, hierarchy = cv2.findContours(imgErode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        print("area", area)
        if area > 0:
            cv2.drawContours(imgErode, contour, -1, (255, 0, 0), 7)
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            if len(approx) > 3:
                object = approx
    cv2.drawContours(orgImage, object, -1, (255, 0, 0), 20)
    cv2.imshow("Object Highlighted", orgImage)
    return object

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",85,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",9,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    imgHSV = cv2.cvtColor(imgResult, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(imgResult, imgResult, mask=mask)
    cv2.imshow("Camera", imgResult)
    #Click key 'a' to find the object
    if cv2.waitKey(1) & 0xFF == ord('a'):
        print(h_min, h_max, s_min, s_max, v_min, v_max)
        getContours(imgResult)
    # Click key 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


