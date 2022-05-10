class Game():
    """
    Class for the internal Wordle simulator for testing purposes
    """

    def __init__(self, correct_word):
        self.correct_word = correct_word

    def check_recent_board(self, attempted_word):
        """
        Checks the most recent results after attempting a word and returns the necessary information to the user
        
        Params:
        attempted_word: the word you're trying
        Returns: a tuple of new_wrong, new_unknown, and new_known
        """

        # new_wrong: a list of letters representing things you newly learned are wrong
        new_wrong = []

        # new_unknown: list of tuples, with each tuple being (letter, wrong_index)
        new_unknown = []

        # now_known: list of tuples, with each tuple being (letter, correct_index)
        now_known = []
        
    
        for i in range(len(attempted_word)):
            if attempted_word[i] in self.correct_word:
                if self.correct_word[i] == attempted_word[i]:
                    now_known.append((attempted_word[i], i))
                else:
                    new_unknown.append((attempted_word[i], i))
            else:
                new_wrong.append(attempted_word[i])

        return new_wrong, new_unknown, now_known
