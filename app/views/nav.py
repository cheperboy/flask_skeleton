from flask import Blueprint, render_template
from flask_login import login_required

nav_blueprint = Blueprint('nav', __name__)


@nav_blueprint.route('/')
def home():
    return render_template('home.html')


@nav_blueprint.route('/about')
@login_required
def about():
    return render_template('about.html')

@nav_blueprint.route('/test')
def index():
    return render_template('index.html')

