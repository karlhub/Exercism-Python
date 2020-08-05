def latest(scores):
#    print(type(scores))

    try:
        lenSco=len(scores)
    except:
        return("Not a list")
    if lenSco==0:
        return("Empty list")
    return scores[-1]

#    try:
#        lenSco=len(scores)
#    except:
#        return("Not a list")
#    if lenSco==0:
#        return("Empty list")
#    latestSco=scores[lenSco-1]
#    return(latestSco)

def personal_best(scores):
#    print(type(scores))

    try:
        lenSco=len(scores)
    except:
        return("Not a list")
    if lenSco==0:
        return("Empty list")
    return max(scores)

# Original solution
#    try:
#        lenSco=len(scores)
#    except:
#        return("Not a list")
#    if lenSco==0:
#        return("Empty list")
#    scores.sort()
#    bestSco=scores[lenSco-1]
#    return(bestSco)

def personal_top_three(scores):
#    print(type(scores))

    try:
        lenSco=len(scores)
    except:
        return("Not a list")
    return sorted(scores, reverse=True)[:3]

# Original solution
#    try:
#        lenSco=len(scores)
#    except:
#        return("Not a list")
#    if lenSco==0:
#        return("Empty list")
#    scores.sort()
#    pos=0
#    lstTop3=list()
#    while True:
#        pos+=1
#        if pos>lenSco or pos>3:
#            break
#        lstTop3.append(scores[lenSco-pos])
#    return(lstTop3)

# Program tester
lstScores=list()
while True:
    print("Current list: ",lstScores)
    score=input("Enter score: ")
    if score=="done":
         break
    try:
        lstScores.append(int(score))
    except:
        print("Not an integer")

latestScore=latest(lstScores)
print("Latest Score: ",latestScore)

bestScore=personal_best(lstScores)
print("Best Score: ",bestScore)

top3Scores=personal_top_three(lstScores)
print("Top 3 Scores: ",top3Scores)

print("=> End of program")
