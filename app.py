from flask import Flask, render_template, flash
from flask_assets import Environment

from assets import bundles

app = Flask(__name__)
app.config['SECRET_KEY'] = '7b7e30111ddc1f8a5b1d80934d336798'

assets = Environment(app)
assets.register(bundles)


@app.route('/')
def index():
    return render_template('index.html', data=None)

@app.route('/mission')
def mission():
    return render_template('mission.html', data=None)

@app.route('/about')
def about():
    return render_template('about.html', data=None)


if __name__ == '__main__':
    app.run(debug=True)
