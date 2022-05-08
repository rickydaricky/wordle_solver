from english_words import english_words_alpha_set
from website import Website
from game import Game
import random
import collections


class WordsController():
    """
    Class for choosing and managing the words to choose
    """

    def __init__(self, word_length):
        self.word_length = word_length
        self.word_options = []

        # keep all the words that are of the word length
        for word in english_words_alpha_set:
            if len(word) == word_length:
                self.word_options.append(word)

        # dictionary of word indexes representing the known word, each key-value pair is (index, str)
        self.known_location_options = collections.defaultdict(str)
        for i in range(word_length):
            self.known_location_options[i] = ''

        # a dictionary, with each key value pair being letter: [wrong_indexes]
        self.unknown_location_options = {}

        # list of all the letters that aren't in the word
        self.known_wrong_options = set()

        # self.options = {'a': [], 'b': [], 'c': [], 'd': (), 'e': (), 'f': (), 'g': (), 'h': (), 'i': (), 'j': (), 'k': (), 'l': (), 'm': (), 'n': (), 'o': (), 'p': (
        # ), 'q': (), 'r': (), 's': (), 't': (), 'u': (), 'v': (), 'w': (), 'x': (), 'y': (), 'z': ()}   # dictionary representing information about each letter, each list representing a position the word could be in

    @staticmethod
    def valid_known_wrong(known_wrong_options, word):
        """
        Determines if the word has any of the letters in known_wrong_options

        Params:
        known_wrong_options: list of all the letters that aren't in the word
        word: the word to test
        Returns: True is the word does not violate the rule, False if it does
        """

        for letter in known_wrong_options:
            if letter in word:
                return False

        return True

    @staticmethod
    def valid_known_locations(known_location_options, word):
        """
        Determines if the word passes the known_locations test, aka whether, for every letter we know is in a specific position, the word also has that in the position

        Params:
        known_location_options: a list of tuples, with each tuple being (letter, [not_index_in_word])
        word: the word to test against
        Returns: True is the word does not violate the rule, False if it does
        """

        for index, letter in known_location_options.items():
            if word[index] != letter:
                return False

        return True

    @staticmethod
    def valid_unknown_locations(unknown_location_options, word):
        """
        Determines if the word passes the unknown_locations test, aka whether, for every letter we know is in a specific position, the word also has that in the position

        unknown_location_options: a dictionary, with each key value pair being letter: [wrong_indexes]
        word: the word to test
        Returns: True if the word does not violate the rule, False if it does
        """

        temp_word = word

        for letter, wrong_indexes in unknown_location_options.items():
            if letter not in temp_word or word.index(letter) in wrong_indexes:
                return False
            else:
                temp_word.remove(letter)

        return True

    def choose_word(self):
        """
        From the remaining word_options, pick a random word that fits the conditions

        Params:
        Returns: string word
        """

        # filter for letters that don't exist
        self.word_options[:] = [x for x in self.word_options if self.valid_known_wrong(
            self.known_wrong_options, x)]

        print()

        # filter for known letters with known locations
        self.word_options[:] = [x for x in self.word_options if self.valid_known_locations(
            self.known_location_options, x)]

        # filter for known letters with unknown locations
        self.word_options[:] = [x for x in self.word_options if self.valid_unknown_locations(
            self.unknown_location_options, x)]

        # pick a random word from the remaining options
        chosen_word = random.choice(self.word_options)

        return chosen_word

    def update_info(self, new_wrong, new_unknown, now_known):
        """
        Updates the model info using the current word

        Params:
        new_wrong: a list of letters representing things you newly learned are wrong
        new_unknown: list of tuples, with each tuple being (letter, wrong_index)
        now_known: list of tuples, with each tuple being (letter, index_in_word)
        """

        # update known_wrong_options
        self.known_wrong_options = self.known_wrong_options.union(new_wrong)

        # update known_location_options

        for letter, index_in_word in now_known: 
            self.known_location_options[index_in_word] = letter

        # update unknown_location_options
        for letter, _ in now_known:
            if letter in self.unknown_location_options:
                self.unknown_location_options.pop(letter)

        for letter, wrong_index in new_unknown:
            self.unknown_location_options[letter].append(wrong_index)

    def try_word(self, web, word):
        """
        Tries the word with the game and updates the object accordingly

        web: an instance of the site we're running on
        word: the word to try
        Returns: either a word if we found the final word, or False to indicate the word has not been fully found yet
        """

        answer = ['_' for _ in range(self.word_length)]

        # web.attempt_word(word)
        new_wrong, new_unknown, now_known = web.check_recent_board(word)
        self.update_info(new_wrong, new_unknown, now_known)

        for index, letter in self.known_location_options.items():
            if letter == '':
                return False
            else:
                answer[index] = letter

        return ''.join(answer)
