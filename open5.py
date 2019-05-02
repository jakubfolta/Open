#! python3

"""open5.py - Opens several Google search results."""

# Import essential modules.
import sys
import requests
import bs4
import webbrowser
import pyperclip

# Download google search site with searched words from command line using requests module.
# Or using pyperclip module and copied words.
keywords = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else pyperclip.paste()

result = requests.get('https://www.google.com/search?client=' + keywords)
result.raise_for_status()

# Parse this site and retrieve link elements using bs4 module.
result_text = bs4.BeautifulSoup(result.text)
link_elements = result_text.select('.r a')

# Set variable with tabs number to be opened.
opened_tabs = min(3, len(link_elements))

# Open every link in new tab.
for i in range(opened_tabs):
    webbrowser.open('http://google.com' + link_elements[i].get('href'))
