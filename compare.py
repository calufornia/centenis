from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3

img_path = './static/images/airplane_0008.jpg'


def classify(img_path):
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key='3f9715d01175fea2d469518dd06a59cad135d59c')
    with open(join(dirname(__file__), img_path), 'rb') as image_file:
        results = visual_recognition.classify(images_file=image_file)
    classes = results['images'][0]['classifiers'][0]['classes']
    classes.sort(key=lambda c: c['score'], reverse=True)
    classes = classes[:len(classes)/2]  # Only keeps the best half of classifications
    words = []
    for c in classes:
        words += [c['class']]
    return words


def score(input, prev_words, words):
    if input in prev_words:
        return False
    elif input in words:
        return True
    else:
        return False


print(classify(img_path))
