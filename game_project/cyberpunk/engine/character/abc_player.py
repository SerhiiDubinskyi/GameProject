from typing import List

from game_project.cyberpunk.engine.character.abc_body import IBody
from game_project.cyberpunk.engine.character.abc_character import ICharacter
from game_project.cyberpunk.engine.character.abc_state import IState
from game_project.cyberpunk.engine.character.classes.abc_class import IClass
from game_project.cyberpunk.engine.mount.abc_mount import IMount
from game_project.cyberpunk.engine.summon.abc_summon import ISummon


class IPlayer(ICharacter):
    name: str
    cls: IClass

    action_points: int
    state: IState
    body: IBody

    biography: object

    current_location: object

    mount: IMount
    summon: ISummon

    @property
    def stats(self):
        return  # get all stats or calculate it(stats-object???maybe stats-dict???)

    @property
    def health_points(self):
        return self.body.health_points

    @property
    def skills(self):
        return  # all skills from everything

    @property
    def implants(self):
        return  # get all implants from iBody

    @property
    def perks(self):
        return  # get all perks

    @property
    def appearance(self):
        return  # get appearance based on equiped items

    @property
    def mass(self):
        return  # get all mass

    @property
    def volume(self):
        return  # get all volume
