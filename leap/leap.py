def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Program tester
#while True:
#    try:
#        year = int (input ("Year: "))
#    except:
#        break
#    print (leap_year(year))

#print("=> End of program")
