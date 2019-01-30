#randomly rearrange a set of words; takes command-line arguments
import random
import sys

#the list of command line arguments the shuffle function will take
word_array = sys.argv[1:]

"""" this function accesses the index of the arguments, picks a random index number between 0 and the length of the array,
converts each string in the array to lowercase, swaps the original index for a random index, and joins them into
a "sentence". """

def word_shuffle():
    for index in range(len(word_array) -1, 0, -1):
        random_index = random.randint(0, index)
        word_array[index] = word_array[index].lower()
        word_array[index], word_array[random_index] = word_array[random_index], word_array[index]

    #joining words from array into a sentence
    sentence = ' '.join(word_array) + '.'
    sentence = sentence.capitalize()
    print(sentence)

if __name__ == '__main__':
    word_shuffle()
