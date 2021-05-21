# This script plays back a video file on the virtual camera.
# It also shows how to:
# - select a specific camera device
# - use BGR as pixel format
import os
import argparse
import pyvirtualcam
from pyvirtualcam import PixelFormat
import cv2
import numpy as np
from masks import vintage, invert, sepia, edgemode, picturestyle, blur, cirlur_blur, coloroverlay, portraitmod, \
    alphachanel, alphablend, grey, blackandwhite, cartoon, pencil
import imageio




with open('/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/path.txt', 'r') as file:
    text = file.read()
if text == 'Nothing2' or text == 'Nothing':
    video = cv2.VideoCapture(0)
else:
    video = cv2.VideoCapture(text)
if not video.isOpened():
    raise ValueError("error opening video")
# length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)
name = "BGR"
count = 0
lastframe = ''
print(width, height)
while True:
    with pyvirtualcam.Camera(width, height, fps, fmt=eval(f"PixelFormat.{name}"), print_fps=fps) as cam:
        print(f'Virtual cam started: {cam.device} ({cam.width}x{cam.height} @ {cam.fps}fps)')
        while True:
            ret, frame = video.read()
            cam.send(frame)
            cam.sleep_until_next_frame()
