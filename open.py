#! python3

"""open.py - Opens several Google search results."""

# Import essential modules.
import sys
import webbrowser
import requests
import bs4

# Download google search site with requests module.
result = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
result.raise_for_status()

# Parse this site and retrieve top search results links with bs4.
result_text = bs4.BeautifulSoup(result.text)
link_elements = result_text.select('.r a')

# Open a browser tab for each result.
opened_numbers = min(3, len(link_elements))
for i in range(opened_numbers):
    webbrowser.open('http://google.com' + link_elements[i].get('href'))
