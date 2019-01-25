#randomly rearrange a set of words; takes command-line arguments
import random
import sys

#the list of command line arguments the shuffle function will take
arguments = sys.argv[1:]

#This function randomly rearranges command line arguments when executed
def word_shuffle():
    random.shuffle(arguments)
    print(arguments)

word_shuffle()