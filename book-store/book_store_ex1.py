from typing import List
from collections import Counter

BOOK_PRICE = 800
DISCOUNT = [1, 1, 0.95, 0.9, 0.8, 0.75]


def total(basket: List[int]) -> int:
    return int(price_calc(basket))


def price_calc(basket):
    if len(basket) == 0:
        return 0

    different_books = set(basket)
    number_of_books = Counter(basket)

    if len(different_books) == 5 and len(basket) % 4 == 0 and len(basket) <= 20:
        different_books.remove(number_of_books.most_common()[-1][0])

    price = BOOK_PRICE * len(different_books) * DISCOUNT[len(different_books)]

    for item in different_books:
        basket.remove(item)

    return price + price_calc(basket)

# Program tester
basket = []
while True:
    try:
        book = int (input ("Enter Book: "))
    except:
        break
    basket.append(book)

price = total(basket)
print ("Basket price: ", price)

print("=> End of program")
