from unittest import result
import requests

class CountriesService:
    @staticmethod
    def get_countries():
        tab=[]

        result = requests.get(f"https://api.covid19api.com/countries").json()

        for c in result:
            tab.append(c['Country'])

            tab.sort()

        return tab

