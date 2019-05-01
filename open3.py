#! python3

"""open3.py - Opens several Google search results."""

# Import essential modules.
import sys
import requests
import bs4
import webbrowser

# Download the google search page with words entered in command line with requests module.
result = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
result.raise_for_status()

# Parse this site and retrieve top search results using bs4 module.
result_text = bs4.BeautifulSoup(result.text)
link_elements = result_text.select('.r a')

# Set variable with minimum amount of tabs to be opened.
tabs_opened = min(3, len(link_elements))

# Open every link in new tab using webbrowser.
for i in range(tabs_opened):
    webbrowser.open('http://google.com' + link_elements[i].get('href'))
