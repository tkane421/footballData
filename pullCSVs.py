import requests
from bs4 import BeautifulSoup

main_leagues = {
    'England': {'page': 'englandm.php', 'prefix' : 'E'},
    'Scotland': {'page': 'scotlandm.php', 'prefix' : 'SC'},
    'Germany': {'page': 'germanym.php', 'prefix' : 'D'},
    'Italy': {'page': 'italym.php', 'prefix' : 'I'},
    'Spain': {'page': 'spainm.php', 'prefix' : 'SP'},
    'France': {'page': 'francem.php', 'prefix': 'F'},
    'Netherlands': {'page': 'netherlandsm.php', 'prefix': 'N'},
    'Belgium': {'page': 'belgiumm.php', 'prefix': 'B'},
    'Portugal': {'page': 'portgualm.php', 'prefix': 'P'},
    'Turkey': {'page': 'turkeym.php', 'prefix': 'T'},
    'Greece': {'page': 'greecem.php', 'prefix': 'G'}
}

extra_leagues = {
    'Argentina': {'page': 'argentina.php', 'file': 'ARG'},
    'Austria': {'page': 'austria.php', 'file': 'AUT'},
    'Brazil': {'page': 'brazil.php', 'file': 'BRA'},
    'China': {'page': 'china.php', 'file': 'CHN'},
    'Denmark': {'page': 'denmark.php', 'file': 'DNK'},
    'Finland': {'page': 'finland.php', 'file': 'FIN'},
    'Ireland': {'page': 'ireland.php', 'file': 'IRL'},
    'Japan': {'page': 'japan.php', 'file': 'JPN'},
    'Mexico': {'page': 'mexico.php', 'file': 'MEX'},
    'Norway': {'page': 'norway.php', 'file': 'NOR'},
    'Poland': {'page': 'poland.php', 'file': 'POL'},
    'Romania': {'page': 'romania.php', 'file': 'ROU'},
    'Russia': {'page': 'russia.php', 'file': 'RUS'},
    'Sweden': {'page': 'sweden.php', 'file': 'SWE'},
    'Switzerland': {'page': 'switzerland.php', 'file': 'SWZ'},
    'USA': {'page': 'usa.php', 'file': 'USA'}
}

def scrape_last_updated(page_name):
    # Send a GET request to the URL
    response = requests.get(f"https://www.football-data.co.uk/{page_name}")

    # Check if the response was successful (200 OK)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.find('i').text.strip()
    else:
        print(f"Error: {response.status_code}")
        return None

for league in main_leagues:
    # Use the function to scrape the data for a specific URL
    last_updated_text = scrape_last_updated(main_leagues[league]['page'])
    if last_updated_text is not None:
        print(f"{league} {last_updated_text.lower()}")

for league in extra_leagues:
    # Use the function to scrape the data for a specific URL
    last_updated_text = scrape_last_updated(extra_leagues[league]['page'])
    if last_updated_text is not None:
        print(f"{league} {last_updated_text.lower()}")