class ReplyNode:
    def __init__(self, buttons, text, node_id, action=None):
        self.buttons = buttons
        self.text = text
        self.node_id = node_id
        self.action = action
