import os
import argparse
import pyvirtualcam
from pyvirtualcam import PixelFormat
import cv2
import numpy as np
from masks import vintage, invert, sepia, edgemode, picturestyle, blur, cirlur_blur, coloroverlay, portraitmod, \
    alphachanel, alphablend, grey, blackandwhite, cartoon, pencil
import imageio

while True:
    with open('/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/canstart.txt', 'r') as file:
        text = file.read()
    if text == 'Yes':
        break
print('Start')


class CFEVideoConf(object):
    # Standard Video Dimensions Sizes
    STD_DIMENSIONS = {
        "360p": (480, 360),
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }
    # Video Encoding, might require additional installs
    # Types of Codes: http://www.fourcc.org/codecs.php
    VIDEO_TYPE = {
        'avi': cv2.VideoWriter_fourcc(*'XVID'),
        # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
        'mp4': cv2.VideoWriter_fourcc(*'XVID'),
    }

    width = 640
    height = 480
    dims = (640, 480)
    capture = None
    video_type = None

    def __init__(self, capture, filepath, res="480p", *args, **kwargs):
        self.capture = capture
        self.filepath = filepath
        self.width, self.height = self.get_dims(res=res)
        self.video_type = self.get_video_type()

    # Set resolution for the video capture
    # Function adapted from https://kirr.co/0l6qmh
    def change_res(self, width, height):
        self.capture.set(3, width)
        self.capture.set(4, height)

    def get_dims(self, res='480p'):
        width, height = self.STD_DIMENSIONS['480p']
        if res in self.STD_DIMENSIONS:
            width, height = self.STD_DIMENSIONS[res]
        self.change_res(width, height)
        self.dims = (width, height)
        return width, height

    def get_video_type(self):
        filename, ext = os.path.splitext(self.filepath)
        if ext in self.VIDEO_TYPE:
            return self.VIDEO_TYPE[ext]
        return self.VIDEO_TYPE['avi']


while True:
    with open('/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/path.txt', 'r') as file:
        text = file.read()
    if text == 'Nothing2' or text == 'Nothing':
        isreal = True
    else:
        isreal = False
    if isreal:
        video = cv2.VideoCapture(0)
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = video.get(cv2.CAP_PROP_FPS)
        name = "BGR"
        count = 0
        lastframe = ''
        changevideo = False
        while True:
            if changevideo:
                break
            with pyvirtualcam.Camera(width, height, fps, fmt=eval(f"PixelFormat.{name}"), print_fps=fps) as cam:
                print(f'Virtual cam started: {cam.device} ({cam.width}x{cam.height} @ {cam.fps}fps)')
                while True:
                    with open('/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/path.txt',
                              'r') as file:
                        text = file.read()
                    if text != 'Nothing2' and text != 'Nothing':
                        changevideo = True
                        # print('break1')
                        break
                    # Restart
                    ret, frame = video.read()
                    if not ret:
                        raise RuntimeError('Error fetching frame')
                    try:
                        f = open("/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/main/filtername.txt",
                                 "r").read()
                        frame = eval(f + ".filters(frame)")
                    except Exception as ex:
                        pass
                    try:
                        cam.send(frame)
                    except Exception:
                        if name == "GRAY":
                            name = "BGR"
                        else:
                            name = "GRAY"
                        count += 1
                        break
                    cam.sleep_until_next_frame()
    else:
        with open('/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/path.txt', 'r') as file:
            text = file.read()
        initialpath = text
        video = cv2.VideoCapture(text)
        length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = video.get(cv2.CAP_PROP_FPS)
        config = CFEVideoConf(video, filepath='saved-media/filter.mp4', res='480p')

        name = "BGR"
        count = 0
        changevideo = False
        while True:
            if changevideo:
                break
            with pyvirtualcam.Camera(width, height, fps, fmt=eval(f"PixelFormat.{name}"), print_fps=fps) as cam:
                print(f'Virtual cam started: {cam.device} ({cam.width}x{cam.height} @ {cam.fps}fps)')
                while True:
                    with open('/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/path.txt',
                              'r') as file:
                        text = file.read()
                    if text != initialpath or text == 'Nothing2' or text == 'Nothing':
                        changevideo = True
                        # print("break2")
                        break
                    # Restart video on last frame.
                    if count == length:
                        count = 0
                        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    ret, frame = video.read()
                    if not ret:
                        raise RuntimeError('Error fetching frame')
                    try:
                        f = open("/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/main/filtername.txt",
                                 "r").read()
                        # print(f)
                        frame = eval(f + ".filters(frame)")
                    except Exception as ex:
                        pass
                    try:
                        cam.send(frame)
                    except Exception:
                        if name == "GRAY":
                            name = "BGR"
                        else:
                            name = "GRAY"
                        count += 1
                        break
                    cam.sleep_until_next_frame()
                    count += 1
