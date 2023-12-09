import time
from selenium import webdriver
import json
from bs4 import BeautifulSoup
from seleniumbase import Driver

with open('yandex.ru/url_yandex.txt') as f:
    LINKS = f.read().split()

for project_url in projects_urls:
    req = requests.get(project_url)
    req.encoding = 'utf-8'

    soup = BeautifulSoup(req.text, 'html.parser')
    questions = soup.find_all('div', class_='Task-Description')
    for question in questions:
        print(question.text)
    '''парсинг вопросов'''


    soup = BeautifulSoup(req.text, 'html.parser')
    explanations = soup.find_all('div', class_='Text Text_size_m TaskBlock TaskBlock_type_text TaskBlock_parentBlock_ResultLine')
    for explanation in explanations:
        print(explanation.text)
    '''парсинг объяснений'''
    

    soup = BeautifulSoup(req.text, 'html.parser')
    answers = soup.find_all('div', class_='Row Row_gapTop_m')
    for answer in answers:
        print(answer.text)
