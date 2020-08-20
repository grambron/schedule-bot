from reply_node import ReplyNode


class NodeManager:
    def get_node(self, message):
        user_id = message.from_user.id
        rn = ReplyNode(["Привет", "мир"],
                       "Приветствуем в 34, остальным соболзнуем", 'Меню')
        return rn
