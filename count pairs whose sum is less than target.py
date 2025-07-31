from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        left , right = 0 , len(nums)-1

        while left < right:
            if nums[left] + nums[right] < target:
                res += right -left
                left += 1
            else:
                right -=1
        
        return res

s=Solution()
print(s.countPairs([1,2,3,4], 5))  # Example usage
