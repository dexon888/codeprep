def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        buy = prices[0]
        maxProfit = float('-inf')
        for price in prices:
            buy = min(buy, price)
            maxProfit= max(maxProfit, price - buy)
        return maxProfit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))