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

# This code defines a class Solution with a method maxProfit that calculates the maximum profit
# from a list of stock prices. The method uses a two-pointer approach to track the buy and sell indices.
# It iterates through the prices, updating the buy index when a lower price is found,
# and calculating the profit when a higher price is encountered. The maximum profit is updated accordingly.
# The time complexity of this implementation is O(n), where n is the number of prices,
# and the space complexity is O(1) since it uses a constant amount of space for variables.
# The code is efficient and straightforward, leveraging a single pass through the list to determine the maximum profit.