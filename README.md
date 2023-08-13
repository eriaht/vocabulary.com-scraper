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
abandon
abate
abdicate
abhorrent
abound
abridge
abscond
abundant
acute
adversary
affect
aggravate
allot
amateur
ambient
amity
anomie
anticipate
appraise
arcanum
obscure
vague
limber
inertia
ambiguous
frugal
corrugated
vestibule
jetty
eulogy
satchel
glut
slander
vicious
immerse
lofty
accost
despicable
carcass
debonair
spondee
spontaneous
momentous
offish
transpose
fasting
inflexible
perish
adept
competent
economical
shrine
incentive
levelheaded
reluctant
hostile
surmount
barred
warily
grating
vagrant
scrappy
dilemma
menagerie
unaccustomed
fluorescent
rodent
humorous
notary
knead
bliss
impulsive
interject
jargon
tight
consequence
obliterate
unison
turmoil
wary
impair
ravage
perpetual
chide
savory
inhabit
fidget
massive
flaunt
hoist
clumsy
frail
utilize
zest
prosperous
defy
wheeze
luminous
incinerate
calligraphy
prestige
profane
whim
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
```


