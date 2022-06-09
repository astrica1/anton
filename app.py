from modules.process import CommandProcessor
from modules.recognizer import Recognizer
    
def main():
    r = Recognizer()
    status = r.start()
    while status:
        command = r.listen()
        if command is not None:
            CommandProcessor(command)
    
if __name__ == "__main__":
    main()