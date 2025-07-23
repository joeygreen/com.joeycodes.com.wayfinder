import requests
from bs4 import BeautifulSoup

def fetch_html(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def check_availability(html: str, selector: str):
    soup = BeautifulSoup(html, "html.parser")
    element = soup.select_one(selector)
    return element.get_text(strip=True) if element else "This item may be in stock."
