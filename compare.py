from thesaurus import get_synonyms
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3


def classify(img_path, api_key):
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key=api_key)
    with open(join(dirname(__file__), img_path), 'rb') as image_file:
        results = visual_recognition.classify(images_file=image_file)
    classes = results['images'][0]['classifiers'][0]['classes']
    classes.sort(key=lambda c: c['score'], reverse=True)
    # classes = classes[:len(classes)/2]  # Only keeps the best half of classifications
    words = []
    for c in classes:
        words.extend(c['class'].split(' '))
    print('CLASSIFICATIONS: ' + str(words))
    return words


def score(guess, prev_words, words, api_key):
    synonyms = get_synonyms(guess, api_key)
    print('SYNONYMS: ' + str(synonyms))
    num_matches = 0
    for synonym in synonyms:
        if synonym not in prev_words and synonym in words:
            prev_words += [synonym]
            num_matches += 1
    return num_matches


def increment(guess, prev_words, words, api_key):
    return score(guess, prev_words, words, api_key)