#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from gensim.models import word2vec

model = word2vec.Word2Vec.load('./model/wiki_jpn')

def iDeea(word):
    return model.most_similar([word])

if __name__ == '__main__':
    words = iDeea('日本')
    print(words)