# uses histogram data structure to display word frequency, least/most frequent words, and how many unique words in a text
import random
import string

#dictionary implementation
#TO DO: account for extraneous punctuation and numbers
'''
access file, creates a dictionary, reads file, removes line breaks, split returns a list of individual words, 
words are added to dictionary from list and paired with how many times the word appears
'''
def histogram(file):
    with open(file) as f:
        dict = {}
        text = f.read()
        words_list = [word for line in text.split('\n') for word in line.split(' ')]
        for word in words_list:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
        return dict

#takes histogram data and returns number of unique words
def unique_words(histogram):

    return len(histogram)

'''
checks histogram for word frequency by returning the key value pairs. if word is not in histogram, it returns
an error message prompting the user to try again
'''
def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    else:
        return "That word is not in the histogram. Please try again"

    


if __name__ == '__main__':
   print(histogram('siddhartha.txt'))
   print(unique_words(histogram('siddhartha.txt')))
   print(frequency('she', histogram('siddhartha.txt')))
 
        
