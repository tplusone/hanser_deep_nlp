# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 14:01:06 2021

@author: jochen hirschle
"""
import os
from os.path import join
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.tokenize import word_tokenize

import os
dir = os.path.dirname(__file__)
path = os.path.join(dir, '../Data')

### Daten laden ###
def get_data():
    data = joblib.load(join(path, 'data_phrases.pkl'))
    german = [ el[1] for el in data]
    english = [ el[0] for el in data]
    return german, english


### 2) Zeitversetzte Eingabe produzieren (für Teacher Force)
def insert_start_sign( data: list, start='<start>'):
    new_data = []
    for phrase in data:
        phrase = start + " " + phrase
        new_data.append(phrase)
    return new_data

def load_tokenizer():
    tok_de = joblib.load(join(path, 'tok_de_trans.pkl'))    
    tok_en = joblib.load(join(path, 'tok_en_trans.pkl'))    
    return tok_de, tok_en

def load_data(new_tokenizer=False):
    X, y = get_data()
    X2 = insert_start_sign(y)
    print(X[:5], X2[:5], y[:5])

    ### 3) Sequences erstellen
    if new_tokenizer:
        filters = '!"#$%&()*+,-./:;=?@[\\]^_`{|}~\t\n'
        tok_en, tok_de = Tokenizer(filters=filters), Tokenizer(filters=filters)
        tok_de.fit_on_texts(X)
        tok_en.fit_on_texts(X2)
        ####
        joblib.dump(tok_de, join(path, 'tok_de_trans.pkl'))
        joblib.dump(tok_en, join(path, 'tok_en_trans.pkl'))
    else:
        tok_de = joblib.load(join(path, 'tok_de_trans.pkl'))    
        tok_en = joblib.load(join(path, 'tok_en_trans.pkl'))
    
    X1_ = tok_de.texts_to_sequences(X)
    X2_ = tok_en.texts_to_sequences(X2)
    y_ = tok_en.texts_to_sequences(y)
    print(X1_[:5], X2_[:5], y_[:5])
    
    ### Maxlength
    len_german = 0
    for el in X1_:
        if len(el) > len_german:
            len_german = len(el)
    print('max length german', len_german)
    ### Maxlength
    len_english = 0
    for el in y_:
        if len(el) > len_english:
            len_english = len(el)
    print('max length english', len_english)

    X1_pad = pad_sequences(X1_, maxlen=len_german,
                                padding='post',
                                truncating='post')
    X2_pad = pad_sequences(X2_, maxlen=len_english,
                                padding='post',
                                truncating='post')
    y_pad = pad_sequences(y_, maxlen=len_english, 
                              padding='post',
                              truncating='post')
    
    return X1_pad, X2_pad, y_pad


if __name__ == '__main__':

    X1_pad, X2_pad, y_pad = load_data()
    X1_pad.shape, X2_pad.shape, y_pad.shape

    X, y = get_data()
    print(X[:3], y[:3])
    tok_de, tok_en = load_tokenizer()
    X_pad = tok_de.texts_to_sequences(X[:3])
    tok_de.sequences_to_texts(X_pad)
    
