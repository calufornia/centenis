import utils
from compare import classify

class ImgStats:
    def __init__(self, img_path, settings):
        self.count = 0
        self.prev_words = []
        self.img_path = img_path
        self.words = classify(self.img_path, settings.watson_api_key)

    def inc_count(self, num):
        self.count += num


class AppStats:
    def __init__(self, img_dir):
        self.images = utils.shuffle_images(img_dir)
        self.num_images = len(self.images)
        self.curr_image = 0

    def inc_image(self):
        self.curr_image += 1
        if self.curr_image == self.num_images:
            self.curr_image = 0

    def get_image_path(self):
        return self.images[self.curr_image]

class Settings:
    def __init__(self, watson_api_key, bighugelabs_api_key):
        self.watson_api_key = watson_api_key
        self.bighugelabs_api_key = bighugelabs_api_key