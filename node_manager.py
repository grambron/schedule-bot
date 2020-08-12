from reply_node import ReplyNode
import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


class NodeManager:
    def connect(self):
        db = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            passwd=config["password"],
            database=config["database"]
        )
        cursor = db.cursor()

    def get_node(self, user_id):

        rn = ReplyNode(["Привет", "мир"],
                       "Приветствуем в 34, остальным соболзнуем", 'Меню')
        return rn
