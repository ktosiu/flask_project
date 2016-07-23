from flask_utils import *

blueprint = Blueprint('localization', __name__)

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