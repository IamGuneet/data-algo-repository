class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_prof = 0
        start,sell = 0,1

        while sell < len(prices):
            if prices[sell] > prices[start]:
                max_prof = max(max_prof,(prices[sell]-prices[start]))
            else: 
                start = sell
            sell += 1

        return max_prof
        