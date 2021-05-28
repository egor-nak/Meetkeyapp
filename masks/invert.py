import cv2
from .alphachanel import *



def filters(frame):
    return cv2.bitwise_not(frame)
