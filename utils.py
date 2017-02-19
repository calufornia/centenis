import os
from random import shuffle

def shuffle_images(img_path):
    images = list(map(lambda path: img_path + path, os.listdir(img_path)))
    shuffle(images)
    return images