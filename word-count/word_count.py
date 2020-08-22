import re
import string

def count_words(sentence):

    sentence = re.sub("[\t\n,.:!_&@$%^]|' | '|^'+|'+$", " ", sentence.lower())
# string.punctuation -> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    words = sentence.split()
    d = dict()
    for word in words:
        d[word] = d.get(word,0) + 1

    return (d)

# Program tester
#while True:
#    stringWords = input ("Sentence to count words: ")
#    if stringWords == "done":
#         break
#    dictWords = count_words(stringWords)
#    print ("Words counter: ",dictWords)

#print("=> End of program")
