import tensorflow as tf
import tensorflow_hub as hub
from datetime import datetime
import cv2
import matplotlib.pyplot as plt
import numpy as np

def img_scaler(image, max_dim=512):
    # Casts a tensor to a new type.
    original_shape = tf.cast(tf.shape(image)[:-1], tf.float32)

    # Creates a scale constant for the image
    scale_ratio = max_dim / max(original_shape)

    # Casts a tensor to a new type.
    new_shape = tf.cast(original_shape * scale_ratio, tf.int32)

    # Resizes the image based on the scaling constant generated above
    return tf.image.resize(image, new_shape)


def load_img(path_to_img):
    # Reads and outputs the entire contents of the input filename.
    img = tf.io.read_file(path_to_img)
    # Detect whether an image is a BMP, GIF, JPEG, or PNG, and
    # performs the appropriate operation to convert the input
    # bytes string into a Tensor of type dtype
    img = tf.image.decode_image(img, channels=3)

    # Convert image to dtype, scaling (MinMax Normalization) its values if needed.
    img = tf.image.convert_image_dtype(img, tf.float32)

    # Scale the image using the custom function we created
    img = img_scaler(img)

    # Adds a fourth dimension to the Tensor because
    # the model requires a 4-dimensional Tensor
    return img[tf.newaxis, :]


def load_img2(img):
    # Reads and outputs the entire contents of the input filename.
    # img = tf.convert_to_tensor(img, dtype=tf.string)
    #
    # # Detect whether an image is a BMP, GIF, JPEG, or PNG, and
    # # performs the appropriate operation to convert the input
    # # bytes string into a Tensor of type dtype
    # img = tf.image.decode_image(img, channels=3)
    #
    # # Convert image to dtype, scaling (MinMax Normalization) its values if needed.
    # img = tf.image.convert_image_dtype(img, tf.float32)
    #
    # # Scale the image using the custom function we created
    img = img_scaler(img)

    # Adds a fourth dimension to the Tensor because
    # the model requires a 4-dimensional Tensor
    return img[tf.newaxis, :]


def filters(frame, hub_module, style_path):
    content_path = frame



    style_image = load_img(style_path)
    content_image = load_img2(content_path)


    stylized_image = hub_module(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = stylized_image.numpy()
    stylized_image = stylized_image.reshape(stylized_image.shape[1:])
    return cv2.cvtColor(stylized_image, cv2.COLOR_BGR2RGB)
