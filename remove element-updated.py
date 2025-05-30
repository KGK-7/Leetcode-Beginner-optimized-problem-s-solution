from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[k]=nums[i]
                k+=1
        return k

sol=Solution()
# Example usage:
nums = [3, 2, 2, 3]
val = 3
result = sol.removeElement(nums, val)
print(result)  # Output: 2
# Time Complexity: O(n)
# Space Complexity: O(1)
# where n is the number of elements in the input list nums.
# The function iterates through the list once, checking each element.
# The space complexity is O(1) because we are not using any additional data structures that grow with the input size.
