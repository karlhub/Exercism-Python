# Optional parameters are specified by assigning a default value when defining the function
def two_fer(name="you"):
    if name is None:
        x="you"
    elif name=="":
        x="you"
    else:
        x=name
    str="One for "+x+", one for me."
    return(str)

# Program tester
#while True:
#    strName=input("Name: ")
#    if strName=="done":
#         break
#    strRes=two_fer(strName)
#    print("Result: ",strRes)
#    strRes=two_fer()
#    print("Result: ",strRes)
#print("Done!")
