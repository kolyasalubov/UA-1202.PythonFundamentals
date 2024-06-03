from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather_data(location):
    observation = mgr.weather_at_place(location)
    w = observation.weather
    return {"detailed_status": w.detailed_status,
            "wind_speed": w.wind().get('speed'),
            "wind_deg": w.wind().get('deg'),
            "humidity": w.humidity,
            "temperature": w.temperature("celsius"),
            'rain': w.rain,
            "heat_index": w.heat_index,
            "clouds": w.clouds}
