import speech_recognition as sr
from logger import Logger
from general import clear_console
from playsound import playsound


class Recognizer:
    def __init__(self):
        self.required = -1
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            if 'pulse' in name.lower():
                self.required = index
                break
        self.language = 'en-US'
        self.listener = sr.Recognizer()
        self.logger = Logger()

    def language_selector(self, language):
        if language == 'ar':
            self.language = 'ar-SA'
        elif language == 'ch':
            self.language = 'zh-CN'
        elif language == 'de':
            self.language = 'de-DE'
        elif language == 'fa':
            self.language = 'fa-IR'
        elif language == 'fr':
            self.language = 'fr-FR'
        elif language == 'it':
            self.language = 'it-IT'
        elif language == 'ru':
            self.language = 'ru-RU'
        elif language == 'sp':
            self.language = 'es-ES'
        else:
            self.language = 'en-US'

    def start(self, _lang=None):
        if _lang:
            self.language_selector(_lang)
        try:
            with sr.Microphone(device_index=self.required) as source:
                clear_console()
                logger.log('anton-speech-recognition-is-starting',
                           color='white', indent=2, _lang=self.language)
                self.listener.adjust_for_ambient_noise(source, duration=0.5)
                while True:
                    voice = self.listener.listen(source)
                    try:
                        command = self.listener.recognize_google(
                            voice, language=self.language).lower()
                        logger.log(command, color='green',
                                   prefix='You', _lang=self.language)
                        if 'hey' in command or 'anton' in command:
                            playsound('src/beep.wav')
                            self.logger.log(
                                'listening', color='yellow', indent=2, _lang=self.language)
                            return True
                    except Exception as e:
                        logger.log('an-error-has-occurred',
                                   color='red', indent=2, _lang=self.language)
                        logger.log(str(e), color='red', indent=4)
        except Exception:
            return False

    def listen(self, _lang=None):
        if _lang:
            self.language_selector(_lang)
        try:
            with sr.Microphone(device_index=self.required) as source:
                self.listener.adjust_for_ambient_noise(source, duration=0.5)
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(
                    voice, language=self.language).lower()
                self.logger.log(command, color='green',
                                prefix='You', _lang=self.language)
                return command
        except KeyboardInterrupt:
            self.logger.log('keyboard-interrupt', color='red',
                            indent=2, _lang=self.language)
            exit(0)
        except sr.UnknownValueError:
            self.logger.log('i-cant-understand-you', color='red',
                            prefix='Anton', _lang=self.language)
        except Exception:
            return None
