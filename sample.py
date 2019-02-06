import random
import histogram

''' 
This function takes a list of words, splits them into their own string separated by whitespace,
creates a word count based upon the length of the list, creates a dictionary, iterates through the list and adds the word and word count to the dictionary,
returns the probability of each word being chosen
'''
def word_probability(words_list):
    words_list = words_list.split(" ")
    word_count = len(words_list)
    dict = {}

    for word in words_list:
       dict[word] = words_list.count(word)
    
    for key, value in dict.items():
        print("{} : {}".format(key, value/word_count))

# random word function
def random_word(file):
    words_list = []
    histo = histogram.histogram(file)
    for word in histo:
        words_list.append(word)
        rand_num = random.randint(1, len(histo)-1)
    return words_list[rand_num]

if __name__ == '__main__':   
    words = "one fish two fish red fish blue fish"
    word_probability(words)
    
