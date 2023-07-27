import requests
from bs4 import BeautifulSoup

user_input = "Lutheran Aged Care Albury"
print("Googling...")

# Create the search URL with the user's input
search_url = "https://www.google.com/search?q=" + user_input

# Set a user-agent header to simulate a real web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send the HTTP request to Google
google_search = requests.get(search_url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(google_search.text, 'html.parser')

# Find all the anchor tags containing search result links
search_result_links = soup.select("div.r a")

# Extract and print the links from the search results
for link in search_result_links:
    print(link.get("href"))