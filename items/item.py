class Item:

    tags = []
    price = -1

    def __init__(self, name: str, emoji_id: int):
        self.name = name
        self.icon = emoji_id

    def make_data_dict(self) -> dict:
        data = {
            "item_type": "item",
            "icon": self.icon
        }
