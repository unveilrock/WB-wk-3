class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maximum = 0
        minimum = prices[0]
        for i in range(len(prices)):
            if prices[i]< minimum:
                minimum = prices[i]
            elif prices[i]-minimum > maximum:
                maximum = prices[i]-minimum
        return maximum
