import database
from reply_node import ReplyNode


class QueueManagerAdd:
    def __init__(self):
        self.db = database.DataBase()

    def action(self, lock, status, message, role):
        name = message.from_user.first_name
        last_name = message.from_user.last_name
        with lock:
            if not self.db.check_queue(name, last_name):
                self.db.add_to_queue(name, last_name)
        return ReplyNode(self.db.get_reply_buttons(status, role), "Готово", status, "Add_queue")
