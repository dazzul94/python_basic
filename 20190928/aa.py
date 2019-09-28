from bs4 import BeautifulSoup
import urllib.request as req

url = "https://news.naver.com/"
res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')
# #today_main_news > div.hdline_news > ul > li:nth-child(1) > div.hdline_article_tit > a
a_links = soup.select('#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a')

for a_link in a_links:
    name = a_link.string
    print(name.strip())
