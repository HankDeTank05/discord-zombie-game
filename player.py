from typing import Union

import util
import items


class Player:
    max_health = [
        0,
        100
    ]

    default_melee = items.melee.Knife()
    default_ranged = items.ranged.Bow()

    def __init__(self, player: Union[str, dict]):
        if isinstance(player, dict):
            self.id = player["id"]
            self.level = player["level"]
            self.health = player["health"]
            self.money = player["money"]

            try:
                self.weapon_melee = player["weapon_melee"]
            except KeyError:
                self.weapon_melee = items.melee.Knife()

            try:
                self.weapon_ranged = player["weapon_ranged"]
            except KeyError:
                self.weapon_ranged = items.ranged.Bow()

        elif isinstance(player, str):
            self.id = player
            self.level = 1
            self.health = Player.max_health[self.level]
            self.money = 0
            self.weapon_melee = items.melee.Knife()
            self.weapon_ranged = items.ranged.Bow()

            util.new_save_file(player, self.make_data_dict())
            print(f"Making a new file for {player}")

    def make_data_dict(self) -> dict:
        data = {
            "id": self.id,
            "level": self.level,
            "health": self.health,
            "money": self.money,
            "weapon_melee": self.weapon_melee.make_data_dict(),
            "weapon_ranged": self.weapon_ranged.make_data_dict()
        }
        return data

    def profile(self):
        output = f"Level  {util.emoji('level')} {self.level}\n" \
                 f"Health {util.emoji('health')} {self.health}/{Player.max_health[self.level]}\n" \
                 f"Money  {util.emoji('money')} ${self.money}\n"

        return output

    def save(self):
        util.save_progress(self.id, self.make_data_dict())

    def fight(self):
        pass
