#! python3

"""open5.py - Opens several Google search results."""

# Import essential modules.
import sys
import requests
import bs4
import webbrowser

# Download google search site with searched words from command line using requests module.
result = requests.get('https://www.google.com/search?client=' + ' '.join(sys.argv[1:]))
result.raise_for_status()

# Parse this site and retrieve link elements using bs4 module.
result_text = bs4.BeautifulSoup(result.text)
link_elements = result_text.select('.r a')

# TODO: Set variable with tabs number to be opened.


# TODO: Open every link in new tab.
