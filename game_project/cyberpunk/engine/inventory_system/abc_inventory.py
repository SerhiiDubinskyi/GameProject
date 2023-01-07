from typing import List
from abc_active_slots import IActiveSlots


class IInventory:
    items: List[object]
    volume: float

    @property
    def volume(self):
        return sum(item.volume for item in self.items)

    @property
    def mass(self):
        return sum(item.mass for item in self.items)
