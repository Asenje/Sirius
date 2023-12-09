import undetected_chromedriver
import time
from selenium import webdriver
import json
from bs4 import BeautifulSoup
from seleniumbase import Driver


options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument('--load-extension=C:\Users\username\Desktop\extension')
#options.add_expermental_option('excludeSwitches', ['enable-automation'])
#options.add_experimental_option('useAutomationExtension', False)

#driver = undetected_chromedriver.Chrome(options=options)
driver = Driver(uc=True)


with open('yandex.ru/OGE_output_obshaga.txt') as f:
    LINKS = f.read().split()

def parse_page(source_text):
    soup = BeautifulSoup(source_text, 'html.parser')
    content_div = soup.find_all('div', class_='Card Card_background-image_none Card_border-radius_m Card_inner-space_l Task Task_controlType_input Task_frame_card')

    if not content_div:
        return None

    print(content_div)

    for content in content_div:
        question_text = content.find('div', class_='Task-Description').text.strip()
        print('\n', question_text)

    print('----------------------------------------------')
    print(content_div)


    for content in content_div:
        answer_text = content.find('div', class_='Task-Scroller').text.strip()
        print(answer_text)
    return {"question": question_text, "answer": answer_text}


def wait_until_captcha_is_done(driver):
    max_retries = 20
    
    while max_retries != 0:
        time.sleep(3)
        output = parse_page(driver.page_source)
        if output:
            return output
    
        max_retries -= 1

    return None


# {"question": "...", "answer": "...", "explanation": "..."}

OUTPUT = [] 
for link in LINKS:
    print(link)
    driver.get(link)

    OUTPUT.append(wait_until_captcha_is_done(driver))

    with open('OGE_output_final_obshaga_yandex.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(OUTPUT))
    
    print('Total size: ', len(OUTPUT))
        
