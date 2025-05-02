import requests
from bs4 import BeautifulSoup

main_leagues = {
    'england': ['E0','E1','E2','E3','EC'],
    'scotland': ['SC0','SC1','SC2','SC3'],
    'germany': ['D1', 'D2'],
    'italy': ['I1', 'I2'],
    'spain': ['SP1', 'SP2'],
    'france': ['F1', 'F2'],
    'netherlands': ['N1'],
    'belgium': ['B1'],
    'portugal': ['P1'],
    'turkey': ['T1'],
    'greece': ['G1']
}

extra_leagues = {
    'argentina': ['ARG'],
    'austria': ['AUT'],
    'brazil': ['BRA'],
    'china': ['CHN'],
    'denmark': ['DNK'],
    'finland': ['FIN'],
    'ireland': ['IRL'],
    'japan': ['JPN'],
    'mexico': ['MEX'],
    'norway': ['NOR'],
    'poland': ['POL'],
    'romania': ['ROU'],
    'russia': ['RUS'],
    'sweden': ['SWE'],
    'switzerland': ['SWZ'],
    'usa': ['USA']
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
    last_updated_text = scrape_last_updated(league+"m.php")
    if last_updated_text is not None:
        print(f"{league.title()} {last_updated_text.lower()}")

for league in extra_leagues:
    # Use the function to scrape the data for a specific URL
    last_updated_text = scrape_last_updated(league+"php")
    if last_updated_text is not None:
        print(f"{league.title()} {last_updated_text.lower()}")