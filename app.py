from flask import Flask, render_template, abort
from flask_assets import Environment

from assets import bundles
from experiments import read_all_experiments, read_featured_experiments, read_experiment

app = Flask(__name__)
app.config['SECRET_KEY'] = '7b7e30111ddc1f8a5b1d80934d336798'

assets = Environment(app)
assets.register(bundles)

@app.route('/')
def index():
    files = ['fire_egg.md', 'ping_pong_ball.md', 'water_filter.md', 'slime.md', 'oobleck.md'] #Five at a time
    featured = read_featured_experiments(files)
    return render_template('index.html', data=None, featured=featured)

@app.route('/mission')
def mission():
    return render_template('mission.html', data=None)

@app.route('/experiments')
def experiments():
    exp = read_all_experiments()
    print(exp)
    return render_template('experiments.html', data=None, experiments=exp)

@app.route('/experiments/<path:path>')
def experiment_detail(path):
    try:
        title, description, content = read_experiment(path+'.md')
        return render_template('experiment_detail.html', data=None, title=title, description=description, content=content)
    except FileNotFoundError:
        # Redirect to 404 page
        abort(404)

@app.route('/about')
def about():
    return render_template('about.html', data=None)

# 404 Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', data=None), 404

if __name__ == '__main__':
    app.run(debug=True)
