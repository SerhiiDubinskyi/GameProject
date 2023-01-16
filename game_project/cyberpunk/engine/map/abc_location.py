from typing import List

from game_project.cyberpunk.engine.FactionSystem.abc_faction import IFaction
from game_project.cyberpunk.engine.map.abc_place import IPlace
from game_project.cyberpunk.engine.map.abc_weather import IWeather

class ILocationType:
    pass

class ILocation:
    places: List[IPlace]
    owner: IFaction
    weather: IWeather | None
    location_type: ILocationType
    safety: int
    position: dict  # x, y ,z pos of the location on the map
