from flask import Flask
import os
from dictionary_words import random_sentence
app = Flask(__name__)

@app.route('/')
def hello_world():
    rando_sentence = random_sentence()
    return rando_sentence


if __name__ == '__main__':  
    hello_world()
