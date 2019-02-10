#an algorithm that generates random sentences from words in a file
#TO DO: refactor code to use randint
import random
import sys

# number = sys.argv[:1]
number = input('Enter number of words: ')
''' This function takes user input for number of words, accesses the word file, creates a list object, removes line breaks, 
and appends the words from the file to the list, takes five words from the list object, stores them in an array, 
and joins the array into a sentence before outputting it'''
def random_sentence():
    words_list = []
    with open('/usr/share/dict/words') as file:
            text = file.read().split()
            for word in text:
                # words_list.append(word)
                # rand_num = random.randint(0, len(text)-1)
                # rand_word = words_list[rand_num]
            
                # words_list.append(word)
                word = word.strip()
                words_list.append(word)  
                word_array = random.choices(words_list, k= int(number))
                sentence = ' '.join(word_array) + '.'
                sentence = sentence.capitalize()
            return sentence


if __name__ == '__main__':
  test = random_sentence()
  print(test)
