
# This is a script to know if any source is damaged/all champions are well-written

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import constants

url1 = "https://probuildstats.com/champion/"    # Eg: https://probuildstats.com/champion/lillia
url2 = "https://www.lolvvv.com/es/champion/"    # EG: https://www.lolvvv.com/es/champion/Lillia/build

c = Options()
c.add_argument("--headless")
driver = webdriver.Chrome(options=c)

for champion in constants.CHAMPIONS_LIST:
    print("Champion Name: " + champion)

    try:
        driver.get(url1 + champion)
        driver.implicitly_wait(5)
        html1 = driver.page_source

        driver.get(url2 + champion + "/build")
        driver.implicitly_wait(5)
        html2 = driver.page_source

        print(html1)

    except Exception:
        print(Exception)

driver.quit()
