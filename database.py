import mysql.connector
import configurer


class DataBase(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataBase, cls).__new__(cls)
            cls.instance = mysql.connector.connect(
                host=configurer.config['DB']["host"],
                user=configurer.config['DB']["user"],
                passwd=configurer.config['DB']["password"],
                database=configurer.config['DB']["database"]
            )
        return cls.instance


db = DataBase()
cursor = db.cursor()