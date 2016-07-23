#Basic imports
from flask_utils import *
from db import *

#Common imports
import utils

#View specific imports
import re

blueprint = Blueprint('services', __name__)



@blueprint.route('/a')
def autocomplete():
    """
    barebone autocomplete for mongo, probably should not be used on a large scale because of how taxing regex is
    """
    query = request.args.get('q')
    rgx = re.compile(r'\b'+ re.escape(query), re.IGNORECASE)
    autocomplete_results = db.find({'$or':[
        {'title':{"$regex":rgx}},
    ]}).limit(10)

    autocomplete_results = [(r['title'], r['url_slug']) for r in autocomplete_results]

    return jsonify(autocomplete_results=autocomplete_results)


@blueprint.route('/lang')
def set_lang():
    """
    Endpoint responsible for setting language option in cookie.
    After setting the cookie redirects to url supplied in parameters.
    """
    args = request.args
    lang = args.get('lang')
    redirect_url = args.get('url')

    session['lang'] = lang
    return redirect(redirect_url)

