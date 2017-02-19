import os, random
from compare import increment
from flask import *
from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import StringField


img_dir = './static/images/'
count = 0
prev_words = []
app = Flask(__name__)
app.secret_key = 'monkey'


class APIRequestForm(Form):
    SECRET_KEY = "mankey"
    input = StringField('input', validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def index():
    global count, prev_words
    form = APIRequestForm()
    img_path = list(map(lambda path: img_dir + path, os.listdir(img_dir)))
    prev_img = request.cookies.get('prev_img')
    img = prev_img

    if request.method == 'GET': # called when moving on to next image
        count = 0
        prev_words = []
        while img == prev_img:
            img = random.sample(img_path, 1)[0]

        resp = make_response(render_template('image.html', img=img, form=form, count=count))
        resp.set_cookie('prev_img', img)
        return resp
    else: # called when entering a guess
        kwargs = {'input': form.input._value()}
        guess = kwargs['input']
        if increment(guess, prev_words,img):
            count += 1
            prev_words += [guess]
        return render_template('image.html', img=img, form=form, count=count)


if __name__ == '__main__':
    app.run(debug=True)
