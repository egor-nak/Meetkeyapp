import cv2


def filters(frame):
    cartoon_image1, cartoon_image2 = cv2.pencilSketch(frame, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
    return cartoon_image2
