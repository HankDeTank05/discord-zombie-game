from items.wearables.gears.buff import HealthBuff


class Multivitamin(HealthBuff):

    name = "Multivitamin"
    emoji_id = -1
    price = -1
    multiplier = 0.05

    tags = HealthBuff.tags + [name.lower()]

    def __init__(self):
        super().__init__(Multivitamin.name, Multivitamin.emoji_id, Multivitamin.multiplier)


class PowerVitamin(HealthBuff):

    name = "Power Vitamin"
    emoji_id = -1
    price = -1
    multiplier = 0.10

    tags = HealthBuff.tags + [name.lower()]

    def __init__(self):
        super().__init__(PowerVitamin.name, PowerVitamin.emoji_id, PowerVitamin.multiplier)


class SuperVitamin(HealthBuff):

    name = "Super Vitamin"
    emoji_id = -1
    price = -1
    multiplier = 0.15

    tags = HealthBuff.tags + [name.lower()]

    def __init__(self):
        super().__init__(SuperVitamin.name, SuperVitamin.emoji_id, SuperVitamin.multiplier)
