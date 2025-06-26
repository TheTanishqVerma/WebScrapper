import requests
from bs4 import BeautifulSoup

# Target URL for top news
URL = "https://www.bbc.com/news"

try:
    # Fetch the webpage
    response = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    response.raise_for_status()  # Check for HTTP errors

    # Parse the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all <h2> headlines
    headlines = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]

    # Save headlines to a text file
    with open('headlines.txt', 'w', encoding='utf-8') as f:
        for i, title in enumerate(headlines, 1):
            f.write(f"{i}. {title}\n")

    print(f"Saved {len(headlines)} headlines to headlines.txt!")
except requests.RequestException as e:
    print(f"Error fetching page: {e}")
