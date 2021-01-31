def is_valid(isbn):

    # Remove "-"
    isbn_str = isbn.replace("-","")

    # Validate length without "-" is 10
    if len(isbn_str) != 10:
        return False

    # Validate first 9 positions are numbers and last one is number or "X"
    if isbn_str[:9].isnumeric() == False or isbn_str[-1].replace("X","10").isnumeric() == False:
        return False

    # Calculate checksum
    check = sum([int(pair[0]) * pair[1] for pair in zip(isbn_str[:-1], range(10,1,-1))]) + int(isbn_str[-1].replace("X","10"))

    # Validate checksum
    return (check % 11 == 0)

# Program tester
#while True:
#    isbn = input("ISBN: ")
#    if isbn == "done":
#         break
#    print (is_valid(isbn))
#
#print("=> End of program")
