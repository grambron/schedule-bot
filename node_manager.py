from reply_node import ReplyNode


class NodeManager:

    def get_node(self, status):
        rn = ReplyNode(["Привет", "мир"],
                       "Приветствуем в 34, остальным соболзнует")
        return rn
