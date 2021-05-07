class Item:

    tags = []
    cost = -1

    def __init__(self, name: str, emoji_id: int):
        self.name = name
        self.icon = emoji_id
