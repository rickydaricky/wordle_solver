from game import Game
from words import WordsController

MAX_ATTEMPTS = 6


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

        # set up the game
        game_board = Game(correct_word)
        wc = WordsController(5)

        chosen = 'salet'

        for i in range(MAX_ATTEMPTS):
            print(chosen)

            answer = wc.try_word(game_board, chosen)
            if answer != False:
                print(f'complete in {i + 1} turns!')
                break

            # print(wc.known_location_options)
            # print(wc.unknown_location_options)

            chosen = wc.choose_word()
            print('\n')
