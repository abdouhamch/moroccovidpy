import matplotlib.pyplot as plt
from moroccovid19 import morocco

# Create Variables
Confirmed = morocco.status('Confirmed')
Deaths = morocco.status('Deaths')
Recovered = morocco.status('Recovered')
Today_Confirmed = morocco.status('TodayConfirmed')
Today_Deaths = morocco.status('TodayDeaths')


# Create List
Val = [Confirmed, Deaths, Recovered, Today_Confirmed, Today_Deaths]
Labels = ["Confirmed","Deaths","Recovered","Today Confirmed","Today Deaths"]

# Create Charts
if Today_Deaths == 0:
    Val = [Confirmed, Deaths, Recovered, Today_Confirmed]
    Labels = ["Confirmed", "Deaths", "Recovered", "Today Confirmed"]
    plt.pie(Val, labels=Labels, radius=1.4, autopct='%0.0f%%')
    plt.show()
else:
    plt.pie(Val, labels=Labels, radius=1.4, autopct='%0.0f%%')
    plt.show()
