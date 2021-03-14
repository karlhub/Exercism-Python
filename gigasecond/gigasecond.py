from datetime import datetime
from datetime import timedelta

def add(moment):
    one_giga_sec = 10 ** 9
    return moment + timedelta(0,one_giga_sec)

# Program tester
#while True:
#    year = int(input("Year: "))
#    if year == 0:
#         break
#    month = int(input("Month: "))
#    day = int(input("Day: "))
#    hour = int(input("Hour: "))
#    minute = int(input("Minute: "))
#    print (add(datetime(year,month,day,hour,minute)))

#print("=> End of program")
