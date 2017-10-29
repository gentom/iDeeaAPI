#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from gensim.models import word2vec

model = word2vec.Word2Vec.load('./model/wiki_jpn')

def iDeea(word):
    words = model.most_similar([word])
    wordList = [words[i][0] for i in range(len(words))]
    return wordList

# test
if __name__ == '__main__':
    print(iDeea('サッカー'))