from .abc_item import IItem


class ISlot:
    item: IItem
    @property
    def is_empty(self):
        return bool(self.item)
