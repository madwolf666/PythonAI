import requests
from bs4 import BeautifulSoup

#Yahoo
#xml = requests.get('http://news.yahoo.co.jp/pickup/science/rss.xml')
#CNET Japan
#xml = requests.get('http://feeds.japan.cnet.com/rss/cnet/all.rdf')
#Impress Watch HeadLine
#xml = requests.get('http://rss.rssad.jp/rss/headline/headline.rdf')
#IT Media
#xml = requests.get('http://rss.rssad.jp/rss/itmnews/2.0/news_bursts.xml')
#ZDNet Japan
#xml = requests.get('http://feeds.japan.zdnet.com/rss/zdnet/all.rdf')

#Engadget Japanese
#xml = requests.get('http://japanese.engadget.com/rss.xml')
#Gizmodo Japan
#xml = requests.get('http://www.gizmodo.jp/index.xml')
#ガジェット通信
#xml = requests.get('http://getnews.jp/feed')

#ライフハッカー
#xml = requests.get('http://www.lifehacker.jp/index.xml')
#GIGAZINE
xml = requests.get('http://feed.rssad.jp/rss/gigazine/rss_2.0')

xml.encoding=xml.apparent_encoding
soup = BeautifulSoup(xml.text, 'html.parser')
print(soup)
for news in soup.findAll('item'):
    print(news.title.string, news.link.string)
