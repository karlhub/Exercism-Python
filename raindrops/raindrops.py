def convert(number):
    try:
        inumber=int(number)
    except:
        return("Not a number")
#        raise Exception("Parameter is not a number or cannot be transformed into an integer")
    strdrop=""
    if inumber%3 == 0:
        strdrop=strdrop+"Pling"
    if inumber%5 == 0:
        strdrop=strdrop+"Plang"
    if inumber%7 == 0:
        strdrop=strdrop+"Plong"
    if strdrop=="":
        strdrop=str(inumber)
    return(strdrop)

# Program tester
#while True:
#    strNumber=input("Number: ")
#    if strNumber=="done":
#         break
#    strdropRes=convert(strNumber)
#    print("Result: ",strdropRes)
#print("Done!")
