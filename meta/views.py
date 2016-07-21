#Basic imports
from flask_utils import *
from db import *

#Common imports
import utils

#View specific imports


blueprint = Blueprint('meta', __name__)

@blueprint.route('/login', methods=['POST', 'GET'])
def login():
    #Login information handling
    if request.method.lower() == 'post':
        username = request.form['username']
        password = request.form['password']

        user = db.users.find_one({'username':username})

        #If no user with such username was found
        if not user:
                flash('No such user found', 'danger')
                return render_template('/meta/login.html')

        #If supplied password matches the one stored in database
        if check_password_hash(user['password'], password):
            session['username'] = username
            session['user_group'] = user['user_group']
            return 'logged in'

        #If user exists but the username/password combination doesn't match
        else:
            flash('Incorrect password/user combination', 'danger')
            flash('Incorrect password/user combination', 'error')
            return render_template('/meta/login.html')

    #Simply display login form
    else:
        return render_template('/meta/login.html')
