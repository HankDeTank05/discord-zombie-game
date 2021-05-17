from typing import Type

from items.tagging import Tags
from items.wearable import Wearable


class Gear(Wearable):

    tags = Wearable.tags + [Tags.gear]

    def __init__(self, name: str, emoji_id: int):
        super().__init__(name, emoji_id)


''' SUBCLASSES '''


class StorageGear(Gear):

    tags = Gear.tags + [Tags.storage_gear]

    def __init__(self, name: str, emoji_id: int, storage_type: Type, storage_amount: int):
        super().__init__(name, emoji_id)


class BuffGear(Gear):

    tags = Gear.tags + [Tags.buff_gear]

    def __init__(self, name: str, emoji_id: int):
        super().__init__(name, emoji_id)
