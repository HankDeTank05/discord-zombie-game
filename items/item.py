from items.tagging import Tags


class Item:
    tags = [Tags.item]
    price = -1

    def __init__(self, name: str, emoji_id: int):
        self.name = name
        self.icon = emoji_id

    def __str__(self):
        return self.name

    def make_data_dict(self) -> dict:
        data = {
            "item_type": "item",
            "icon": self.icon
        }
        return data


NoneDict = {"name": "none"}
