from items.consumable import Consumable
from player import Player


class HealthConsumable(Consumable):

    tags = Consumable.tags + ["health", "healing"]

    def __init__(self, name: str, emoji_id: int, uses: int, health_increase: int):
        super().__init__(name, emoji_id, uses)
        self.health_increase = health_increase

    def use(self, plr: Player) -> None:
        if self.uses_remaining > 0:
            if plr.health + self.health_increase >= plr.max_health[plr.level]:
                plr.health = plr.max_health[plr.level]
            else:
                plr.health += self.health_increase

            self.uses_remaining -= 1


class PainKillers(HealthConsumable):

    tags = HealthConsumable.tags + ["pain killers"]

    name = "Pain Killers"
    emoji_id = None
    price = -1
    base_uses = 5
    health_increase = 5

    def __init__(self):
        super().__init__(PainKillers.name, PainKillers.emoji_id, PainKillers.base_uses, PainKillers.health_increase)


class FirstAidKit(HealthConsumable):

    tags = HealthConsumable.tags + ["first aid kit"]

    name = "First Aid Kit"
    emoji_id = None
    price = -1
    base_uses = 1
    health_increase = 25

    def __init__(self):
        super().__init__(FirstAidKit.name, FirstAidKit.emoji_id, FirstAidKit.base_uses, FirstAidKit.health_increase)


class Medkit(HealthConsumable):

    tags = HealthConsumable.tags + ["medkit"]

    name = "Medkit"
    emoji_id = None
    price = -1
    base_uses = 1
    health_increase = 50

    def __init__(self):
        super().__init__(Medkit.name, Medkit.emoji_id, Medkit.base_uses, Medkit.health_increase)


class Antidote(HealthConsumable):

    tags = HealthConsumable.tags + ["antidote"]

    name = "Antidote"
    emoji_id = None
    price = -1
    base_uses = 1
    health_increase = 999

    def __init__(self):
        super().__init__(Antidote.name, Antidote.emoji_id, Antidote.base_uses, Antidote.health_increase)
