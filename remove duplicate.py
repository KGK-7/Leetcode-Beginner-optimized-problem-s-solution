from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=1
        for right in range(1,len(nums)):
            if nums[right]!=nums[right-1]:
                nums[left]=nums[right]
                left+=1
        return left

print(Solution().removeDuplicates([1,1,2]))  # Output: 2    
# The function returns the length of the array after removing duplicates
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # Output: 5