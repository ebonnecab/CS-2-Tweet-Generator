import random
import histogram 

# imports histogram function for use in random_word function
def import_sample(sample, file):
    with open(file) as f:
        sample = histogram.histogram(f)
        return sample

# a function that takes a histogram and returns a single random word
def random_word():
   return
