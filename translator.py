class UndefinedTranslation(Exception): pass


trls = {
    'hey':{'en':'hello', 'lt':'labas'}
}

class Translator():
    def __init__(self, lang, translations, fallback=None):
        self.lang = lang
        self.translations = translations
        self.fallback = fallback

    @staticmethod
    def translate(phrase, lang, translations, fallback=None):
        """Tries to get translation for supplied key aka phrase, if that fails but fallback language is supplied
            it tries to return translation in it.
        """

        try:
            return translations[phrase][lang]
        except KeyError:
            if fallback:
                try: return translations[phrase][fallback]
                except KeyError: raise UndefinedTranslation("Translation for key '{}' does not exist in language '{}' or fallback '{}'".format(phrase, lang, fallback))
            else: raise UndefinedTranslation("Translation for key '{}' does not exist in language '{}'".format(phrase, lang, fallback))

    def __getitem__(self, item):
        return self.translate(item, self.lang, self.translations, self.fallback)


