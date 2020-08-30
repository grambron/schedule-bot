import mysql.connector
import configurer


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DataBase(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=configurer.config['DB']["host"],
            user=configurer.config['DB']["user"],
            passwd=configurer.config['DB']["password"],
            database=configurer.config['DB']["database"]
        )
        self.nodes = {}
        self.status = ""
        self.next_node = ""

    def get_nodes(self):
        self.connection.cursor().execute("SELECT * from node_text")
        rows = self.connection.cursor().fetchall()
        for row in rows:
            self.nodes[row[1]] = row[0]
        return self.nodes

    def get_status(self, user):
        cursor = self.cursor()
        query = "SELECT node_id from users where user_id=%s"
        cursor.execute(query, (user,))
        self.status = cursor.fetchall()
        return self.status[0][0]

    def get_next_node(self, text, status):
        cursor = self.cursor()
        query = "SELECT next_node from buttons where text=%s AND id=%s"
        cursor.execute(query, (text, status))
        self.next_node = cursor.fetchall()
        return self.next_node[0][0]

    def get_reply_buttons(self, next_node_id):
        cursor = self.cursor()
        query = "SELECT text from buttons where id=%s"
        cursor.execute(query, (next_node_id,))
        return cursor.fetchall()

    def get_reply_text(self, next_node_id):
        cursor = self.cursor()
        query = "SELECT text from node_text where id=%s"
        cursor.execute(query, (next_node_id,))
        return cursor.fetchall()[0][0]

    def change_status(self, user_id, next_node_id):
        cursor = self.cursor()
        query = "UPDATE users SET node_id=%s WHERE user_id=%s"
        cursor.execute(query, (next_node_id, user_id))
        self.connection.commit()

    def add_user(self, user_id, username):
        cursor = self.cursor()
        query = "INSERT INTO users VALUES(%s, 'MENU', %s)"
        cursor.execute(query, (user_id, username))
        self.connection.commit()

    def check(self, user_id):
        cursor = self.cursor()
        query = "SELECT user_id from users WHERE user_id=%s"
        cursor.execute(query, (user_id,))
        return cursor.fetchall()

    # def check_buttons(self, next_node_id):
    #     cursor = self.cursor()
    #     query = "SELECT id from node_text WHERE id=%s"
    #     cursor.execute(query, (next_node_id,))
    #     return cursor.fetchall()

    def cursor(self):
        return self.connection.cursor()
