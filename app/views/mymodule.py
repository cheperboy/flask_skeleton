from flask import Blueprint, render_template

mymodule_blueprint = Blueprint('mymodule', __name__)

@mymodule_blueprint.route('/mymodule/index')
def mymodule():
    return render_template('mymodule/mymodule.html')
