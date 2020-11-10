import os
import numpy as np
import tensorflow as tf
import random
IGNORE_LABEL = 255
IMG_MEAN = np.array((125.0, 114.4, 107.9), dtype=np.float32)

def read_labeled_image_list(data_dir):
    f = os.listdir(data_dir)
    images = []
    for line in f:
        image = line.strip('\n')
        images.append(data_dir + image)
    return images

def read_images_from_disk(input_queue, input_size, random_scale, random_mirror=False): # optional pre-processing arguments
    img_contents = tf.read_file(input_queue[0])
    img = tf.image.decode_jpeg(img_contents, channels=3)
    img_r, img_g, img_b = tf.split(value=img, num_or_size_splits=3, axis=2)
    img = tf.cast(tf.concat([img_b, img_g, img_r], 2), dtype=tf.float32)
    img -= IMG_MEAN
    return img

class ImageReader(object):
    def __init__(self, data_dir, input_size, random_scale, random_mirror, shuffle, coord):
        self.data_dir = data_dir
        self.input_size = input_size
        self.coord = coord
        self.image_list = read_labeled_image_list(self.data_dir)
        self.images = tf.convert_to_tensor(self.image_list, dtype=tf.string)
        self.queue = tf.train.slice_input_producer([self.images], shuffle=shuffle) 
        self.image = read_images_from_disk(self.queue, self.input_size, random_scale, random_mirror) 

    def dequeue(self, num_elements):
        batch_list = [self.image]
        image_batch = tf.train.batch([self.image], num_elements)
        return image_batch
