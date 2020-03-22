import json
from urllib.request import urlopen
with urlopen("https://coronavirus-19-api.herokuapp.com/countries/morocco?fbclid=IwAR1VXs16dwAVQJU_ymguD0X1EGwK659cV7E9oNuTz7cNq-SMsQCni2LaFk8") as response:
    source = response.read()

class morocco:
    def status(statut):
        if statut == 'Confirmed':
            data = json.loads(source)
            Confirmed = data['cases']
            return Confirmed
        elif statut == 'Deaths':
            data = json.loads(source)
            Deaths = data['deaths']
            return Deaths
        elif statut == 'Recovered':
            data = json.loads(source)
            Recovered = data['recovered']
            return Recovered
        elif statut == 'TodayConfirmed':
            data = json.loads(source)
            TodayConfirmed = data['todayCases']
            return TodayConfirmed
        elif statut == 'TodayDeaths':
            data = json.loads(source)
            TodayDeaths = data['todayDeaths']
            return TodayDeaths
        else:
            print('ERROR')
