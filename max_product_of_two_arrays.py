from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1=max2=0
        for n in nums:
            if n > max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n
        
        return (max1-1) * (max2-1)

sol=Solution()
print(sol.maxProduct([3,4,5,2]))  # Example usage

