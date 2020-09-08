import threading

import database
from tm_schedule import TmSchedule
from show_queue import QueueManagerShow
from add_queue import QueueManagerAdd
from exit_queue import QueueManagerExit
from clear_queue import QueueManagerClear


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ActionManager(metaclass=SingletonMeta):
    def __init__(self):
        self.db = database.DataBase()

        self.invokers = {"TM_SCHEDULE": TmSchedule(), "SHOW_QUEUE": QueueManagerShow(),
                         "ADD_QUEUE": QueueManagerAdd(), "EXIT_QUEUE": QueueManagerExit(),
                         "CLEAR_QUEUE": QueueManagerClear()}

    def check_action(self, next_node_id):
        action = self.db.action(next_node_id)
        return action

    def get_node(self, action, status, message, role):
        lock = threading.Lock()
        return self.invokers[action].action(lock, status, message, role)
