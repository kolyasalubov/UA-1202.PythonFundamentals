from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather_data(location):
    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(location)
    w = observation.weather
    return {"detailed_status": str(w.detailed_status),
            "wind": str(w.wind),
            "humidity": w.humidity,
            "temperature": w.temperature("celsius"),
            'rain': w.rain,
            "heat_index": w.heat_index,
            "clouds": str(w.clouds)}

    # 'clouds'
    # {'speed': 4.6, 'deg': 330}
    # 87
    # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    # {}
    # None
    # 75
