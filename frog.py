from ConfigParser import *
from stats import *
from compare import increment
from flask import *
from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import StringField

img_dir = './static/images/'


app_stats = AppStats(img_dir)
# img_stats = ImgStats()

app = Flask(__name__)
app.secret_key = 'monkey'


class APIRequestForm(Form):
    SECRET_KEY = "mankey"
    input = StringField('input', validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def index():
    global img_stats # needed so the else case doesn't complain about uninitialized variables

    form = APIRequestForm()

    if request.method == 'GET': # called when moving on to next image

        img_path = app_stats.get_image_path()
        img_stats = ImgStats(img_path, settings)
        app_stats.inc_image()
        count = img_stats.count
        resp = make_response(render_template('image.html', img_path=img_path, form=form, count=count))
        return resp
    else: # called when entering a guess
        kwargs = {'input': form.input._value()}
        guess = kwargs['input']
        img_path = img_stats.img_path
        img_stats.inc_count(increment(guess, img_stats.prev_words, img_stats.words, settings.bighugelabs_api_key))
        return render_template('image.html', img_path=img_path, form=form, count=img_stats.count)


if __name__ == '__main__':
    config = SafeConfigParser()
    config.read('settings.cfg')
    settings = Settings(config.get('watson', 'api_key'), config.get('bighugelabs', 'api_key'))
    app.run(debug=True)
