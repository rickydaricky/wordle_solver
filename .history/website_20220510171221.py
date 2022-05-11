from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Website():
    """
    Class for interacting with the website via selenium
    """

    def __init__(self):
        self.site = 'https://www.nytimes.com/games/wordle/index.html'
        self.attempts = 0

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def check_recent_board(self, attempted_word):
        """
        Checks the most recent results after attempting a word on the website and returns the necessary information to the user

        Params:
        attempted_word: the word you're trying
        Returns: a tuple of new_wrong, new_unknown, and new_known
        """

        # set up driver and site
        self.driver.get(self.site)
        self.driver.implicitly_wait(1)

        # find the row of blank spaces to insert our attempted_word into
        rows = self.driver.find_elements(By.TAG_NAME, "game-row")
        right_row = rows[self.attempts]
        
        returned_boxes = right_row.find_elements(By.TAG_NAME, "game-tile")
        for i in range(len(returned_boxes)):
            b = returned_boxes[i]
            b.send_keys(attempted_word[i])

            # if reach last column box, press enter to check the word
            if i == 4:
                right_row[i].send_keys(Keys.RETURN)


        # Below is all about retrieving the results of the insertion

        
        # new_wrong: a list of letters representing things you newly learned are wrong
        new_wrong = []

        # new_unknown: list of tuples, with each tuple being (letter, wrong_index)
        new_unknown = []

        # now_known: list of tuples, with each tuple being (letter, correct_index)
        now_known = []

        # wait for the letters to flip and get checked
        self.driver.implicitly_wait(2)

        # returned_boxes = right_row.find_elements(By.TAG_NAME, "game-tile")
        for i in range(len(returned_boxes)):
            b = returned_boxes[i]
            letter = b.letter()
            evaluation = b.evaluation()
            if evaluation == "absent":
                new_wrong.append(letter)
            else:
                if evaluation == "correct":
                    now_known.append((letter, i))
                elif evaluation == "present":
                    new_unknown.append((letter, i))

        search_button = self.driver.find_element(By.NAME, "btnK")
        # search_box.send_keys("Selenium")
        search_button.click()
        self.driver.implicitly_wait(1)
        print(self.driver.find_element(By.NAME, "q").get_attribute("value")) # => "Selenium"

        self.attempts += 1