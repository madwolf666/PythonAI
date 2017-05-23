import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def _get_write_rss(h_mode, h_site_name, h_url):
    a_xml = requests.get(h_url)
    a_xml.encoding=a_xml.apparent_encoding
    a_soup = BeautifulSoup(a_xml.text, 'html.parser')
    #print(a_soup)
    with open('get_rss_info.txt', h_mode, encoding='utf-8') as a_file:
        a_file.write('********************************************************************************\n')
        a_file.write('*** ' + h_site_name + ' ***\n')
        a_file.write('********************************************************************************\n')
        for news in a_soup.findAll('item'):
            print(news.title.string, news.link.string)
            a_file.write('■' + news.title.string + '\n')
            a_file.write(news.link.string + '\n')

if __name__ == '__main__':
    #Yahoo
    _get_write_rss('w', 'Yahoo', 'http://news.yahoo.co.jp/pickup/science/rss.xml')
    #CNET Japan
    _get_write_rss('a', 'CNET Japan', 'http://feeds.japan.cnet.com/rss/cnet/all.rdf')
    #Impress Watch HeadLine
    _get_write_rss('a', 'Impress Watch Headline', 'http://rss.rssad.jp/rss/headline/headline.rdf')
    #IT Media
    _get_write_rss('a', 'IT Media', 'http://rss.rssad.jp/rss/itmnews/2.0/news_bursts.xml')
    #ZDNet Japan
    _get_write_rss('a', 'ZDNet Japan', 'http://feeds.japan.zdnet.com/rss/zdnet/all.rdf')

    #Engadget Japanese
    _get_write_rss('a', 'Engadget Japanese', 'http://japanese.engadget.com/rss.xml')
    #Gizmodo Japan
    _get_write_rss('a', 'Gizmodo Japan', 'http://www.gizmodo.jp/index.xml')
    #ガジェット通信
    _get_write_rss('a', 'ガジェット通信', 'http://getnews.jp/feed')

    #ライフハッカー
    _get_write_rss('a', 'ライフハッカー', 'http://www.lifehacker.jp/index.xml')
    #GIGAZINE
    _get_write_rss('a', 'GIGAZINE', 'http://feed.rssad.jp/rss/gigazine/rss_2.0')

    JP='iso-2022-jp'
    message=MIMEText(
        'あああああ'.encode(JP),
        'plain',
        JP,
    )
    message['Subject'] = str(Header('こんにちはPython', JP))
    message['From'] = 'madwolf699@gmail.com'
    message['To'] = 'madwolf666@live.jp'
    gm = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    gm.login('madwolf699@gmail.com','chappy666')
    gm.sendmail('madwolf699@gmail.com', 'madwolf666@live.jp', message.as_string())
    gm.close()
