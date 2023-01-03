class IPlayer:
    name: str
    cls: object

    health_points: float
    action_points: int

    skills: object # Skill-class
    biography: object #
    stats: object
    perks: object
    active_slots: object #Inventory with active items? TODO: think about active slots as sub of inventory?
    inventory: object #Inventory with non-active items
    implants: object #Inventory with active-implants TODO: implants as active_slots sub?

    location: object

    mounts: object
    summon: object
    
    #@property APPEARENCE depends of inventory.equiped items




