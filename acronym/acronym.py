import re

def abbreviate(words):
#    words_clean = re.sub("[\t\n,.:!-_&@$%^]|' | '|^'+|'+$", " ", words)
    words_clean = re.sub("[\t\n,.:!&@$%^_-]", " ", words)
    acronym = ""
    wrd_list = words_clean.split()
    for word in wrd_list:
        acronym += word[0].upper()
    return (acronym)

# Program tester
#while True:
#    string_to_abbreviate = input ("String to abbreviate: ")
#    if string_to_abbreviate == "done":
#         break
#    string_acronym = abbreviate(string_to_abbreviate)
#    print ("Acronym: ",string_acronym)

#print("=> End of program")
