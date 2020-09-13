class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def _luhn(self,i,dig):
        if i % 2 != 0:
            dig *= 2
            if dig > 9:
                dig -= 9
        return (dig)

    def valid(self):
        # Remove spaces and reverse card number.
        clean_card_num = self.card_num.replace(" ","")[::-1]

        # If lenght <= 1 return "Not Valid".
        if len(clean_card_num) <= 1:
            return False

        # In case of other special characters return "Not Valid".
        if clean_card_num.isnumeric() == False:
            return False

        check_sum = sum(self._luhn(i,int(digit)) for i, digit in enumerate(clean_card_num))

        # If the sum is evenly divisible by 10, then the number is valid
        if check_sum % 10 != 0:
            return False

        return True

# Program tester
#while True:
#    card_num = input ("Card Number: ")
#    if card_num == "done":
#        break
#    luhn_card_num = Luhn(card_num)
#    print ("Luhn: ", luhn_card_num.luhn)
#    print ("Valid? ", luhn_card_num.valid())

#print ("=> End of program")
