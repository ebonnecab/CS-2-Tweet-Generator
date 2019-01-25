#TO DO: Create an algorithm that generates random sentences from words in a file.
import random
#access and read the file
file = open("testfile.txt", "r").readlines()
# store selected words into a list object
word = file[0]
#split the words in the list into individual strings
words = word.split()
#randomly choose words from the list
random_words = random.choices(words, k=4)
#put those random words together into a "Sentence"
sentence = ''.join(random_words)
#output the sentence
print(sentence)

# Issues: there are no spaces between the words. the words repeat themselves.
# had to put all the words on one line and I may need to access a multiline file