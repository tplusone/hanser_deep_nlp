
import numpy as np

class SpellingMistake:

    def __init__(self):
        self.alphabet = [word for word in 'abcdefghijklmnopqrstuvwxyzßäöü']
    
    def gen_misspelling(self, words: np.array):
        spellings = []
        for word in words:
            word = str(word)
            rand_num = np.random.randint(0,6)
            if rand_num == 0:
                mistake = self.__random_char_exchange(word, add=True)
            if rand_num==1 or rand_num==2:
                mistake = self.__char_dublication(word)
            else:
                mistake = self.__random_char_exchange(word)
            if len(word) > 5 and np.random.randint(0,10) == 0:
                mistake = self.__random_char_exchange(mistake)
            spellings.append(mistake)
        return np.array(spellings)

    def __char_dublication(self, word):
        idx = np.random.randint(0,len(word))
        char = word[idx]
        if idx==len(word)-1:
            mistake = word + char
        else:
            mistake = word[:idx] + char + word[idx:]
        return mistake

    def __random_char_exchange(self, word, add=False):
        char = self.alphabet[np.random.randint(0,len(self.alphabet))]
        idx = np.random.randint(0,len(word))
        if not add:
            if idx==len(word)-1:
                mistake = word[:idx] + char
            else:
                mistake = word[:idx] + char + word[idx+1:]
        else:
            if idx==len(word)-1:
                mistake = word + char
            else:
                mistake = word[:idx] + char + word[idx:]
        return mistake