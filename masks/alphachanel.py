import cv2

def verify_alpha_channel(frame):
    try:
        frame.shape[3]  # 4th position
    except IndexError:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    return frame