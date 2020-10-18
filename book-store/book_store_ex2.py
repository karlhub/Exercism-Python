from collections import Counter
from typing import List


def total(basket: List[int]) -> int:
    groups = count_groups(basket)
    groups = adjust_groups(groups)
    return calculate(groups)


def count_groups(basket: List[int]) -> List[int]:
    """ return books counts per group """
    book_counter, groups = Counter(basket), []
    while len(book_counter) > 0:
        groups.append(len(book_counter))
        book_counter.subtract(book_counter.keys())
        book_counter = Counter(book_counter.elements())
    return groups


def adjust_groups(groups: List[int]) -> List[int]:
    """ change [3, 5] to [4, 4] for more discount """
    while (3 in groups) and (5 in groups):
        groups.remove(3)
        groups.remove(5)
        groups += [4, 4]
    return groups


def calculate(groups: List[int]) -> int:
    """ calculate total price with group discout """
    discount_map = {
        1: 800,
        2: (800 * 2) * 0.95,
        3: (800 * 3) * 0.90,
        4: (800 * 4) * 0.80,
        5: (800 * 5) * 0.75,
    }
    sum_price = sum([discount_map[books_count] for books_count in groups])
    return int(sum_price)

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
