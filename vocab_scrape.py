# Written by EriahT
# This script scrapes vocabulary lists from vocabulary.com

import sys
import requests
import bs4

# Get the link from the first command line argument
list = sys.argv[1]

try:
    # Request the page for the list
    response = requests.get(list)
    # Make soup from the HTML in the response
    soup = bs4.BeautifulSoup(response.text, features="html.parser")
    # Select all elements with class "word"
    words = soup.select(".word")

    # Print all the words
    for word in words:
        print(word.text)
except:
    print("Error: Invalid link, please try a valid vocabulary.com url")
