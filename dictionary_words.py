#an algorithm that generates random sentences from words in a file
import random

''' This function accesses the word file, creates a list object, removes line breaks, and appends the words from the
file to the list, takes five words from the list object, stores them in an array, and joins the array
into a sentence before outputting it'''
def random_sentence():
    with open('/usr/share/dict/words') as file:
        words_list = []
        for word in file:
            word = word.rstrip("\n")
            words_list.append(word)
        word_array = random.choices(words_list, k=5)
        sentence = ' '.join(word_array) + '.'
        sentence = sentence.capitalize()
        print(sentence)


if __name__ == '__main__':
    random_sentence()
