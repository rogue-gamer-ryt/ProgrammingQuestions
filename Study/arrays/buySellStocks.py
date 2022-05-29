# consider the following sequence of stock prices:
# [310,315,275,295,260,270,290,230,255,250]. The maximum profit that can be made with one buy
# and one sell is 30-buy at 260 and sell at 290. Note that 250 is not the lowest price, nor 290 the
# highest price.
# 
# Write a program that takes an array denoting the daily stock price, and returns the maximum profit
# that could be made by buying and then selling one share of that stock. There is no need to buy if
# no profit is possible.

def buy_and_sell_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

print(buy_and_sell_stock_once([310,315,275,295,260,270,290,230,255,250]))

# The max difference problem, introduced on Page 1, formalizes the maximum profit that can be
# made by buying and then selling a single share over a given day range.
# Write a program that computes the maximum profit that can be made by buying and selling a share
# at most twice. The second buy must be made on another date after the first sale.


def buy_and_sell_stock_twice(prices):
    min_price_so_far, max_profit = float('inf'), 0.0

    first_buy_sell_profits = [0 for _ in range(len(prices))]
    
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_profit = max(max_profit, price-min_price_so_far)
        first_buy_sell_profits[i] = max_profit 

    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_profit = max(max_profit, max_price_so_far - price + first_buy_sell_profits[i - 1])

    return max_profit

print(buy_and_sell_stock_twice([12,11,13,9,12,8,14,13,15]))