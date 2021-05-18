from typing import Union

from items.consumable import Consumable
from player import Player


class HealthConsumable(Consumable):

    tags = Consumable.tags + ["health", "healing"]

    def __init__(self, name: Union[str, dict],
                 emoji_id: int = None,
                 uses: int = None,
                 health_increase: int = None):
        if isinstance(name, str)\
                and emoji_id is not None\
                and uses is not None\
                and health_increase is not None:
            super().__init__(name, emoji_id, uses)
            self.health_increase = health_increase
        elif isinstance(name, dict):
            super().__init__(name["name"], name["icon"], name["uses_remaining"])
            self.health_increase = name["health_increase"]

    def make_data_dict(self) -> dict:
        data = {
            "item_type": "health_consumable",
            "name": self.name,
            "icon": self.icon,
            "uses_remaining": self.uses_remaining,
            "health_increase": self.health_increase
        }

        return data

    def use(self, plr: Player) -> None:
        if self.uses_remaining > 0:
            if plr.health + self.health_increase >= plr.max_health[plr.level]:
                plr.health = plr.max_health[plr.level]
            else:
                plr.health += self.health_increase

            self.uses_remaining -= 1


class PainKillers(HealthConsumable):

    name = "Pain Killers"
    emoji_id = -1
    price = 5
    base_uses = 5
    health_increase = 5

    tags = HealthConsumable.tags + [name.lower()]

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == PainKillers.name:
            super().__init__(data)
        else:
            super().__init__(PainKillers.name, PainKillers.emoji_id, PainKillers.base_uses, PainKillers.health_increase)


class FirstAidKit(HealthConsumable):

    name = "First Aid Kit"
    emoji_id = -1
    price = 25
    base_uses = 1
    health_increase = 25

    tags = HealthConsumable.tags + [name.lower()]

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == FirstAidKit.name:
            super().__init__(data)
        else:
            super().__init__(FirstAidKit.name, FirstAidKit.emoji_id, FirstAidKit.base_uses, FirstAidKit.health_increase)


class Medkit(HealthConsumable):

    name = "Medkit"
    emoji_id = -1
    price = 50
    base_uses = 1
    health_increase = 50

    tags = HealthConsumable.tags + [name.lower()]

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == Medkit.name:
            super().__init__(data)
        else:
            super().__init__(Medkit.name, Medkit.emoji_id, Medkit.base_uses, Medkit.health_increase)


class Antidote(HealthConsumable):

    name = "Antidote"
    emoji_id = -1
    price = 1000
    base_uses = 1
    health_increase = 1000

    tags = HealthConsumable.tags + [name.lower()]

    def __init__(self, data: dict = None):
        if isinstance(data, dict) and data["name"] == Antidote.name:
            super().__init__(data)
        else:
            super().__init__(Antidote.name, Antidote.emoji_id, Antidote.base_uses, Antidote.health_increase)
