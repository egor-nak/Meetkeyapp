import cv2
from .alphachanel import *
import numpy as np
from .alphablend import *


def filters(frame, intensity=0.2):
    frame = verify_alpha_channel(frame)
    frame_h, frame_w, frame_c = frame.shape
    y = int(frame_h / 2)
    x = int(frame_w / 2)
    radius = int(x / 2)  # int(x/2)
    center = (x, y)
    mask = np.zeros((frame_h, frame_w, 4), dtype='uint8')
    cv2.circle(mask, center, radius, (255, 255, 255), -1, cv2.LINE_AA)
    mask = cv2.GaussianBlur(mask, (21, 21), 11)
    blured = cv2.GaussianBlur(frame, (21, 21), 11)
    blended = alpha_blend(frame, blured, 255 - mask)
    frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
    return frame
