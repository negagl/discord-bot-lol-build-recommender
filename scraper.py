from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import undetected_chromedriver as uc

# Create Webdriver
driver = webdriver.Chrome()


def create_url(champion, role='', counter=''):
    """Create URL based on champion, role and counter. Champion is mandatory"""
    if counter != '':
        url_to_navigate = f'https://probuildstats.com/champion/{champion}?matchup={counter}'
    elif role != '':
        url_to_navigate = f'https://probuildstats.com/champion/{champion}?role={role}'
    else:
        url_to_navigate = f'https://probuildstats.com/champion/{champion}'

    return url_to_navigate


# dummy vars
champion = 'aatrox'
role = 'top'
counter = 'garen'

# Get Site in Chrome
url = create_url(champion, role, counter)
print(url)
driver.get(url)
driver.implicitly_wait(5)

# get the source code
html = driver.page_source
driver.quit()

# Parse source code with bs4
soup = bs(html, 'html.parser')

mythic1 = soup.select('div.champion-mythics > div.side-column_grid-item.top-items > div:nth-child(1) > div.item-image.mythic-item > img')[0]['alt']
print(mythic1)
mythic2 = soup.select('div.champion-mythics > div.side-column_grid-item.top-items > div:nth-child(2) > div.item-image.mythic-item > img')[0]['alt']
print(mythic2)

