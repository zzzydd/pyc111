import requests
from bs4 import BeautifulSoup

url = "https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw"
html = requests.get(url).text
sel = "#pageptlist > div > div > div > div.d-txt > div.mtitle > a"
soup = BeautifulSoup(html, "lxml")
target = soup.select(sel)
fp = open("c111196101-news.txt", "w", encoding="utf-8")
for t in target:
    print(t.text.strip())
    fp.write(t.text.strip()+"\n")
fp.close()