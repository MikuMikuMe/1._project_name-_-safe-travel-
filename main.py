```python
# safe-travel.py

import requests

def get_travel_advisory(country):
    url = f'https://www.travel-advisory.info/api?country={country}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        advisory = data['data'][country]['advisory']['score']
        print(f"Travel Advisory Score for {country}: {advisory}")
    else:
        print("Error fetching travel advisory information.")

def get_covid_stats(country):
    url = f'https://api.covid19api.com/live/country/{country}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        latest_stats = data[-1]
        confirmed = latest_stats['Confirmed']
        deaths = latest_stats['Deaths']
        recovered = latest_stats['Recovered']
        print(f"COVID-19 Stats for {country}: Confirmed - {confirmed}, Deaths - {deaths}, Recovered - {recovered}")
    else:
        print("Error fetching COVID-19 statistics.")

def main():
    country = input("Enter the country you are planning to travel to: ")

    try:
        get_travel_advisory(country)
        get_covid_stats(country)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```

This Python program provides personalized safety recommendations for international travelers by analyzing global travel advisories and COVID-19 statistics based on the country the user plans to travel to. The program prompts the user to enter the country they are planning to travel to, fetches the travel advisory score and COVID-19 statistics for that country using APIs, and displays the information to the user. Error handling is implemented to handle any exceptions that may occur during the API requests.