class IWeatherState:
    pass


class IWeather:
    weather_state: IWeatherState
    temperature: int


