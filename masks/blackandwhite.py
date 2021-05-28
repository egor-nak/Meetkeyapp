import cv2


def filters(frame):
    originalImage = frame
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    return blackAndWhiteImage

