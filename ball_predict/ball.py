import cv2
import cvzone 
from cvzone.ColorModule import ColorFinder
import numpy as np
import math

# initialize the Video 
cap = cv2.VideoCapture('Videos/vid (7).mp4')

# creating the color finder
# if we fill the ColorFInder() with True, we will using debug mode to find the color
myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 0, 'smin': 115, 'vmin': 0, 'hmax': 15, 'smax': 255, 'vmax': 255}

# Variables
posListX = []
posListY = []
xList = [item for item in range(0,1300)]
prediction = False


while True:
# Grabbing the image
    success, img = cap.read()
    # we will do color selection for the ball

    # img = cv2.imread("Ball.png")
    # i'm cropping the image but only the heigh not the width
    img = img[0:900, :]

    imgColor, mask = myColorFinder.update(img, hsvVals)

    # finding ball location
    imgContours, contours = cvzone.findContours(img, mask, minArea=200)

    # putting a circle each frame of location
    # the biggest value will be the first
    if contours:
        posListX.append(contours[0]['center'][0])
        posListY.append(contours[0]['center'][1])

    if posListX :   
    # Polynomial Regression y = Ax^2 + Bx + C
    # find the Coefficients
        A, B, C = np.polyfit(posListX, posListY, 2)


        # print(cx, cy)
        for i, (posX, posY) in enumerate(zip(posListX, posListY)):
            pos = (posX, posY)
            cv2.circle(imgContours, pos, 10, (0, 255, 0), cv2.FILLED)
            if i == 0 :
                cv2.line(imgContours, pos, pos,(0, 255, 0), 2)
            else:
                cv2.line(imgContours, pos, (posListX[i-1], posListY[i-1]),(0, 255, 0), 2)
        for x in xList:
            y = int(A * x ** 2 + B * x + C)
            cv2.circle(imgContours, (x, y), 1, (255, 0, 200), cv2.FILLED)

        if len(posListX)<10:

    # Prediction
    #  X values 330 to 430 , Y 590 ( i found it with Paint)
        
            a = A
            b = B
            c = C - 590

            x = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
            prediction = 330 < x < 430

        if prediction:
            cvzone.putTextRect(imgContours, "Ball in", (50, 150), scale=5, thickness=5, colorR=(0, 200, 0), offset=20)
        else:
            cvzone.putTextRect(imgContours, "Zonk!", (50, 150), scale=5, thickness=5, colorR=(0, 0, 200), offset=20)


# Display
    # resizing the image
    imgContours = cv2.resize(imgContours, (0,0), None, 0.7, 0.7)
    # cv2.imshow("Image", img)
    cv2.imshow("ImageColor", imgContours)
    cv2.waitKey(80)