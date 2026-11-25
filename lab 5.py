from enum import Enum


class WeatherType(Enum):
    SUNNY = "SUNNY"
    CLOUDY = "CLOUDY"
    RAINY = "RAINY"
    FOGGY = "FOGGY"
    SNOWY = "SNOWY"
    WINDY = "WINDY"
    STORMY = "STORMY"


class Weather:
    def __init__(
        self,
        day="",
        city="",
        country="",
        temperature=0.0,
        humidity=0,
        wind_speed=0.0,
        weather_type=WeatherType.SUNNY,
    ):
        self.__day = day
        self.__city = city
        self.__country = country
        self.__temperature = temperature
        self.__humidity = humidity
        self.__wind_speed = wind_speed
        self.__type = weather_type

    def __del__(self):
        print(f"Об'єкт погоди видалено: {self.__city}, {self.__day}")

    def get_day(self):
        return self.__day

    def get_city(self):
        return self.__city

    def get_country(self):
        return self.__country

    def get_temperature(self):
        return self.__temperature

    def get_humidity(self):
        return self.__humidity

    def get_wind_speed(self):
        return self.__wind_speed

    def get_type(self):
        return self.__type

    def is_lviv_weather(self):
        return self.__humidity > 80 and self.__type == WeatherType.RAINY

    def __str__(self):
        return (f"Day: {self.__day}, City: {self.__city}, "
                f"Country: {self.__country}, "
                f"Temperature: {self.__temperature}, "
                f"Humidity: {self.__humidity}%, "
                f"Wind speed: {self.__wind_speed} m/s, "
                f"Type: {self.__type.name}")

    def __repr__(self):
        return (f"Weather({self.__day!r}, {self.__city!r}, "
                f"{self.__country!r}, {self.__temperature}, "
                f"{self.__humidity}, {self.__wind_speed}, {self.__type})")


def find_max_temperature(weathers, day):
    max_temp = None
    for weather in weathers:
        if weather.get_day() == day:
            if max_temp is None or weather.get_temperature() > max_temp:
                max_temp = weather.get_temperature()
    return max_temp


class WeatherCalendar:
    def __init__(self, weathers=None):
        self.__weathers = weathers if weathers is not None else []

    def __del__(self):
        print("WeatherCalendar обєкт видалено")

    def __iter__(self):
        return iter(self.__weathers)

    def add(self, weather):
        self.__weathers.append(weather)

    def get_weathers(self):
        return self.__weathers

    def find_max_temperature(self, day):
        return find_max_temperature(self.__weathers, day)

    def sort_by_day(self):
        self.__weathers.sort(key=lambda weather: weather.get_day())

    def show(self):
        for index, weather in enumerate(self.__weathers, 1):
            print(f"{index}. {weather}")


def print_max_temperature(weather_calendar, day):
    max_temp = weather_calendar.find_max_temperature(day)
    if max_temp is None:
        print("Not enough data")
    else:
        print(f"Max temperature on {day}: {max_temp}")


def main():
    weather_calendar = WeatherCalendar()
    weather_calendar.add(Weather("2026-11-12", "Lviv", "Ukraine", 4.5, 85,
                                 3.2, WeatherType.RAINY))
    weather_calendar.add(Weather("2026-11-10", "Kyiv", "Ukraine", 7.0, 60,
                                 5.1, WeatherType.CLOUDY))
    weather_calendar.add(Weather("2026-11-12", "Odesa", "Ukraine", 10.2, 55,
                                 6.4, WeatherType.SUNNY))
    weather_calendar.add(Weather("2026-11-11", "Lviv", "Ukraine", 2.0, 90,
                                 1.8, WeatherType.FOGGY))

    print("Before sorting:")
    weather_calendar.show()

    weather_calendar.sort_by_day()
    print("\nAfter sorting by day:")
    weather_calendar.show()

    print()
    print_max_temperature(weather_calendar, "2026-11-12")
    print_max_temperature(weather_calendar, "2026-12-01")

    print()
    for weather in weather_calendar:
        if weather.is_lviv_weather():
            print("The typical day in Lviv")
        else:
            print("You're lucky, man")

    print()
    for weather in weather_calendar:
        print(f"{weather.get_city()}: {weather.get_day()}")


if __name__ == "__main__":
    main()
