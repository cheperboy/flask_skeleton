from flask import Blueprint, render_template
from flask_login import login_required

nav_blueprint = Blueprint('nav', __name__)


@nav_blueprint.route('/')
def home():
    return render_template('home.html')

@nav_blueprint.route('/public1')
def public1():
    return render_template('public1.html')

@nav_blueprint.route('/public2')
def public2():
    return render_template('public2.html')

@nav_blueprint.route('/private')
@login_required
def private():
    return render_template('private.html')
