#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import socket
import urllib
import json
import engine
import sys

app = Flask(__name__)

wordList = []

@app.route("/", methods=['POST'])
def iDeeaServer():
    if request.method == "POST":
        word = request.form['word']
        print(word)
        wordList = engine.iDeea(word)
        print(wordList)
        wordList_json = json.dumps(wordList, ensure_ascii=False)
        return wordList_json
        #return word

if __name__ == "__main__":
    app.run(debug=True, port=8000)