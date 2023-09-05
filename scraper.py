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

build = {
    'summoners': [],
    'boots': [],
    'mythic': [],
    'items': [],
}


# Summoners
summoner1 = soup.select('div.champion-spells > div.side-column_grid-item.top-items > div:nth-child(1) > '
                        'div.item-image > img')[0]['alt']
summoner1 = summoner1.replace('Summoner Spell ', '')
summoner2 = soup.select('div.champion-spells > div.side-column_grid-item.top-items > div:nth-child(2) > '
                        'div.item-image > img')[0]['alt']
summoner2 = summoner2.replace('Summoner Spell ', '')

build['summoners'].extend([summoner1, summoner2])


# Boots
boots1 = soup.select('div.champion-skills > div.side-column_grid-item.top-items > div:nth-child(1) > '
                     'div.item-image.completed-item > img')
if len(boots1) != 0:
    boots1 = boots1[0]['alt']
    build['boots'].append(boots1)


# Mythic
mythic1 = soup.select('div.champion-mythics > div.side-column_grid-item.top-items > div:nth-child(1) > '
                      'div.item-image.mythic-item > img')[0]['alt']
build['mythic'].append(mythic1)


# Items
item1 = soup.select('div.champion-items > div.side-column_grid-item.top-items > div:nth-child(1) > '
                    'div.item-image.completed-item > img')[0]['alt']
item2 = soup.select('div.champion-items > div.side-column_grid-item.top-items > div:nth-child(2) > '
                    'div.item-image.completed-item > img')[0]['alt']
item3 = soup.select('div.champion-items > div.side-column_grid-item.top-items > div:nth-child(3) > '
                    'div.item-image.completed-item > img')[0]['alt']
item4 = soup.select('div.champion-items > div.side-column_grid-item.top-items > div:nth-child(4) > '
                    'div.item-image.completed-item > img')[0]['alt']

build['items'].extend([item1, item2, item3, item4])
