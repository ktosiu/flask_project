"""
Optional module for all things localization
"""

import constants
from flask_utils import *
from flask import current_app
from services.translator import Translator, trls

from db import db

blueprint = Blueprint('localization', __name__)


###
#Code for retrieving actual translations from database goes here
#As it currently stand translations are stored in translations collection in format:
#{'*TRANSLATION_KEY*':{'en':'*TRANSLATION_lt*', 'lt':'*TRANSLATION_lt*'}
#'DEFAULT' and 'LANGS' keys are reserved
#Default specifies default language to fall back to
#Langs sepcifies all languages that should be available to the end user
trls = {}
for trl in db.translations.find({}):
    trls.update(trl)
###


@blueprint.before_app_request
def before_request():

        try:
            lang = session['lang']
            translator = Translator(lang, trls, trls['DEFAULT'])
        except KeyError:
            translator = Translator(constants.default_language, trls)
        g.translator = translator

@blueprint.app_context_processor
def add_translator():

    return {'_':g.translator, 'languages':trls['LANGS']}




@blueprint.route('/lang/<lang>')
def set_lang(lang):
    """
    Endpoint responsible for setting language option in cookie.
    After setting the cookie redirects to url supplied in parameters.
    """
    args = request.args
    redirect_url = args.get('url')
    session['lang'] = lang

    if redirect_url: return redirect(redirect_url)
    else: return redirect('/')