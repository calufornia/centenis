import os, random
import utils
from flask import *
from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import StringField


img_dir = './static/images/'
count = 1
app = Flask(__name__)
app.secret_key = 'monkey'


class APIRequestForm(Form):
    SECRET_KEY = "mankey"
    input = StringField('input', validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = APIRequestForm()
    kwargs = {'input': form.input._value()}
    print(kwargs['input'])

    img_path = list(map(lambda path: img_dir + path, os.listdir(img_dir)))
    prev_img = request.cookies.get('prev_img')
    img = prev_img

    if request.method == 'GET':
        while img == prev_img:
            img = random.sample(img_path, 1)[0]

        resp = make_response(render_template('image.html', img=img, form=form))
        resp.set_cookie('prev_img', img)
        return resp
    else:
        return render_template('image.html', img=img, form=form)


if __name__ == '__main__':
    app.run(debug=True)
