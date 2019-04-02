from histogram import histogram
from dictogram import Dictogram
import random


def markov_chain(file):
    with open(file) as f: #access file
        markov_dict = {} #creates empty dictionary
        text = f.read() #reads file
    word_array = [word for line in text.split('\n') for word in line.split(' ')] #removes line breaks and whitespace,returns a list of individual words

    for word in word_array:
        if word not in markov_dict:
            markov_dict[word] = {}

    index = 0
    if index + 1 < len(file):
        next_word = file[index+1]
        if next_word in markov_dict[word].keys():
            markov_dict[word][next_word] += 1
        else:
            markov_dict[word][next_word] = 1
        index +=1
    print(index)
    return markov_dict

def start_word(markov_dict, word):
    rand_word = random.choice(list(markov_dict.keys()))
    return rand_word

def generate_sentences(markov_dict):
    length = 10
    first_word = list(markov_dict.keys())[0]
    second_word = start_word(markov_dict, first_word)
    sentence = first_word + ' ' + second_word + ' '
    prev_word = second_word

    for word in range(0, random.randint(1, length)):
        next_word = start_word(markov_dict, prev_word)
        prev_word = next_word
        sentence += next_word + ' '
    return sentence


def second_order(file):
    with open(file) as f: #access file
        text = f.read() #reads file
        markov_dict = {} #creates empty dictionary
    word_array = [word for line in text.split('\n') for word in line.split(' ')] #removes line breaks and whitespace,returns a list of individual words

    for index in range(len(word_array) -2):
        start_word = word_array[index]
        next_word = word_array[index + 1]
        next_next_word = word_array[index + 2]
        tuple = (start_word, next_word)
        
        if tuple not in markov_dict:
           add_tuple = Dictogram([next_next_word])
           markov_dict[tuple] = add_tuple
        else:
            markov_dict[tuple].add_count(next_next_word)
    return markov_dict

def second_order_sentence(markov_dict):
    tuple = list(markov_dict.keys())[0]
    next_next_word = start_word(markov_dict, tuple)
    sample_sentence = tuple[0] + tuple[1] + next_next_word
    prev_word = (tuple[1], next_next_word)

    length = 10
    for word in range(0, random.randint(1, length)):
        new_word = start_word(markov_dict, prev_word)
        prev_word = (prev_word[1], new_word)
        sample_sentence += new_word
        if prev_word not in markov_dict:
            return sample_sentence
    
    return sample_sentence



    

if __name__ == '__main__':
    chain = markov_chain('siddhartha.txt')
    print(generate_sentences(chain))
    # second_chain = second_order('siddhartha.txt')
    # print(second_order_sentence(second_chain))
    