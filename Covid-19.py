import matplotlib.pyplot as plt
from moroccovid19 import morocco

# Create Variables
Confirmed = morocco.status('Confirmed')
Deaths = morocco.status('Deaths')
Recovered = morocco.status('Recovered')
Today_Confirmed = morocco.status('TodayConfirmed')
Today_Deaths = morocco.status('TodayDeaths')

# Create List
Val = [Confirmed,Deaths,Recovered,Today_Confirmed,Today_Deaths]
Labels = ["Confirmed","Deaths","Recovered","Today Confirmed","Today Deaths"]

# Create Charts
plt.pie(Val, labels=Labels)
plt.show()


