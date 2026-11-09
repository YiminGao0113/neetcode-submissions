class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        currP = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else: 
                currP = prices[r] - prices[l]
                maxP = max(currP, maxP)
            r += 1
        
        return maxP