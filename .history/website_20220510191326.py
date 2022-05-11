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

        # set up driver and site
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.driver.get(self.site)
        self.driver.implicitly_wait(15)

        # Close the overlay that pops up
        x_button = self.driver.execute_script(
            "return document.querySelector('game-app').shadowRoot.querySelector('game-theme-manager').querySelector('#game').querySelector('game-modal').shadowRoot.querySelector('.close-icon')")
        x_button.click()
        self.driver.implicitly_wait(15)

    def check_recent_board(self, attempted_word):
        """
        Checks the most recent results after attempting a word on the website and returns the necessary information to the user

        Params:
        attempted_word: the word you're trying
        Returns: a tuple of new_wrong, new_unknown, and new_known
        """

        # find the row of blank spaces to insert our attempted_word into
        # rows = self.driver.find_elements(By.TAG_NAME, "game-row")

        self.driver.implicitly_wait(15)
        right_row = self.driver.execute_script(
            f"return document.querySelector('game-app').shadowRoot.querySelector('game-theme-manager').querySelector('#game').querySelector('#board').children[{self.attempts}].shadowRoot.querySelector('.row')")
        self.driver.implicitly_wait(15)

        returned_boxes = right_row.find_elements(By.TAG_NAME, "game-tile")

        # print(len(returned_boxes))
        assert(len(returned_boxes) > 0)

        # self.driver.implicitly_wait(15)

        # for i in range(len(returned_boxes)):
        #     b = returned_boxes[i]
        #     b.send_keys(attempted_word[i])

        for i in range(len(attempted_word)):
            game = webdriver.ActionChains(self.driver)
            game.send_keys(attempted_word[i]).perform()

            # if reach last column box, press enter to check the word
            if i == 4:
                game.send_keys(Keys.RETURN)

        # Below is all about retrieving the results of the insertion

        # new_wrong: a list of letters representing things you newly learned are wrong
        new_wrong = []

        # new_unknown: list of tuples, with each tuple being (letter, wrong_index)
        new_unknown = []

        # now_known: list of tuples, with each tuple being (letter, correct_index)
        now_known = []

        # wait for the letters to flip and get checked
        self.driver.implicitly_wait(15)

        # returned_boxes = right_row.find_elements(By.TAG_NAME, "game-tile")
        for i in range(len(returned_boxes)):
            b = returned_boxes[i]
            letter = b.get_attribute("letter")
            evaluation = b.get_attribute("evaluation")
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
        print(self.driver.find_element(
            By.NAME, "q").get_attribute("value"))  # => "Selenium"

        self.attempts += 1
