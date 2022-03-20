from MyModel import ResultModel
import requests
 
class StatsService:
    @staticmethod
    def get_stats(country):
        result=requests.get(f"https://api.covid19api.com/dayone/country/{country}").json()
 
        rs = ResultModel(country,
        result[-1]['Confirmed'],
        result[-1]['Deaths'],
        result[-1]['Date'][0:10],
        result[-1]['Active'],
 
        )
 
        return rs
    @staticmethod
    def get_deaths_all_countries(countriesList):
        tab=[]
        for country in countriesList:
            stats = StatsService.get_stats(country)
            tab.append(stats.mystats["deaths"])

        return tab