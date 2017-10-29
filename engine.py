#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.models import word2vec

# Word2Vec
# return words

# call the model
model = word2vec.Word2Vec.load('wiki_jpn') # there is no model yet.

def ideea(word):
    model.most_similar(word)
    return model[word]