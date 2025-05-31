from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left <= right:
            mid=left+(right-left) //2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left+=1
            else:
                right-=1
        
        return -1

sol=Solution()
# Example usage:
print(sol.search([1, 2, 3, 4, 5], 3))  # Output: 2
print(sol.search([1, 2, 3, 4, 5], 6))  # Output: -1

