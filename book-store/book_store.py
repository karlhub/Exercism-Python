from collections import Counter

def total(basket):

    # Constants definition
    price_book = 800.00
    price_group = [0 * price_book * 1.00,
                1 * price_book * 1.00,
                2 * price_book * 0.95,
                3 * price_book * 0.90,
                4 * price_book * 0.80,
                5 * price_book * 0.75]

    # A Counter is a dict subclass for counting hashable objects.
    # In this case, counter_titles will contain the number of books for each title.
    counter_titles = Counter(basket)
    num_books, num_titles = len(basket), len(counter_titles)

    # Initial price is the most expensive one. It will be reduced each time a discount can be applied.
    price_basket = num_books * price_book

    # Iteration from the biggest possible group of different titles to the smallest one.
    # For each group obtained: reduce basket price with the corresponding discount.
    for group_range in range(num_titles, 1, -1):
        # List of tuples (title, #books) with the top group_range titles.
        group = counter_titles.most_common(group_range)
        # Transform list into a Counter of 1 book for each one of the most_common titles, as it must be removed from the iteration loop.
        counter_group = Counter(tit for tit, _ in group)
        # Remove counter_group from iteration loop.
        counter_rest_group = counter_titles - counter_group
        # Convert remaining group into a list for recursive call to function total()
        list_rest_group = list(counter_rest_group.elements())

        price_basket = min(price_basket, price_group[group_range] + total(list_rest_group))

    return price_basket

# Program tester
#basket = []
#while True:
#    try:
#        book = int (input ("Enter Book: "))
#    except:
#        break
#    basket.append(book)

#price = total(basket)
#print ("Basket price: ", price)

#print("=> End of program")
