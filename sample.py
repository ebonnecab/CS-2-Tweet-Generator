import random
import sys
#TO DO: add comments

def sample():
    sample_sentence = sys.argv
    words_list = sample_sentence.split()
    dict = histogram(words_list)

    word_count = len(words_list)
    chance = 0
    random_num = random.random()
    for key, val in dict.items():
        print("{} = {}".format(key,val/word_count))

    #returns random word    
    for key in dict:
        chance += dict[key]/word_count
        if chance > random_num:
            return key

  
def histogram(word_array):
    histogram = {}
    
    for word in word_array:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1

    return histogram

#tests accuracy of probability results
def word_probability():
    dict = {'one': 0, 'fish': 0, 'two': 0, 'red': 0, 'blue': 0}
    for i in range(0, 50):
        dict[sample()] +=1
    return dict
    


if __name__ == '__main__':   
    test = sample()
    print(test)
    test2 = word_probability()
    print(test2)

    
