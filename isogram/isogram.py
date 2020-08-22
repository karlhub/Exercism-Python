def is_isogram(string):
    str=string.lower()
    d=dict()
    for c in str:
        d[c] = d.get(c,0)+1
        if c != " " and c != "-" and d[c] > 1:
            return (False)
    return (True)

# Program tester
#while True:
#    stringIso = input ("String to analyze: ")
#    if stringIso == "done":
#         break
#    resIso = is_isogram(stringIso)
#    print ("Is Isogram? ",resIso)

#print("=> End of program")
