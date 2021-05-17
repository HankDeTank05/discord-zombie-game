from items.tagging import Tags
from items.wearables.gear import BuffGear


class HealthBuff(BuffGear):

    tags = BuffGear.tags + [Tags.health_buff]

    def __init__(self, name: str, emoji_id: int, multiplier: float):
        super().__init__(name, emoji_id)
        self.health_multiplier = multiplier


class DamageBuff(BuffGear):

    tags = BuffGear.tags + [Tags.damage_buff]

    def __init__(self, name: str, emoji_id: int, multiplier: float):
        super().__init__(name, emoji_id)
        self.damage_multiplier = multiplier


class ProfitBuff(BuffGear):

    tags = BuffGear.tags + [Tags.profit_buff]

    def __init__(self, name: str, emoji_id: int, multiplier: float):
        super().__init__(name, emoji_id)
        self.profit_multiplier = multiplier
