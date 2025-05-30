from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=1
        max_profit=0
        while(sell<len(prices)):
            if(prices[buy]<prices[sell]):
                profit=prices[sell]-prices[buy]
                max_profit=max(max_profit,profit)
            else:
                buy=sell
            sell+=1
        return max_profit


# Example usage:
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))  # Output: 5
print(sol.maxProfit([7,6,4,3,1]))    # Output: 0
