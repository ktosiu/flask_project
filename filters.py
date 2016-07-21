import string
from unidecode import unidecode
import sys
from inspect import getmembers, isfunction
current_module = sys.modules[__name__]


def slugify(text):
    text = unidecode(text)

    out = ''

    seperator_streak = False

    for char in text:
        if char in string.punctuation + string.whitespace:
            seperator_streak = True

        elif char in string.ascii_letters + string.digits:
            if seperator_streak == True:
                out += '-' + char
                seperator_streak = False

            elif seperator_streak == False:
                out += char
    return out

filters = {name: function for name, function in getmembers(current_module) if isfunction(function)}
