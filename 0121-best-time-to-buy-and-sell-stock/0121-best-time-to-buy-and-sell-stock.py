class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        The general idea to buy low and sell high.

        profit = sell - buy

        define two pointers - one will be on an left element while the one loop through the rest of the element
        At each element, we compute the profit and update the maximum profit
        """  

        # setting the variables
        n = len(prices)

        buy = float('inf')

        maxProfit = 0

        for i in range(n):
            if prices[i] < buy:
                buy = prices[i]
            
            profit = prices[i] - buy

            maxProfit = max(profit, maxProfit)
        
        return maxProfit


