import cv2


def filters(frame):
    cartoon_image = cv2.stylization(frame, sigma_s=150, sigma_r=0.25)
    return cartoon_image
