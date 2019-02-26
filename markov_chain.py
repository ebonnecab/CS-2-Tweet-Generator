def markov_chain(sentence):
    markov_dict = {}
    word_array = sentence.split()

    for word in word_array:
        if word not in markov_dict.keys():
            markov_dict[word] = {}
            

    index = 0
    for word in word_array:
        if index + 1 < len(word_array):
            next_word = word_array[index+1]
            if next_word in markov_dict[word].keys():
                markov_dict[word][next_word]+= 1
            else:
                markov_dict[word][next_word] = 1
            index += 1
    return markov_dict

if __name__ == '__main__':
    print(markov_chain("one fish two fish red fish blue fish"))