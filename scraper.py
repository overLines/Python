## Author Benjamin Busch
## Description this a little example to analyse remote WebSite
## You need must download following python libraries
## requests, requests_html, beautiFulsoup4
## Beautiful Soup4  -> https://www.crummy.com/software/BeautifulSoup/bs4/doc/
## To must install libraries with the following commands
## py -m pip requests
## py -m pip requests_html
## py -m pip beautiFulsoup4

from requests_html import HTMLSession
from bs4 import BeautifulSoup

print('Example WebScraper')
baseUrl = 'https://www.youtube.com'
URL = baseUrl + '/@EvolutionLab'

def remoteAnalysisYoutubeChannel(curUrl):
    # Write analysis in the html file
    URL = curUrl
    print('Scrapen from:' + URL)
    session1 = HTMLSession()
    page = session1.get(URL)
    page.html.render(sleep=10)
    soup = BeautifulSoup(page.html.html, 'html.parser')
    content = []
    for link in soup.find_all('a'):
        URL = str(link.get('href'))
        if '/watch?' in URL:
            title = str(soup.find_all('title'))
            conStr = '' + title + "-->" + URL + ''
            content.append(conStr)
    unique_urls = []
    for item in content:
        if item not in unique_urls:
            unique_urls.append(item)

    file = open('analysis.html', 'w', encoding='utf8')
    for x in range(len(unique_urls)):
        file.write(str(unique_urls[x] + '\n'))
    message = 'Done with the automatic analysis ;)'

    return message;

#Test the function remoteWebAnalysis(URL)
print(remoteAnalysisYoutubeChannel(URL))
