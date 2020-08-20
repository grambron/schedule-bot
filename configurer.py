import configparser
import os.path

config = configparser.ConfigParser()
_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config.read(os.path.join(_ROOT_DIR, 'config.ini'))
