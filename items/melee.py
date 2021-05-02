from weaponTypes import MeleeWeapon


class Knife(MeleeWeapon):

    def __init__(self):
        super().__init__("Knife", ":dagger_knife:", 1, 10, 1)


class Crowbar(MeleeWeapon):

    def __init__(self):
        super().__init__("Crowbar", ":question:", 1, 10, 3)


class SportsStick(MeleeWeapon):

    def __init__(self, name: str, emoji: str):
        super().__init__(name, emoji, 1, 10, 5)


class BaseballBat(SportsStick):

    def __init__(self):
        super().__init__("Baseball Bat", ":question:")


class HockeyStick(SportsStick):

    def __init__(self):
        super().__init__("Hockey Stick", ":hockey:")


class GolfClub(SportsStick):

    def __init__(self):
        super().__init__("Golf Club", ":golfer:")


class LacrosseStick(SportsStick):

    def __init__(self):
        super().__init__("Lacrosee Stick", ":lacrosse:")


class RoadSign(MeleeWeapon):

    def __init__(self):
        super().__init__("Road Sign", ":no_entry:", 1, 10, 7)
