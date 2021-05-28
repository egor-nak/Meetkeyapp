import cv2
import numpy as np


def filters(frame):
    rows, cols = frame.shape[:2]
    # Create a Gaussian filter
    kernel_x = cv2.getGaussianKernel(cols, 200)
    kernel_y = cv2.getGaussianKernel(rows, 200)
    kernel = kernel_y * kernel_x.T
    filter = 255 * kernel / np.linalg.norm(kernel)
    vintage_im = np.copy(frame)
    # for each channel in the input image, we will apply the above filter
    for i in range(3):
        vintage_im[:, :, i] = vintage_im[:, :, i] * filter
    return vintage_im
