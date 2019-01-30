#an algorithm that generates random sentences from words in a file.
import random

#access and read the file
with open('/usr/share/dict/words') as file:

#created a list object, removed line breaks, and appended words from file
    words_list = []
    for words in file:
        words = words.rstrip("\n")
        words_list.append(words)

#took four words from list object and stored them in an array
word_array = random.choices(words_list, k=4)

#joining words from array into a sentence
sentence = ' '.join(word_array) + '.'
sentence = sentence.capitalize()

#output of sentence
print(sentence)

