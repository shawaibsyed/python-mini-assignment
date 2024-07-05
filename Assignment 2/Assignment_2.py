import time
import requests
from bs4 import BeautifulSoup

NEWS_URL = "https://news.ycombinator.com/"

# Delay in adherence with the robots.txt file
CRAWL_DELAY = 30
PREVIOUS_REQUEST_TIME = 0


def fetch_and_parse_content(url):
    """Fetch and parse the HTML content of the given URL."""
    global PREVIOUS_REQUEST_TIME
    disallowed_links = [
        '/collapse?/',
        '/context?/',
        '/flag?/',
        '/login/',
        '/logout/',
        '/r?/',
        '/reply?/',
        '/submitlink?/',
        '/vote?/',
        '/x?/'
    ]
    if any(link in url for link in disallowed_links):
        return None
    while time.time() < PREVIOUS_REQUEST_TIME + CRAWL_DELAY:
        time.sleep(max(CRAWL_DELAY - (time.time() - PREVIOUS_REQUEST_TIME), 0))
    response = requests.get(url)
    PREVIOUS_REQUEST_TIME = time.time()
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def scrape_news_headlines():
    """Fetch the news from the website, parse HTML content of the page, and extract the news headlines."""
    print("Scraping news headlines...")
    soup = fetch_and_parse_content(NEWS_URL)
    if not soup:
        return []
    headlines = soup.select(".titleline a")
    valid_headlines = [headline for headline in headlines if not headline.span]
    return [headline.get_text() for headline in valid_headlines]


def output_headlines(headlines, print_to_console):
    """Prints the news headlines either to console or writes to .txt file"""
    print(f"\nRetrieved {len(headlines)} headlines. Outputting headlines...\n")
    if print_to_console:
        print('\n'.join(headlines))
    else:
        with open("News_Headlines.txt", "w") as file:
            file.write("\n".join(headlines))
        print(f"\nCompleted outputting {len(headlines)} headlines.")


def main():
    """The main function of the program that orchestrates the operations."""
    headlines = scrape_news_headlines()
    print_to_console = False
    output_headlines(headlines, print_to_console)


if __name__ == "__main__":
    main()