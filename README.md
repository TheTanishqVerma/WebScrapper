# News Headline WebScrapper

This is a simple Python web scraper that fetches top news headlines from the BBC News homepage and saves them into a text file.

## Features
- Fetches the latest news headlines from a public website (`https://www.bbc.com/news`)
- Parses the page using `BeautifulSoup`
- Saves all `<h2>` headlines into a file (`headlines.txt`)
- Includes basic error handling for failed HTTP requests

## File Structure
├── scraper.py # The main Python script
├── README.md # Project documentation
├── headlines.txt # Output file created after running the script

## How to Run
1. Clone or download this project into a local folder.

2. Install dependencies:
   pip install requests beautifulsoup4

3. Run the scraper:
   python scraper.py

4. Check the headlines.txt file for the list of headlines.

## Sample Output
Your headlines.txt file will look like:
1. Hamas leader killed in airstrike
2. UK economy grows faster than expected
3. NASA announces next Moon landing date
...

## Input Validation & Error Handling
The script raises an error if the page cannot be fetched.

Empty or missing elements are handled gracefully.

Headers are set with a User-Agent to mimic a browser and reduce request blocks.