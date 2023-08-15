# vocabulary.com-scraper
This is a python script that scrapes vocabulary lists from vocabulary.com and outputs the list to your command line.

## How to use the script
This script takes a single command line argument, the argument will be the link to your list on vocabulary.com.
* Make sure you have python installed
* The packages you'll need installed are requests and bs4
* Open your command line of choice
* Enter 
```
pip3 install requests bs4
python vocab_scrape.py <link to vocabulary.com vocab list>
```

### How I used the script to output the list of words to a text file on my desktop
```
python vocab_scrape.py https://www.vocabulary.com/lists/98722 > ~/Desktop/words.txt
```
#### Example output
```
...
thrift
malign
boggy
eccentric
haughty
augment
sublime
hypocrite
hygienic
err
parity
glorify
...
```


