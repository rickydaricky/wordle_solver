import collections
import csv
from words import WordsController
from tests import Tests



def main():
    # Tests.test_word('bater')

    # results = collections.defaultdict(list)
    # wc = WordsController(5)
    # for word in wc.word_options:
    #     results[Tests.test_word(word)].append(word)

    # with open('results.csv', 'w') as f:
    #     for key, value in results.items():
    #         f.write(f'{key}: {value}\n\n')

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
  

if __name__ == "__main__":
    main()