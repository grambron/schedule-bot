from reply_node import ReplyNode
import database
from action_manager import ActionManager
import configurer


class NodeManager:
    def __init__(self):
        self.db = database.DataBase()
        self.action_manager = ActionManager()
        # self.nodes = self.db.get_nodes()

    def get_start_node(self):
        reply = ReplyNode(
            self.db.get_reply_buttons('MENU'),
            self.db.get_reply_text('MENU'),
            'MENU'
        )
        return reply

    def get_node_id(self, message):
        status = self.db.get_status(message.from_user.id)
        next_node_id = self.db.get_next_node(message.text, status)
        if self.action_manager.check_action(next_node_id):
            reply = ReplyNode(
                self.db.get_reply_buttons(next_node_id),
                self.db.get_reply_text(next_node_id),
                next_node_id)
            return reply
        else:
            reply = ReplyNode(
                self.db.get_reply_buttons(status),
                configurer.config['REPLY']['unfinished'],
                status
            )
            return reply

    def add_user(self, user_id, username):
        if not self.db.check(user_id):
            self.db.add_user(user_id, username)
        else:
            self.db.change_status(user_id, 'MENU')

    def check_inline_reply(self, node_id):
        return self.db.check_inline_reply(node_id)

    def change_status(self, message):
        status = self.db.get_status(message.from_user.id)
        next_node_id = self.db.get_next_node(message.text, status)
        self.db.change_status(message.from_user.id, next_node_id)