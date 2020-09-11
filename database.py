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

    def get_from_db(self, query, *param):
        cursor = self.cursor()
        cursor.execute(query, param)
        res = cursor.fetchone()
        if res is None:
            return 0
        return res[0]

    def get_status(self, user):
        query = "SELECT node_id from users where user_id=%s"
        self.status = self.get_from_db(query, user)
        return self.status

    def get_next_node(self, text, status, role):
        query = "SELECT next_node from buttons where text=%s AND id=%s and (role=%s or role = 'USER')"
        self.next_node = self.get_from_db(query, text, status, role)
        return self.next_node

    def get_reply_buttons(self, next_node_id, role):
        cursor = self.cursor()
        query = "SELECT text from buttons where id=%s and (role=%s or role='USER')"
        cursor.execute(query, (next_node_id, role))
        return cursor.fetchall()

    def get_reply_text(self, next_node_id):
        query = "SELECT text from node_text where id=%s"
        return self.get_from_db(query, next_node_id)

    def update_db(self, query, *params):
        cursor = self.cursor()
        cursor.execute(query, params)
        self.connection.commit()

    def change_status(self, user_id, next_node_id):
        query = "UPDATE users SET node_id=%s WHERE user_id=%s"
        self.update_db(query, next_node_id, user_id)

    def add_user(self, user_id, username):
        query = "INSERT INTO users VALUES(%s, 'MENU', %s, 'USER')"
        self.update_db(query, user_id, username)

    def check(self, user_id):
        cursor = self.cursor()
        query = "SELECT user_id from users WHERE user_id=%s"
        cursor.execute(query, (user_id,))
        return cursor.fetchall()

    def action(self, next_node_id):
        query = "SELECT action from node_text WHERE id=%s"
        return self.get_from_db(query, next_node_id)

    def cursor(self):
        return self.connection.cursor()

    def check_inline_reply(self, node_id):
        query = "SELECT inline from node_text WHERE id=%s"
        return self.get_from_db(query, node_id)

    def get_from_db_action(self, query, *params):
        cursor = self.cursor()
        cursor.execute(query, params)
        res_set = cursor.fetchall()
        res = []
        for row in res_set:
            res.append(row)
        return res

    def get_tm_schedule(self, weekday, parity):
        query = "SELECT time, subject, type from schedule WHERE weekday=%s " \
                "and (parity=%s or parity=2)"
        return self.get_from_db_action(query, weekday, parity)

    def get_queue(self):
        query = "SELECT name, last_name from queue"
        return self.get_from_db_action(query)

    def add_to_queue(self, name, last_name):
        query = "INSERT into queue VALUES(%s, %s)"
        self.update_db(query, name, last_name)

    def check_queue(self, name, last_name):
        query = "SELECT last_name from queue WHERE last_name=%s and name=%s"
        return self.get_from_db(query, last_name, name)

    def delete_from_queue(self, name, last_name):
        query = "DELETE FROM queue WHERE name=%s and last_name=%s"
        return self.update_db(query, name, last_name)

    def get_role(self, user_id):
        query = "SELECT role from users where user_id=%s"
        return self.get_from_db(query, user_id)

    def delete_all_from_queue(self):
        query = "DELETE FROM queue"
        return self.update_db(query)
