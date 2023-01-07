from typing import List

from game_project.cyberpunk.engine.inventory_system.abc_implant import IImplant
from game_project.cyberpunk.engine.inventory_system.abc_slot import ISlot


class IBodyPart:
    state: object
    health_points: float
    implant: IImplant
    active_slot: ISlot
    passive_slots: List[ISlot]

class IBody:
    head: IBodyPart

    torso: IBodyPart

    right_hand: IBodyPart
    left_hand: IBodyPart

    left_leg: IBodyPart
    right_leg: IBodyPart
