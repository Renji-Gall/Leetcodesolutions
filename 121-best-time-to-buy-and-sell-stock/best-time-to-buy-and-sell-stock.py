class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        maxval = 0
        while r < len(prices):
            if prices[l] <= prices[r]:
                maxval = max(maxval, prices[r] - prices[l])
            
            while prices[l] > prices[r]:
                l += 1
            
            r += 1
        return maxval