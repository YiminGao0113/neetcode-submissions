class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Keep a running min and maxProfit
        runMin, maxP = prices[0], 0

        for price in prices:
            maxP = max(maxP, price - runMin)
            runMin = min(runMin, price)
        
        return maxP