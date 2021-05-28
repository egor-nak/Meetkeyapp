from .coloroverlay import *


def filters(frame, intensity=0.5):
    blue = 20
    green = 66
    red = 112
    frame = filters(frame,
                                intensity=intensity,
                                blue=blue, green=green, red=red)
    return frame
