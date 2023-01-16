from game_project.cyberpunk.engine.character.abc_body import IBody
from game_project.cyberpunk.engine.character.abc_character import ICharacter
from game_project.cyberpunk.engine.character.classes.abc_class import IClass
from game_project.cyberpunk.engine.mount.abc_mount import IMount
from game_project.cyberpunk.engine.summon.abc_summon import ISummon


class IPlayer(ICharacter):
    cls: IClass

    body: IBody

    mount: IMount
    summon: ISummon

    @property
    def stats(self):
        return  # get all stats or calculate it(stats-object???maybe stats-dict???)

    @property
    def implants(self):
        return  # get all implants from iBody
