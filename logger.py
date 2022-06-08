from datetime import datetime

class Logger:
    def __init__(self):
        self.color = 'white'
        self.prefix = ''
    
    def colorize(self, text, color='white'):
        if color == 'red':
            return '\033[91m' + text + '\033[0m'
        elif color == 'green':
            return '\033[92m' + text + '\033[0m'
        elif color == 'yellow':
            return '\033[93m' + text + '\033[0m'
        elif color == 'blue':
            return '\033[94m' + text + '\033[0m'
        elif color == 'magenta':
            return '\033[95m' + text + '\033[0m'
        elif color == 'cyan':
            return '\033[96m' + text + '\033[0m'
        elif color == 'white':
            return '\033[97m' + text + '\033[0m'
        elif color == 'grey':
            return '\033[90m' + text + '\033[0m'
        elif color == 'black':
            return '\033[90m' + text + '\033[0m'
        else:
            return text
    
    def write2file(self, text, prefix):
        if prefix:
            text = prefix + ': ' + text
        text = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '\t' + text + '\n'
        with open('.log', 'a') as f:
            f.write(text)
    
    def log(self, text, color=None, prefix=None, indent=None):
        self.write2file(text, prefix)
        if color:
            text = self.colorize(text, color)
        if prefix:
            text = prefix + ':\t' + text
        if indent:
            for _ in range(indent):
                text = ' ' + text
        print(text)