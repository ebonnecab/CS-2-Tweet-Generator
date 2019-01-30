#an algorithm that generates random sentences from words in a file.
import random
''' This function accesses the word file, creates a list object, removes line breaks, and appends the words from the
file to the list'''
def random_sentence():
#access and read the file
    with open('/usr/share/dict/words') as file:
#created a list object, removed line breaks, and appended words from file
        words_list = []
        for words in file:
            words = words.rstrip("\n")
            words_list.append(words)
#took four words from list object and stored them in an array
        word_array = random.choices(words_list, k=5)
#joining words from array into a sentence
        sentence = ' '.join(word_array) + '.'
        sentence = sentence.capitalize()
#output of sentence
        print(sentence)


if __name__ == '__main__':
    random_sentence()
