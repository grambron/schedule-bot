import database
import datetime
from reply_node import ReplyNode


class TmSchedule:
    def __init__(self):
        self.db = database.DataBase()

    def action(self, lock, status, message, role):
        weekday = datetime.datetime.today().weekday() + 2
        parity = (datetime.datetime.today().isocalendar()[1] + 1) % 2
        schedule = self.db.get_tm_schedule(weekday, parity)
        text = ""
        for item in schedule:
            text += " ".join(item) + "\n"
        return ReplyNode(self.db.get_reply_buttons(status, role), text, status, "TmSchedule")