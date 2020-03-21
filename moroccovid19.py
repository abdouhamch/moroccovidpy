import json
from urllib.request import urlopen

with urlopen("https://coronavirus-19-api.herokuapp.com/countries/morocco?fbclid=IwAR1VXs16dwAVQJU_ymguD0X1EGwK659cV7E9oNuTz7cNq-SMsQCni2LaFk8") as response:
    source = response.read()

print(json.loads(source))

def Confirmed():
    data = json.loads(source)
    Confirmed = data['cases']
    return Confirmed
def Deaths():
    data = json.loads(source)
    Deaths = data['deaths']
    return Deaths
def Recovered():
    data = json.loads(source)
    Recovered = data['recovered']
    return Recovered

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
    else:
        print('error in parametre')
