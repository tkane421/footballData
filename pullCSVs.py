import requests
from bs4 import BeautifulSoup

def scrape_last_updated(url_base, page_name):
    # Send a GET request to the URL
    response = requests.get(f"{url_base}{page_name}")

    # Check if the response was successful (200 OK)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the desired text
        last_updated_text = soup.find('i').text.strip()

        return last_updated_text
    else:
        print(f"Error: {response.status_code}")
        return None

# Use the function to scrape the data for a specific URL
last_updated_text = scrape_last_updated("https://www.football-data.co.uk/", "englandm.php")
last_updated_text2 = scrape_last_updated("https://www.football-data.co.uk/", "sctolandm.php")

if last_updated_text is not None:
    print(f"England {last_updated_text.lower()}")

if last_updated_text2 is not None:
    print(f"Scotland {last_updated_text2.lower()}")