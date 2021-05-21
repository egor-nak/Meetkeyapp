import cv2


def filters(frame):
    originalImage = frame
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    return grayImage
