from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class Website():
    """
    Class for interacting with the website via selenium
    """

    def __init__(self):
        self.site = 'https://www.nytimes.com/games/wordle/index.html'


    