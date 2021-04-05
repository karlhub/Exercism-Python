def response(hey_bob):

    # Remove any leading and trailing characters (space is the default)
    hey_bob = hey_bob.strip()
    # Check whether hey_bob is an empty string or not
    if hey_bob:
        # hey_bob is not an empty string
        if hey_bob.endswith("?"):
            # hey_bob ends with "?"
            if hey_bob.isupper():
                # hey_bob has letters and all of them are in uppercase
                return "Calm down, I know what I'm doing!"
            # hey_bob ens with "?" but has no capital letters
            return 'Sure.'
        elif hey_bob.isupper():
            # hey_bob is not a question and has all letters in uppercase (YELL)
            return "Whoa, chill out!"
        # hey_bob is neither a question, nor a yell.
        return 'Whatever.'
    # hey_bob is an empty string
    return 'Fine. Be that way!'

# Program tester
#while True:
#    hey_bob = input("Sentence for Bob: ")
#    if hey_bob == "done":
#         break
#    print (response(hey_bob))

#print("=> End of program")
