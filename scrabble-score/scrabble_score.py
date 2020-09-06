def score(word):
    dct = {"a":1,"b":3,"c":3,"d":2,"e":1,"f":4,"g":2,"h":4,"i":1,"j":8,"k":5,"l":1,"m":3,"n":1,"o":1,"p":3,"q":10,"r":1,"s":1,"t":1,"u":1,"v":4,"w":4,"x":8,"y":4,"z":10}
    wrd = word.lower()
    val = 0
    for letter in wrd:
        val += dct.get(letter,0)
    return (val)

# Program tester
#while True:
#    word_scrab = input ("Word to compute: ")
#    if word_scrab == "done":
#         break
#    score_scrab = score(word_scrab)
#    print ("Scrabble score: ",score_scrab)

#print("=> End of program")
