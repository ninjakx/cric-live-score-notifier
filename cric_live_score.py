import subprocess as s
from bs4 import BeautifulSoup
import time
from urllib.request import urlopen

def bsoup_get_html():
    get_url = 'http://www.cricbuzz.com/cricket-match/live-scores'
    url = urlopen(get_url)
    content = url.read()
    return BeautifulSoup(content,"lxml")

while(1):
    soup = bsoup_get_html()

    score = []
    results = []

    for head in soup.find_all('div', attrs={"class": "cb-lv-scrs-col text-black"}):
        score.append(head.text)
    for desc in soup.find_all('div', attrs={"class": "cb-lv-scrs-col cb-text-live"}):
          results.append(desc.text)

 
    s.call(["notify-send", "-i","/home/ninjakx/Desktop/kaam/cric.png",score[0],results[0]])
    time.sleep(30)
