#! python3

"""open.py - Opens several Google search results."""

# Import essential modules.
import sys
import webbrowser
import requests
import bs4
import pyperclip

# Download google search site with requests module.
# Or by using pyperclip module and copied words.
keywords = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else pyperclip.paste() # ternary operator ;)

result = requests.get('http://google.com/search?q=' + keywords)
result.raise_for_status()

# Parse this site and retrieve top search results links with bs4.
result_text = bs4.BeautifulSoup(result.text)
link_elements = result_text.select('.r a')

# Open a browser tab for each result.
opened_numbers = min(3, len(link_elements))
for i in range(opened_numbers):
    webbrowser.open('http://google.com' + link_elements[i].get('href'))
