class ResultModel:
     
    def __init__(self,country,confirmed,deaths,date,active):
        self.country = country
        self.mystats={
            "confirmed":confirmed,
            "deaths":deaths,
            "date":date,
            "active":active
        }
 
 
    # return object representation
 
    def __repr__(self):
        return f"{self.country}:{self.mystats}"