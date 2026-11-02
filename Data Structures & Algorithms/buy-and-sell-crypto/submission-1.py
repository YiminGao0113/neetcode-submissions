class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # This can be done with two pointers as well
        # Pointers is not limited to one step only...

        res = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                margin = prices[r] - prices[l]
                res = max(margin, res)
            else:
                l = r
            r += 1
        
        return res