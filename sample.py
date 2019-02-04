import random
import histogram 

# imports histogram function for use in random_word function
def import_text(text, file):
    with open(file) as f:
        text = histogram.histogram(f)
        return text

# a function that takes a histogram and returns a single random word
def random_word(sample):
   return
