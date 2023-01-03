from typing import List
from abc_active_slots import IActiveSlots


class iInventory:
    items:List(object)

    # Maybe active slots will be inside inventory, but as separate objects? 
    # also implants could be here
    
    # def method to work with controller:
    #       TODO: Methods that handles inventory system and synchronise it with database
    #       or just methods to work with inventory system