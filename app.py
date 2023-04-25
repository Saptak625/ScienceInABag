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

@app.route('/experiments')
def experiments():
    return render_template('experiments.html', data=None)

@app.route('/experiments/<path:path>')
def experiment_detail(path):
    return render_template('experiment_detail.html', data=None)

@app.route('/about')
def about():
    return render_template('about.html', data=None)

# 404 Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', data=None), 404

if __name__ == '__main__':
    app.run(debug=True)
