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

# TODO: Parse this site and retrieve top search results links with bs4.
# TODO: Open a browser tab for each result.
