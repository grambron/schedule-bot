import database
from reply_node import ReplyNode


class QueueManagerShow:
    def __init__(self):
        self.db = database.DataBase()

    def action(self, lock, status, message, role):
        with lock:
            queue = self.db.get_queue()
        text = ""
        if not queue:
            text = "Очередь пока пуста"
        else:
            num = 1
            for item in queue:
                text += str(num) + ". " + item[0] + " " + item[1] + "\n"
                num += 1
        return ReplyNode(self.db.get_reply_buttons(status, role), text, status, "Show_queue")
