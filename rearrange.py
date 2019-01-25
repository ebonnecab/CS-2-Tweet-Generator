#TO-DO: randomly rearrange a set of words; takes command-line arguments
import random
import sys

def word_shuffle():
    random.shuffle(sys.argv)
    print(str(sys.argv))

word_shuffle()