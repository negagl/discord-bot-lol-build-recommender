from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Create Webdriver
driver = webdriver.Chrome()

champion = 'qiyana'
role = 'mid'
map_type = ''


def create_url(champion, role='', map_type=''):
    """Create URL based on champion, role and type. Champion in mandatory"""
    url = ''
    if map_type != '':
        url = f'http://www.metasrc.com/lol/{map_type}/build/{champion}'
    elif role != '':
        url = f'http://www.metasrc.com/lol/build/{champion}/{role}'
    else:
        url = f'http://www.metasrc.com/lol/build/{champion}'

    return url


# Get Site in Chrome
url = create_url(champion, role, map_type)
driver.get(url)
driver.implicitly_wait(5)

# get the source code
html = driver.page_source
time.sleep(10)
driver.quit()

# Parse source code with bs4
soup = BeautifulSoup(html, 'html.parser')

summoner1 = soup.select('#page-content > div:nth-child(1) > div:nth-child(1) > section > div > div > div > div:nth-child(1) > div._dcqhsp > div:nth-child(1) > img')[0]['alt']
summoner2 = soup.select('#page-content > div:nth-child(1) > div:nth-child(1) > section > div > div > div > div:nth-child(1) > div._dcqhsp > div:nth-child(2) > img')[0]['alt']
print(summoner1)
print(summoner2)
