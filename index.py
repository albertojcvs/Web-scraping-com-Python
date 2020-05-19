from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

def getTrendTopics(trendTopicsHTML):

    trendTopicsList = []

    soup = BeautifulSoup(trendTopicsHTML, 'html.parser')

    for trend in soup.find_all('div', dir='ltr'):
        if trend.span != None :
            trendTopicsList.append(trend.span.get_text())
    
    return trendTopicsList

url = 'https://twitter.com/explore'
option = Options()
option.headless= True
driver = webdriver.Chrome(options= option)
driver.get(url)
sleep(8)

driver.find_element_by_xpath('//a[@href="/explore/tabs/tab_1"]').click();

sleep(5)
trendTopicsHTML = driver.find_element_by_xpath('//div[@aria-label="Timeline: Explorar"]').get_attribute('outerHTML')
driver.quit()

trendTopicsList =  getTrendTopics(trendTopicsHTML)

for trend in  trendTopicsList: 
    print(trend)