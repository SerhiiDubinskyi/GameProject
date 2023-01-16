from typing import List


class IWeatherState:
    pass


class IWeather:
    weather_states: List[IWeatherState]
    temperature: int


