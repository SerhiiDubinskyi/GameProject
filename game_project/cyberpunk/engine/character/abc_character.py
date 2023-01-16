from typing import List

from game_project.cyberpunk.engine.FactionSystem.abc_relationships import IRelationships
from game_project.cyberpunk.engine.character.abc_biography import IBiography
from game_project.cyberpunk.engine.character.abc_body import IBody
from game_project.cyberpunk.engine.character.abc_state import IState
from game_project.cyberpunk.engine.inventory_system.abc_inventory import IInventory


class ICharacter:
    name: str

    action_points: int
    state: IState
    body: IBody
    biography: IBiography
    relationships: IRelationships
    inventory: IInventory

    current_location: List[dict, dict, dict]


    @property
    def stats(self):
        return  # get all stats or calculate it

    @property
    def resists(self):
        return  # get all resistances

    @property
    def health_points(self):
        return self.body.health_points

    @property
    def skills(self):
        return  # all skills from everything

    @property
    def mass(self):
        return  # get all mass

    @property
    def volume(self):
        return  # get all volume

    @property
    def perks(self):
        return  # get all perks

    @property
    def appearance(self):
        return  # get appearance based on equipped items

    @property
    def implants(self):
        return  # get all implants from iBody