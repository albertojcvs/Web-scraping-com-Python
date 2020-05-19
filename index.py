from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

def getTrendTopics(trendingTopicsHTML):

    trendingTopicsList = []

    soup = BeautifulSoup(trendingTopicsHTML, 'html.parser')

    for topic in soup.find_all('div', dir='ltr'):
        if topic.span != None:
            trendingTopicsList.append(topic.span.get_text())

    return  trendingTopicsList


url = 'https://twitter.com/explore'
driver = webdriver.Chrome()
driver.get(url)
sleep(8)

driver.find_element_by_xpath('//a[@href="/explore/tabs/tab_1"]').click()

sleep(5)
trendingTopicsHTML = driver.find_element_by_xpath(
    '//div[@aria-label="Timeline: Explorar"]').get_attribute('outerHTML')
driver.quit()

trendingTopicsList = getTrendTopics(trendingTopicsHTML)

for topic in trendingTopicsList:
    print(topic)
