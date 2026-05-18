"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""

prices = [2,1,2,1,0,1,2]

def maxProfit(prices):
	start = 0
	maxP = 0
	for end in range(len(prices)):
		print(start, end)
		if prices[end]<prices[start]:
			start=end
		curr = prices[end]-prices[start]
		maxP = maxP if maxP>curr else curr
	return maxP
	
print(maxProfit(prices))