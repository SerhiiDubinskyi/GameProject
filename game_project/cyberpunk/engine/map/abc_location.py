from typing import List

from game_project.cyberpunk.engine.map.abc_place import IPlace


class ILocation:
    places: List[IPlace]