import pyttsx3
from logger import Logger


class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 125)
        self.engine.setProperty('volume', 1)
        self.engine.setProperty('voice', 'english')
        self.logger = Logger()
        self.language = 'en-US'

    def language_selector(self, language):
        if language == 'ar':
            self.engine.setProperty('voice', 'arabic')
            self.language = 'ar-SA'
        elif language == 'ch':
            self.engine.setProperty('voice', 'chinese')
            self.language = 'zh-CN'
        elif language == 'de':
            self.engine.setProperty('voice', 'german')
            self.language = 'de-DE'
        elif language == 'fa':
            self.engine.setProperty('voice', 'persian')
            self.language = 'fa-IR'
        elif language == 'fr':
            self.engine.setProperty('voice', 'french')
            self.language = 'fr-FR'
        elif language == 'it':
            self.engine.setProperty('voice', 'italian')
            self.language = 'it-IT'
        elif language == 'ru':
            self.engine.setProperty('voice', 'russian')
            self.language = 'ru-RU'
        elif language == 'sp':
            self.engine.setProperty('voice', 'spanish')
            self.language = 'es-ES'
        else:
            self.engine.setProperty('voice', 'english')
            self.language = 'en-US'

    def talk(self, message, _lang=None):
        if _lang:
            self.language_selector(_lang)

        self.logger.log(message, color='yellow',
                        prefix='Anton', _lang=self.language)
        try:
            self.engine.say(message)
            self.engine.runAndWait()

        except Exception as e:
            self.logger.log('an-error-has-occurred', color='red',
                            indent=2, _lang=self.language)
            self.logger.log(str(e), color='red', indent=2, _lang=self.language)
            exit(0)

    def stop(self):
        self.engine.stop()
        self.engine.close()
