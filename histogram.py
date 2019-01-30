# uses histogram data structure to display word frequency, least/most frequent words, and how many unique words in a text
import random
import string

# access siddharta file, store the words in an array, appends the array to the dictionary
def histogram():
    with open('siddhartha.txt') as file:
        text = file.readlines()
        print(text)
            

if __name__ == '__main__':
    histogram()     
        
