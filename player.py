from typing import Union

import util


class Player:
    max_health = [
        0,
        100
    ]

    def __init__(self, player: Union[str, dict]):
        if isinstance(player, dict):
            self.id = player["id"]
            self.level = player["level"]
            self.health = player["health"]
            self.money = player["money"]

        elif isinstance(player, str):
            self.id = player
            self.level = 1
            self.health = Player.max_health[self.level]
            self.money = 0

            util.new_save_file(player, self.make_data_dict())
            print(f"Making a new file for {player}")

    def make_data_dict(self) -> dict:
        data = {
            "id": self.id,
            "level": self.level,
            "health": self.health,
            "money": self.money
        }
        return data

    def profile(self):
        output = f"Level  {util.emoji('level')} {self.level}\n" \
                 f"Health {util.emoji('health')} {self.health}/{Player.max_health[self.level]}\n" \
                 f"Money  {util.emoji('money')} ${self.money}\n"

        return output

    def save(self):
        util.save_progress(self.id, self._make_data_dict())

    def fight(self):
        pass
