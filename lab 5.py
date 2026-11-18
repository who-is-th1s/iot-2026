import calendar
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
    def __init__(self, day="", city="", country="", temp=0.0,
                 humidity=0, wind_speed=0.0, weather_type=WeatherType.SUNNY):
        self.__day = day
        self.__city = city
        self.__country = country
        self.__temp = temp
        self.__humidity = humidity
        self.__wind_speed = wind_speed
        self.__type = weather_type
        self.list = []
    def __del__(self):
        print(f"Об'єкт погоди видалено: {self.__city}, {self.__day}")

    def get_day(self):
        return self.__day

    def get_city(self):
        return self.__city

    def get_country(self):
        return self.__country

    def get_temp(self):
        return self.__temp

    def get_humidity(self):
        return self.__humidity

    def get_wind_speed(self):
        return self.__wind_speed

    def get_type(self):
        return self.__type

    def is_lviv_weather(self, humidity, weather_type):
        if humidity > 80 and weather_type == WeatherType.RAINY:
            print("The typical day in Lviv")
        else:
            print("You're lucky, man")

    def __str__(self):
        return (f"Day: {self.__day}, City: {self.__city}, "
                f"Country: {self.__country}, Temp: {self.__temp}, "
                f"Humidity: {self.__humidity}%, "
                f"Wind speed: {self.__wind_speed} m/s, "
                f"Type: {self.__type.name}")

    def __repr__(self):
        return (f"Weather({self.__day!r}, {self.__city!r}, "
                f"{self.__country!r}, {self.__temp}, {self.__humidity}, "
                f"{self.__wind_speed}, {self.__type})")


def find_max_temperature(weathers, day):
    max_temp = None
    for i in weathers:
        if i.get_day() == day:
            if max_temp is None or i.get_temp() > max_temp:
                max_temp = i.get_temp()
    if max_temp is None:
        print("Not enough data")
    else:
        print(f"Max temperature on {day}: {max_temp}")
    return max_temp


class WeatherCalendar:
    def __init__(self, weathers=None):
        self.__weathers = weathers if weathers is not None else []

    def __del__(self):
        print("WeatherCalendar обєкт видалено")

    def add(self, weather):
        self.__weathers.append(weather)

    def get_weathers(self):
        return self.__weathers

    def find_max_temperature(self, day):
        return find_max_temperature(self.__weathers, day)

    def sort_by_day(self):
        self.__weathers.sort(key=lambda w: w.get_day())

    def show(self):
        for i, weather in enumerate(self.__weathers, 1):
            print(f"{i}. {weather}")


def main():
    calendar = WeatherCalendar()
    calendar.add(Weather("2026-11-12", "Lviv", "Ukraine", 4.5, 85, 3.2,
                         WeatherType.RAINY))
    calendar.add(Weather("2026-11-10", "Kyiv", "Ukraine", 7.0, 60, 5.1,
                         WeatherType.CLOUDY))
    calendar.add(Weather("2026-11-12", "Odesa", "Ukraine", 10.2, 55, 6.4,
                         WeatherType.SUNNY))
    calendar.add(Weather("2026-11-11", "Lviv", "Ukraine", 2.0, 90, 1.8,
                         WeatherType.FOGGY))

    print("Before sorting:")
    calendar.show()

    calendar.sort_by_day()
    print("\nAfter sorting by day:")
    calendar.show()

    print()
    calendar.find_max_temperature("2026-11-12")
    calendar.find_max_temperature("2026-12-01")

    print()
    for i in calendar.get_weathers():
        i.is_lviv_weather(i.get_humidity(), i.get_type())


if __name__ == "__main__":
    main()

s1 = WeatherCalendar("hfhg", "jfjf")
s1 = WeatherCalendar()
for i in s1:
    print(f"{i.get_city()}: {i.get_day()}")