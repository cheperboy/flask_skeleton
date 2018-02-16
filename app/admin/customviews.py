from flask import abort
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user

# Create customized model view class
class MyModelView(ModelView):

    # this function connects Flask-Admin to the roles of Flask-Security
    # Only allows superusers to view admin views.
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

