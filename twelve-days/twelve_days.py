def recite(start_verse, end_verse):
    song_verses_order = ["first ","second ","third ","fourth ","fifth ","sixth ","seventh ","eighth ","ninth ","tenth ","eleventh ","twelfth "]
    song_verses_compl = ["twelve Drummers Drumming, ",
                         "eleven Pipers Piping, ",
                         "ten Lords-a-Leaping, ",
                         "nine Ladies Dancing, ",
                         "eight Maids-a-Milking, ",
                         "seven Swans-a-Swimming, ",
                         "six Geese-a-Laying, ",
                         "five Gold Rings, ",
                         "four Calling Birds, ",
                         "three French Hens, ",
                         "two Turtle Doves, ",
                         "a Partridge in a Pear Tree."]

    try:
        if int (start_verse) > int (end_verse):
            return ("Error Fun Recite 1: start verse must be less or equal than end verse")
        elif int (start_verse) < 1 or int (start_verse > 12):
            return ("Error Fun Recite 2: start verse must be between 1 and 12")
        elif int (end_verse) < 1 or int (end_verse > 12):
            return ("Error Fun Recite 3: end verse must be between 1 and 12")
    except:
        return ("Error Fun Recite 4: at least one of the arguments is not an integer")

    song_piece = []
    current_verse = start_verse
    for vord in song_verses_order[start_verse-1:end_verse]:
        song_verse = "On the " + vord + "day of Christmas my true love gave to me: "
        c = 12-current_verse
        for vcomp in song_verses_compl[c:]:
            if current_verse > 1 and c == 11:
                song_verse += "and "
            song_verse += vcomp
            c += 1
        current_verse += 1
        song_piece.append(song_verse)

    return (song_piece)

# Program tester
#while True:
#    try:
#        start_ver = int (input ("Start Verse: "))
#    except:
#        print ("Error Prg 1: start verse not an integer")
#        break

#    try:
#        end_ver = int (input ("End Verse: "))
#    except:
#        print ("Error Prg 2: end verse not an integer")
#        break

#    song_piece = recite (start_ver, end_ver)
#    print (song_piece)

#print("=> End of program")
