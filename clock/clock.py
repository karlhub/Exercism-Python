class Clock:
    def __init__(self, hour = 0, minute = 0):
        hh, self.minute = divmod (int(minute), 60)
        dd, self.hour = divmod (hh + int(hour), 24)

    def __repr__(self):
# Python __repr__() function returns the object representation
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + int(minutes))

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - int(minutes))

# Program tester
#while True:
#    hour = input ("Hour: ")
#    minute = input ("Minute: ")
#    if hour == "done":
#        break
#    print ("Clock: ", Clock(hour, minute))
#
#print ("=> End of program")
