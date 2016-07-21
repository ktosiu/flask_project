from flask_utils import *
import filters
import warnings

import admin.views
import meta.views
import public.views
import services.views



app = Flask(__name__)
app.debug = True
app.secret_key = b"\x92\xde'ES\xb7]\\\x82[\xd2\xfb\xd4\x93\x8a\x08/b\x85\xfe}K\x8f\xa5"

if app.secret_key == b"\x92\xde'ES\xb7]\\\x82[\xd2\xfb\xd4\x93\x8a\x08/b\x85\xfe}K\x8f\xa5": print('!'*5, 'USING DEFAULT SECRET KEY, CHANGE TO SOMETHING UNIQUE', '!'*5)

#Setting up the app environment#
#Importing all filters from filters.py
app.jinja_env.filters.update(filters.filters)

app.register_blueprint(admin.views.blueprint)
app.register_blueprint(meta.views.blueprint)
app.register_blueprint(public.views.blueprint)
app.register_blueprint(services.views.blueprint)

if __name__ == '__main__':
    app.run()
