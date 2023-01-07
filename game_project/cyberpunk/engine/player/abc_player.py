class IPlayer:
    name: str
    cls: object

    action_points: int
    state: object
    body: object

    biography: object #
    stats: object
    perks: object
    # active_slot: object #Inventory with active items? TODO: think about active slots as sub of inventory?
    # inventory: object #Inventory with non-active items

    implants: object #Inventory with active-implants TODO: implants as active_slot sub?

    location: object

    mounts: object
    summon: object
    
    #@property APPEARENCE depends of inventory.equiped items

    # @property
    # def mass(self):
    #     return sum(self.inventory.mass, self.active_slot.mass, self.implants.mass)

    @property
    def health_points(self):
        return self.body.health_points

    @property
    def skills(self):
        return #all skills from evertyhing





