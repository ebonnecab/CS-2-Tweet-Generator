from histogram import histogram

def markov_chain(file):
    with open(file) as f: #access file
        markov_dict = {} #creates empty dictionary
        text = f.read() #reads file
    word_array = [word for line in text.split('\n') for word in line.split(' ')] #removes line breaks and whitespace,returns a list of individual words

    for word in word_array:
        if word not in markov_dict:
            markov_dict[word] = {}

    index = 0
    if index + 1 < len(file):
        next_word = file[index+1]
        if next_word in markov_dict[word].keys():
            markov_dict[word][next_word] += 1
        else:
            markov_dict[word][next_word] = 1
        index +=1
    
    return markov_dict

if __name__ == '__main__':
    print(markov_chain('siddhartha.txt'))