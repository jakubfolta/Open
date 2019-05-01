#! python3

# Import essential modules.
import sys
import requests
import bs4
import webbrowser

# Download google search website with searched words from command line with requests module.
result = requests.get('https://www.google.com/search?client=' + ' '.join(sys.argv[1:]))
result.raise_for_status()

# Parse this website and retrieve link elements with bs4 module.
result_text = bs4.BeautifulSoup(result.text)
link_elements = result_text.select('.r a')

# Set variable with numbers of tabs to open.
tabs_number = min(3, len(link_elements))

# Open every link in new tab with webbrowser module.
for i in range(tabs_number):
    webbrowser.open('http://google.com' + link_elements[i].get('href'))
