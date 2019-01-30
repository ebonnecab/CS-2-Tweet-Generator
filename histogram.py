# uses histogram data structure to display word frequency, least/most frequent words, and how many unique words in a text
import random

def histogram():
    with open('siddhartha.txt') as file:
        words_list = []
        for word in file:
            word = word.rstrip('\n').lower().split()
            words_list.append(word)

            dict = {'word': []}
            dict['word'].append(words_list)
            print(dict['word'])
            

histogram()       
        
