import database
from reply_node import ReplyNode


class QueueManagerClear:
    def __init__(self):
        self.db = database.DataBase()

    def action(self, lock, status, message, role):
        with lock:
            self.db.delete_all_from_queue()
        return ReplyNode(self.db.get_reply_buttons(status, role), "Готово", status, "Clear_queue")