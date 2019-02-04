# uses histogram data structure to display word frequency, least/most frequent words, and how many unique words in a text
import random

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

#histogram list implementation
#TO DO: show how many times each word occurs as a list inside of this list
'''
accesses file, creates an empty list, reads file, appends words to list, shows frequency of each word in list
 '''
def histogram_list(file):
    with open(file) as f:
        histogram = []
        text = f.read()
        words_list = [word for line in text.split('\n') for word in line.split(' ')]
        for word in words_list:
            histogram.append(word)

        return histogram

#histogram tuples implementation
#TO DO: add word and word frequency to tuples in histogram list
def histogram_tuples(file):
    with open(file) as f:
        histogram = []
        text = f.read()
        words_list = [word for line in text.split('\n') for word in line.split(' ')]
        for word in words_list:
            return




if __name__ == '__main__':
    histogram('siddhartha.txt')
    # print(histogram_list('siddhartha.txt'))
    unique_words(histogram('siddhartha.txt'))
    frequency('he', histogram('siddhartha.txt'))
 
        
