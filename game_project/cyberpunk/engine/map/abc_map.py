from typing import List

from game_project.cyberpunk.engine.map.abc_location import ILocation
from game_project.cyberpunk.engine.map.abc_time import ITime
from game_project.cyberpunk.engine.map.abc_weather import IWeather


class IMap:
    locations: List[ILocation]
    weather: IWeather
    time: ITime




