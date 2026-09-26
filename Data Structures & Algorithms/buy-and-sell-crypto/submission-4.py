class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_prof = 0

        for i in range(len(prices)):
            curr = prices[i]
            for j in range(i,len(prices)):
                nex = prices[j]
                if nex > curr:
                    max_prof = max(max_prof,(nex-curr))

        return max_prof
        