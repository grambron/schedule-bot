import database
import configurer


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
        self.invokers = configurer.config['ACTION']

    def check_action(self, next_node_id):
        action = self.db.action(next_node_id)
        if action != 'NONE':
            self.invokers[action].action()
