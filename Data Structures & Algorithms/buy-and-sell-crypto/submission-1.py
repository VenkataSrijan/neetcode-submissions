class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        MaxProfit = 0
        while j<len(prices):
            if prices[i]>prices[j]:
                i=j
                j+=1
            else:
                profit = prices[j] - prices[i]
                MaxProfit = max(MaxProfit, profit)
                j+=1


        return MaxProfit