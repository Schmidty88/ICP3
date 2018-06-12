#This function is used for counting vowels then
def VowelCount(Sentence):
#this set contains all the vowels we will be using if
#it sees a letter in the set it will add to the counter
    Vowel = set("aeiou")
    counter = 0
    for letter in Sentence:
        if letter in Vowel:
            counter += 1
    print("Vowels in String " + str(counter))
Sentence = input("Please Enter A Sentence:")
VowelCount(Sentence)
