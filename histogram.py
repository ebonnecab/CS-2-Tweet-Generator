# uses histogram data structure to display word frequency, least/most frequent words, and how many unique words in a text
import random

#dictionary implementation
#TO DO: account for extraneous punctuation and numbers
'''
, 
words are added to dictionary from list and paired with how many times the word appears
'''
def histogram(file): 
    with open(file) as f: #access file
        dict = {} #creates a dictionary
        text = f.read() #reads file
    words_list = [word for line in text.split('\n') for word in line.split(' ')] #removes line breaks, split returns a list of individual words
    for word in words_list: #words and word frequency are added to dictionary from list
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

'''
shows results from histogram function in a new file by accessing text file, 
opening a new file and writing the key value pairs from the histogram into the new file
'''
#TO DO: figure out why it also changes original text file

def histo_file(file, histogram):
    with open(file, 'w+') as f:
        f.write('\n Histogram\n')
        for key, val in histogram.items():
            f.write('{}: {}\n'.format(key, val))

#histogram list implementation
def histogram_list():
    sample_sentence = "one fish two fish red fish blue fish"
    word_array = sample_sentence.split(" ")
    words_list = []
    for word in word_array:
        for index in words_list:
            if index[0] == word:
                index[1] += 1
        words_list.append([word, 1])
    return words_list
                

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
    print(histogram('siddhartha.txt'))
    # print(histogram_list())
    unique_words(histogram('siddhartha.txt'))
    frequency('he', histogram('siddhartha.txt'))
    # histo_file('histo.txt', histogram('siddhartha.txt')
 
        
