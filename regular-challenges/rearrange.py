#randomly rearrange a set of words; takes command-line arguments
import random
import sys

#the list of command line arguments the shuffle function will take
word_array = sys.argv[1:]

def word_shuffle():
    for index in range(len(word_array) -1, 0, -1): #this function accesses the index of the arguments
        random_index = random.randint(0, index) #picks a random index number between 0 and the length of the array
        word_array[index] = word_array[index].lower() #converts each string in the array to lowercase
        word_array[index], word_array[random_index] = word_array[random_index], word_array[index] # swaps the original index for a random index

    #joining words from array into a sentence
    sentence = ' '.join(word_array) + '.'
    sentence = sentence.capitalize()
    return sentence

if __name__ == '__main__':
    word_shuffle()
