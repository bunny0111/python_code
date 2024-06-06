'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

def max_profit(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update the minimum price if the current price is lower
        if price < min_price:
            min_price = price
        # Calculate the profit if we sell at the current price
        current_profit = price - min_price
        # Update the maximum profit if the current profit is higher
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
result = max_profit(prices)
print(f"The maximum profit is: {result}")  # Output: 5



'''
Example
For the given array prices = [7, 1, 5, 3, 6, 4]:

On day 1 (price = 7), min_price becomes 7.
On day 2 (price = 1), min_price is updated to 1.
On day 3 (price = 5), current_profit is 4 (5 - 1), max_profit is updated to 4.
On day 4 (price = 3), current_profit is 2 (3 - 1), max_profit remains 4.
On day 5 (price = 6), current_profit is 5 (6 - 1), max_profit is updated to 5.
On day 6 (price = 4), current_profit is 3 (4 - 1), max_profit remains 5.
Thus, the maximum profit is 5.
'''