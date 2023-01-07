from game_project.cyberpunk.engine.character.abc_body import IBody
from game_project.cyberpunk.engine.character.abc_state import IState
from game_project.cyberpunk.engine.character.classes.abc_class import IClass


class ICharacter:
    name: str
    cls: IClass

    action_points: int
    state: IState
    body: IBody
    biography: object

    location: object

    @property
    def stats(self):
        return  # get all stats or calculate it

    @property
    def health_points(self):
        return self.body.health_points

    @property
    def perks(self):
        return  # get all perks

    @property
    def appearance(self):
        return  # get appearance based on equipped items
