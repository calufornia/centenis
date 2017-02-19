from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3


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
    print(words)
    return words


def score(guess, prev_words, words):
    if guess in prev_words:
        return False
    elif guess in words:
        return True
    else:
        return False


def increment(guess, prev_words, img_path):
    return score(guess, prev_words, classify(img_path))
