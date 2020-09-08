from __future__ import with_statement

import database
from reply_node import ReplyNode


class QueueManagerExit:
    def __init__(self):
        self.db = database.DataBase()

    def action(self, lock, status, message, role):
        name = message.from_user.first_name
        last_name = message.from_user.last_name
        with lock:
            if self.db.check_queue(name, last_name):
                self.db.delete_from_queue(name, last_name)
        return ReplyNode(self.db.get_reply_buttons(status, role), "Готово", status, "Exit_queue")