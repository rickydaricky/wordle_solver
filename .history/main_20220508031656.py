from words import WordsController
from tests import Tests


def main():
    Tests.test_word('zesty')

    wc = WordsController(5)
    


if __name__ == "__main__":
    main()
