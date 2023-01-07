from typing import List

from game_project.cyberpunk.engine.inventory_system.abc_item import IItem


class IInventory:
    items: List[IItem]
    volume: float

    @property
    def volume(self):
        return sum(item.volume for item in self.items)

    @property
    def mass(self):
        return sum(item.mass for item in self.items)
