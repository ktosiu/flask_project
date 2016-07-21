#Basic imports
from flask_utils import *
from db import *

#Common imports
import utils

#View specific imports


blueprint = Blueprint('admin', __name__, url_prefix='/admin')

