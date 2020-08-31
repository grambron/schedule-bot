from reply_node import ReplyNode
import database
from action_manager import ActionManager


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
        user_id = message.from_user.id
        text = message.text
        status = self.db.get_status(user_id)
        try:
            next_node_id = self.db.get_next_node(text, status)
            self.action_manager.check_action(next_node_id)
            self.db.change_status(user_id, next_node_id)
            reply = ReplyNode(
                self.db.get_reply_buttons(next_node_id),
                self.db.get_reply_text(next_node_id),
                next_node_id)
            return reply
        except IndexError:
            reply = ReplyNode(
                self.db.get_reply_buttons(status),
                "Извини, этот раздел пока не готов",
                status
            )
            return reply

    def add_user(self, user_id, username):
        if not self.db.check(user_id):
            self.db.add_user(user_id, username)
        else:
            self.db.change_status(user_id, 'MENU')
