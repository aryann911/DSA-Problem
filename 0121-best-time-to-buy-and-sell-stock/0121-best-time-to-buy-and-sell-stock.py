class Solution(object):
    def maxProfit(self, prices):
        min_=float('inf')
        max_=0
        for i in range(0,len(prices)):
            min_=min(min_,prices[i])
            max_=max(max_,prices[i]-min_)

        return max_
        