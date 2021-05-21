import cv2


def filters(frame):
    edges = cv2.Canny(frame, 100, 300)
    return edges
