import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Asks user for the URL
URL = input("Enter the URL to fetch: ")

# Main Requests the page HTML
page = requests.get(URL)
print("=== HTML PAGE CONTENT ===")
print(page.text)

# Parse the HTML to find the CSS link
soup = BeautifulSoup(page.text, "html.parser")
css_links = soup.find_all("link", rel="stylesheet")

print("\n=== CSS FILES ===")
for link in css_links:
    css_href = link.get("href")
    if css_href:
        css_url = urljoin(URL, css_href)  # Handles relative URLs
        try:
            css_response = requests.get(css_url)
            print(f"\n--- CSS from {css_url} ---")
            print(css_response.text)
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch CSS from {css_url}: {e}")
