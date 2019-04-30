#! python3

"""open2.py - Opens several Google search results."""

# Import essential modules.
import sys
import requests
import bs4
import webbrowser

# Download the google page with entered search words with requests module.
result = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
result.rise_for_status()

# Parse this site and retrieve top search results with bs4 module.
result_text = bs4.BeautifulSoup(result.text)
link_elements = result_text.select('.r a')

# Open new tabs with top links using webbrowser module.
tabs_opened = min(3, len(link_elements))
for i in range(tabs_opened):
    webbrowser.open('http://google.com' + link_elements[i].get('href'))
