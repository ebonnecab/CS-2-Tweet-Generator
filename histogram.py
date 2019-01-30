# uses histogram data structure to display word frequency, least/most frequent words, and how many unique words in a text
import random
import string

'''access siddharta file, store the words in a string, cleans out punctuation and line breaks, converts string to lowercase,
split returns a list of individual words'''
def histogram():
    with open('siddhartha.txt') as file:
        text = file.readlines()
        for char in '-.,\n':
            text = [item.replace(char, ' ') for item in text]
        text = [item.lower().split() for item in text]
        dict = {}
        for word in range(len(text)-1, 0, -1):
            dict[word] = text[word]
       
        return dict     

if __name__ == '__main__':
    histogram()     
        
