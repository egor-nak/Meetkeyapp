import cv2

def filters(frame):
    frame = cv2.GaussianBlur(frame, (5, 5), cv2.BORDER_DEFAULT)
    return frame