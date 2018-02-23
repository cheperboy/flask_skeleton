import os
from flask import Flask, url_for, redirect, render_template, request, abort
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
from flask_security.utils import encrypt_password
import flask_admin
from flask_admin.contrib import sqla
from flask_admin import helpers as admin_helpers
from flask_admin.base import MenuLink
from flask_bootstrap import Bootstrap

from .views.nav import nav_blueprint
from .views.mymodule import mymodule_blueprint

from .models import db, security
from .models.user import User, Role

from .admin.customviews import MyModelView

# Create Flask application
app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
Bootstrap(app)
app.debug = True
# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
#toolbar = DebugToolbarExtension(app)

app.register_blueprint(nav_blueprint)
app.register_blueprint(mymodule_blueprint)


# Create admin
admin = flask_admin.Admin(
    app,
    'MyAdminApp',
    base_template='admin-base.html',
    template_mode='bootstrap3',
)

# Add model views
admin.add_view(MyModelView(Role, db.session))
admin.add_view(MyModelView(User, db.session))
admin.add_link(MenuLink(name='Back to public', url='/'))

# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )


