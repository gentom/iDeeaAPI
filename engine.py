#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, session
import json
from flask_socketio import SocketIO
from gensim.models import word2vec
import sys

async_mode = None
app = Flask(__name__)
socketio = SocketIO(app, async_mode = async_mode)
thread = None

model = word2vec.Word2Vec.load('./model/jp_wiki')

@app.route("/", methods=['POST'])
def iDeeaServer():
    if request.method == "POST":
        word = request.form['word']
        print(word)
        words = model.most_similar([word])
        wordList = [words[i][0] for i in range(len(words))]
        print(wordList)
        wordList_json = json.dumps(wordList, ensure_ascii=False)
        return wordList_json

@app.route("/merge", methods=['POST'])
def MergeX():
    if request.method == "POST":
        word = request.form['word']
        # mecabで分かち書き
        # 二つの単語に分割
        # Word2Vecにて二つの単語の加算

if __name__ == "__main__":
    #app.run(debug=True, port=8000)
    socketio.run(app, debug=True, port=8000)