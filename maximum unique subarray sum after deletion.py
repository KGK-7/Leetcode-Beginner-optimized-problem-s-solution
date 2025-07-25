from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        allNegative = True
        max_val = float('-inf')
        for n in nums:
            if n >= 0:
                allNegative = False
            max_val = max(max_val , n)
        
        if allNegative:
            return max_val

        unique_num = set(nums)
        sum = 0
        for n in unique_num:
            if n > 0:
                sum += n
        return sum

s= Solution()
# Example usage:
print(s.maxSum([1, 2, 3, -1, -2, -3]))  # Output: 6
print(s.maxSum([-1, -2, -3]))  # Output: -1 
print(s.maxSum([0, 0, 0]))  # Output: 0
print(s.maxSum([1, 2, 3, 4, 5]))  # Output: 15  
print(s.maxSum([-1, 0, 1, 2, 3]))  # Output: 6