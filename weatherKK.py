#Ex. 02_02 and 02_03 Begin weatherKK.py KKey 3/24/2025
import requests



class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()


    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=f4627a983f79d23d4eeabe9547a3d447")

        except:
            print("No internet connection")


        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        units_sybol = "C"
        if self.units == "imperial":
            units_sybol = "F"
        print(f"In {self.name}, the temperature is currently {self.temp}° {units_sybol}")
        print(f"Today's High: {self.temp_max}° {units_sybol}")
        print(f"Today's Low: {self.temp_min}° {units_sybol}")

my_city = City("Tokyo", 35.6762, 139.6503)  
my_city.temp_print()


vaction_city = City("Summerville", 33.019791, -80.177582, units="imperial")
vaction_city.temp_print() 
print(vaction_city.response_json)  