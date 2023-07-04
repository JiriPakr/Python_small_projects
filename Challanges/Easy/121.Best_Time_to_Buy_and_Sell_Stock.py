"""
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

 
Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104
"""
import sys
##################################################################
def maxProfit(prices) -> int:
    l,r = 0,1 # left -> buy, right -> sell
    maxProfit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
        else:
            l = r
        r += 1
    return maxProfit

##################################################################
# Kadane's Algorithm - Largest Sum Contiguous Subarray
def maxProfit2(prices) -> int:
    if len(prices) == 0:
        return 0
    
    minP = prices[0]
    profit = 0
    for i in range(1,len(prices)):
        profit = max(profit, prices[i]-minP)
        minP = min(minP, prices[i])
    
    return profit

##################################################################
def maxProfit3(prices) -> int:
    maxProfit, minBuy = 0, prices[0]
    for i in range(1,len(prices)):
        minBuy = min(minBuy, prices[i])
        maxProfit = max(maxProfit, prices[i]-minBuy)

    return maxProfit
##################################################################
prices1 = [7,1,5,3,6,4]     # Output: 0
prices2 = [7,6,4,3,1]       # Output: 5

print(maxProfit(prices1))
print(maxProfit(prices2))
print(maxProfit2(prices1))
print(maxProfit2(prices2))
print(maxProfit3(prices1))
print(maxProfit3(prices2))
