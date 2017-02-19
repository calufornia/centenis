import os, random
import utils
from flask import *
from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import StringField

img_dir = './static/images/'

app = Flask(__name__)
app.secret_key = 'monkey'

class APIRequestForm(Form):
    input = StringField('Input', validators=[DataRequired()])

@app.route('/')
def index():
    img_path = list(map(lambda path: img_dir + path, os.listdir(img_dir)))
    prev_img = request.cookies.get('prev_img')
    img = random.sample(img_path, 1)[0]
    while img == prev_img:
        img = random.sample(img_path, 1)[0]

    resp = make_response(render_template('image.html', img=img))
    resp.set_cookie('prev_img', img)
    return resp


if __name__ == '__main__':
    app.run()
