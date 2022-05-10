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
        self.attempts = 0


    def check_recent_board():
        """
        Checks the most recent results after attempting a word on the website and returns the necessary information to the user

        Params:
        attempted_word: the word you're trying
        Returns: a tuple of new_wrong, new_unknown, and new_known
        """

        driver.get("https://www.nytimes.com/games/wordle/index.html")
        print(driver.title)
        driver.implicitly_wait(1)
        # board = driver.find_element(By.ID, "board")
        rows = driver.find_elements(By.TAG_NAME, "game-row")
        
        
        
        search_button = driver.find_element(By.NAME, "btnK")
        search_box.send_keys("Selenium")
        search_button.click()
        driver.implicitly_wait(1)
        print(driver.find_element(By.NAME, "q").get_attribute("value")) # => "Selenium"

        # driver.quit()
    