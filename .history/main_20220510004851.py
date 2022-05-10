from words import WordsController
from tests import Tests
from selenium import webdriver

import collections
import csv


def main():
    Tests.test_word('bater')

    # results = collections.defaultdict(list)
    # wc = WordsController(5)
    # for word in wc.word_options:
    #     results[Tests.test_word(word)].append(word)

    # with open('results.csv', 'w') as f:
    #     for key, value in results.items():
    #         f.write(f'{key}: {value}\n\n')


    driver = webdriver.Chrome()

    driver.get("http://selenium.dev")

    driver.quit()
  

if __name__ == "__main__":
    main()
