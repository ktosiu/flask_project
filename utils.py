"""
This is a place to put custom utilities and functions that help with web development
"""


from functools import wraps
from flask_utils import *

def need_login(*user_groups, min_user_group=False):
    def decorator(f):
        @wraps(f)
        def final_function(*args, **kwargs):
            access_level = session.get('user_group')
            if access_level in user_groups or (min_user_group != False and access_level >= min_user_group):
                return f(*args, **kwargs)
            else:
                flash("Your account does not have sufficient privileges to access this", 'danger')
                return render_template('/meta/login.html')

        return final_function

    return decorator