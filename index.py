from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
def getTwitterTrendingTopics():

    url = 'https://twitter.com/explore'
    driver.get(url)
    sleep(8)

    driver.find_element_by_xpath('//a[@href="/explore/tabs/trending"]').click()

    sleep(5)
    trendingTopicsHTML = driver.find_element_by_xpath(
        '//div[@aria-label="Timeline: Explorar"]').get_attribute('outerHTML')

    driver.quit()
    trendingTopicsList = []

    soup = BeautifulSoup(trendingTopicsHTML, 'html.parser')

    for topic in soup.find_all('div', dir='ltr'):
        if topic.span != None:
            trendingTopicsList.append(topic.span.get_text())

    return trendingTopicsList


def getYoutubeTredingVideos():

    url = 'https://www.youtube.com/feed/trending'
    driver.get(url)
    sleep(8)
    trendingVideosHTML = driver.find_element_by_xpath(
        '//div[@id="grid-container"]').get_attribute('outerHTML')
    soup = BeautifulSoup(trendingVideosHTML, 'html.parser')

    trendingVideosList = []
    contador =0
    for video in soup.find_all('a',id="video-title"):
        trendingVideosList.append(video.get_text().strip())
    
    driver.quit()

    return trendingVideosList



option = int(input('Digite [1] para ver os assuntos do momento do Twitter\n Digite [2]para ver os videos em alta do Youtube\n'))

while option != 1 and option != 2:
    print('Você digitou uma opção inválida!\n')
    option = int(input(' Digite [1] para ver os assuntos do momento do Twitter\n Digite [2] para ver os videos em alta do Youtube\n'))


driver = webdriver.Chrome(ChromeDriverManager().install())
if option == 1:
    lista = getTwitterTrendingTopics()
else:
    lista = getYoutubeTredingVideos()

for item in lista:
    print(item)
