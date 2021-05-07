from typing import Type

from commands.command import Command
from items.item import Item


class ItemCreationCmd(Command):

    def __init__(self, create_type: Type[Item]):
        super().__init__()
        self.type = create_type
