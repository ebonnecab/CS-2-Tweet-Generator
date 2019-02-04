import random
import histogram 

# imports histogram for use in random_word function
def import_text(histo, file):
    with open(file) as f:
        histo = histogram.histogram(f)
        return histo

# a function that takes a histogram and returns a single random word
def random_word(sample):
   return
