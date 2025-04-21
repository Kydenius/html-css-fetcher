# CSS and HTML style-extractor

A simple Python tool to fetch the HTML content and linked CSS stylesheets of any webpage. Useful for inspecting site structure, debugging, or scraping design elements which you fancy.

## Features

>ALL WEBPAGES MUST BE INSERTED AS "https://.." for example "https://www.google.com" WILL WORK, "www.google.com" WILL throw an error.
- Prompts the user to enter a URL
- Fetches and displays the full HTML of the page
- Parses and extracts all linked CSS stylesheets
- Resolves relative CSS links correctly
- Displays the contents of each CSS file

## Requirements

- Python 3.6 or newer
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

Install dependencies using pip:

```bash
pip install requests beautifulsoup4
