##This is code one for ICP 3
#Fucntion for the word count so we can call it later for our input
def WordCount(sentence):

    dictionary = dict()

#this for loop is spliting the words then counting them
#if it has been counted before it adds if not it starts a new count
    for word in sentence.split():
        word = word.lower()
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

sentence = input("Please Enter a Sentence")
print(WordCount(sentence))


