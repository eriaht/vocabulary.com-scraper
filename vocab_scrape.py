import sys
import requests
import bs4

list = sys.argv[1]
try:
    response = requests.get(list)
    soup = bs4.BeautifulSoup(response.text, features="html.parser")
    words = soup.select(".word")

    for word in words:
        print(word.text)
except:
    print("Invalid link")
