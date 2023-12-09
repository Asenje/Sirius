import requests
from bs4 import BeautifulSoup
from seleniumbase import Driver
import undetected_chromedriver
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

driver = Driver(uc=True)
url = 'https://tutor.yandex.ru/tutor/subject/?subject_id=25'
driver.get(url)

LINKS = []
def get_data(source_text):

    soup = BeautifulSoup(source_text, 'html.parser')

    divs = soup.find_all('div', class_='Text Text_size_m TopicListCard-LinkText TopicListCard-LinkText_spaced')
    for div in divs:
        project_url = 'https://tutor.yandex.ru' + div.find('a').get('href')
        LINKS.append(project_url)
        print(project_url)

        with open('OGE_output.json', 'w') as f:
            f.write('\n'.join(LINKS))

        

get_data(driver.page_source)


# https://tutor.yandex.ru/tutor/subject/tag/problems/?ege_number_id=274&tag_id=19
# https://yandex.ru/tutor/subject/tag/problems/?ege_number_id=274&tag_id=19 