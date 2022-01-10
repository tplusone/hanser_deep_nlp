import numpy as np
import pandas as pd

class SequenceEncoder:
    
    def __init__( self, x: np.array, 
                        y: np.array, 
                        filler='\t'):
        if len(y) != len(x):
            raise ValueError('x and y must have same length!')
        self.y = y
        self.x = x
        self.filler = filler
        self.__variables_one_hot_encoding()
        self.__variables_target()

    def gen_feature_target_data(self):
        X = self.gen_one_hot_data(self.x)
        y = np.array([self.word_to_int(word) for word in self.y])
        return X, y
    
    def gen_one_hot_data(self, data: np.array):
        one_hot_data = np.zeros(shape=(len(data), 
                                self.max_word_length, 
                                len(self.char_idx)))
        for idx, word in enumerate(data):
            for i, char in enumerate(word):
                if char in self.char_idx:
                    one_hot_data[idx, i, self.char_idx[char]] = 1
            for i in range(len(word), self.max_word_length):
                one_hot_data[idx, i, self.char_idx[self.filler]] = 1
        return one_hot_data

    def one_hot_to_word(self, one_hot: np.array):
        word = []
        for col in one_hot:
            idx = np.argmax(col)
            word.append(self.idx_char[idx])
        return ''.join(word)
    
    def int_to_word(self, word_int: int):
        return self.idx_word[word_int]

    def word_to_int(self, word: str):
        return self.word_idx[word]

    def __variables_one_hot_encoding(self):
        self.max_word_length = len(max(self.x, key=len))
        self.__gen_charset()
        self.char_idx = dict([(char, idx) for idx, char in enumerate(self.charset)])
        self.idx_char = dict([(idx, char) for idx, char in enumerate(self.charset)])

    def __variables_target(self):
        target_word_list = sorted(list(set(self.y.tolist())))
        self.word_idx = dict([word, i] for i, word in enumerate(target_word_list))
        self.idx_word = dict([i, word] for i, word in enumerate(target_word_list))

    def __gen_charset(self):
        charset = set()
        for word in self.x:
            for char in word:
                charset.add(char)
        charset = list(charset)
        charset.sort()
        if self.filler in charset:
            raise ValueError('x contains filler!')
        else:
            charset.append(self.filler)
        self.charset = charset