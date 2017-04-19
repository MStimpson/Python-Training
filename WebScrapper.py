from webLogic import Logic
import os

os.system('cls')
url = 'http://example.webscraping.com'
logic = Logic(url)
logic.webScrapper(url)