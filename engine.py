#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, session
import json
from flask_socketio import SocketIO
from gensim.models import word2vec
import sys
import MeCab

async_mode = None
app = Flask(__name__)
socketio = SocketIO(app, async_mode = async_mode)
thread = None

# Model Loading
model = word2vec.Word2Vec.load('./model/jp_wiki')
m = MeCab.Tagger("-Owakati")

@app.route("/", methods=['POST'])
def iDeea():
    if request.method == "POST":
        word = request.form['word']
        words = m.parse(word)
        words = words.split(' ')
        print('---------')
        print(len(words), words)
        print(words[0])
        print(words[1])

        if len(words) > 2:
            words = model.most_similar(positive=[words[0], words[1]])
        else:
            words = model.most_similar([words[0]])
            
        wordList = [words[i][0] for i in range(len(words))]
        wordList_json = json.dumps(wordList, ensure_ascii=False)
        return wordList_json
'''
def iDeea():
    if request.method == "POST":
        word = request.form['word']
        print(word)
        words = model.most_similar([word])
        wordList = [words[i] for i in range(len(words))]
        print(wordList)
        wordList = [words[i][0] for i in range(len(words))]
        wordList_json = json.dumps(wordList, ensure_ascii=False)
        return wordList_json
'''

if __name__ == "__main__":
    #app.run(debug=True, port=8000)
    socketio.run(app, debug=True, port=8000)