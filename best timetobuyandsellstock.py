def max_profit(prices):

    minimum_price = prices[0]
    maximum_profit = 0

    for price in prices:

        if price < minimum_price:
            minimum_price = price

        profit = price - minimum_price

        if profit > maximum_profit:
            maximum_profit = profit

    return maximum_profit


prices = [7, 1, 5, 3, 6, 4]

print(max_profit(prices))