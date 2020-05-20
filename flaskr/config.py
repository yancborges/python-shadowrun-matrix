import configparser
import os

config = configparser.ConfigParser()
config.read(
    os.path.join(os.path.abspath(
        os.path.dirname(__file__)
    ), 'settings.ini')
)
url_mongo = config.get('main', 'url_mongo')
database_name = config.get('main', 'database_name')
debug = config.getboolean('main', 'debug')
