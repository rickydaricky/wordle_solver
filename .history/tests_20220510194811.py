from game import Game
from words import WordsController
from website import Website

MAX_ATTEMPTS = 10


class Tests():
    """
    Class for JUnit testing
    """

    def __init__(self):
        pass

    @staticmethod
    def test_word(correct_word):
        """
        Tests the given word and prints out each try
        """

        found = False

        # set up the game
        game_board = Game(correct_word)
        wc = WordsController(5)

        chosen = 'salet'

        for i in range(MAX_ATTEMPTS):

            print(chosen)

            answer = wc.try_word(game_board, chosen)
            if answer != False:
                print(f'complete in {i + 1} turns!')
                found = True
                return i + 1

            chosen = wc.choose_word()

        print(f'failure to find the word within {MAX_ATTEMPTS} steps')
        return False

    @staticmethod
    def test_web():
        """
        Solves Wordle
        """

        found = False

        # set up the game
        web = Website()
        wc = WordsController(5)

        chosen = 'salet'

        for i in range(MAX_ATTEMPTS):

            # print(chosen)

            valid = False
            while not valid:
                try:
                    answer = wc.try_word(web, chosen)
                    valid = True
                except:
                    chosen = wc.choose_word()

            if answer != False:
                print(f'Complete in {i + 1} turns: the answer is {chosen}!')
                found = True
                return i + 1

            chosen = wc.choose_word()

        print(f'failure to find the word within {MAX_ATTEMPTS} steps')
        return False
