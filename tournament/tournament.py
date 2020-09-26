def tally(rows):
    rk = dict()
    for row in rows:
        # Row format: team_name1;teamname2;win/loss/draw
        row = row.split(';')
        # Retrieve ranking for both teams. In case of first result, initial ranking is [0,0,0,0,0]
        team1 = rk.get(row[0],[0,0,0,0,0])
        team2 = rk.get(row[1],[0,0,0,0,0])
        result = row[2]
        # Increase number of matches played for both teams
        team1[0] += 1 # +1 MP
        team2[0] += 1 # +1 MP
        if result == "win":
            team1[1] += 1 # +1 Win
            team1[4] += 3 # +3 points
            team2[3] += 1 # +1 Loss
        elif result == "loss":
            team1[3] += 1 # +1 loss
            team2[1] += 1 # +1 Win
            team2[4] += 3 # +3 points
        else: # Draw
            team1[2] += 1 # +1 draw
            team1[4] += 1 # +1 point
            team2[2] += 1 # +1 draw
            team2[4] += 1 # +1 point
        # Update ranking of both teams in dictionary
        rk[row[0]] = team1
        rk[row[1]] = team2

    # Secondary sort: first sort alphabetically by Team Name
    ranking = sorted(rk.items())
    # Primary sort: second sort by points descending
    ranking.sort(reverse = True, key = lambda x: x[1][4])

    return rkformat(ranking)

def rkformat(ranking):
    tab_ranking = ["Team                           | MP |  W |  D |  L |  P"]
    for rkrow in ranking:
        tab_occur = f'{rkrow[0]:<31}|{rkrow[1][0]:>3} |{rkrow[1][1]:>3} |{rkrow[1][2]:>3} |{rkrow[1][3]:>3} |{rkrow[1][4]:>3}'
        tab_ranking.append(tab_occur)
    return tab_ranking

# Program tester
#results = [
#            "Courageous Californians;Devastating Donkeys;win",
#            "Allegoric Alaskans;Blithering Badgers;win",
#            "Devastating Donkeys;Allegoric Alaskans;loss",
#            "Courageous Californians;Blithering Badgers;win",
#            "Blithering Badgers;Devastating Donkeys;draw",
#            "Allegoric Alaskans;Courageous Californians;draw",
#        ]
#
#ranking = tally(results)
#print (ranking)

#print ("=> End of program")
