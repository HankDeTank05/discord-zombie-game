from items.tagging import Tags
from items.wearable import Wearable


class Armor(Wearable):

    tags = Wearable.tags + [Tags.armor]

    def __init__(self, name: str, emoji_id: int, protection: int, durability: int):
        super().__init__(name, emoji_id)
        self.protection = protection
        self.durability = durability


''' SUBCLASSES '''


class RiotShield(Armor):

    name = "Riot Shield"
    emoji_id = -1
    price = -1
    protection = 2
    base_durability = 100

    tags = Armor.tags + [name.lower()]

    def __init__(self):
        super().__init__(RiotShield.name,
                         RiotShield.emoji_id,
                         RiotShield.protection,
                         RiotShield.base_durability)


class MetalSleeves(Armor):

    name = "Metal Sleeves"
    emoji_id = -1
    price = -1
    protection = 5
    base_durability = 115

    tags = Armor.tags + [name.lower()]

    def __init__(self):
        super().__init__(MetalSleeves.name,
                         MetalSleeves.emoji_id,
                         MetalSleeves.protection,
                         MetalSleeves.base_durability)


class MetalBodyArmor(Armor):

    name = "Metal Body Armor"
    emoji_id = -1
    price = -1
    protection = 25
    base_durability = 200

    tags = Armor.tags + [name.lower()]

    def __init__(self):
        super().__init__(MetalBodyArmor.name,
                         MetalBodyArmor.emoji_id,
                         MetalBodyArmor.protection,
                         MetalBodyArmor.base_durability)
