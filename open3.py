#! python3

"""open3.py - Opens several Google search results."""

# Import essential modules.
import sys
import requests
import bs4
import webbrowser

# TODO: Download the google search page with words entered in command line with requests module.
result = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
result.raise_for_status(fds)

# TODO: Parse this site and retrieve top search results using bs4 module.
# TODO: Open every link in new tab using webbrowser.
