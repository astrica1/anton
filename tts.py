import pyttsx3
from logger import Logger

class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 125)
        self.engine.setProperty('volume', 1)
        self.engine.setProperty('voice', 'english')
        self.logger = Logger()
    
    def language_selector(self, language):
        if language == 'ar':
            self.engine.setProperty('voice', 'arabic')
        elif language == 'ch':
            self.engine.setProperty('voice', 'chinese')
        elif language == 'de':
            self.engine.setProperty('voice', 'german')
        elif language == 'en':
            self.engine.setProperty('voice', 'english')
        elif language == 'fa':
            self.engine.setProperty('voice', 'persian')
        elif language == 'fr':
            self.engine.setProperty('voice', 'french')
        elif language == 'it':
            self.engine.setProperty('voice', 'italian')
        elif language == 'ru':
            self.engine.setProperty('voice', 'russian')
        elif language == 'sp':
            self.engine.setProperty('voice', 'spanish')
        else:
            self.engine.setProperty('voice', 'english')
    
    def talk(self, message, _lang=None):
        if _lang:
            self.language_selector(_lang)
            
        self.logger.log(message, color='yellow', prefix='Anton')
        try:
            self.engine.say(message)
            self.engine.runAndWait()
        except Exception as e:
            self.logger.log('\nError: ' + str(e), color='red', indent=2)
            exit(0)

    def stop(self):
        self.engine.stop()
        self.engine.close()