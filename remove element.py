from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[k]=nums[i]
                k+=1
        return k

print(Solution().removeElement([3,2,2,3], 3))  # Output: 2
# The function returns the length of the array after removing all instances of val
print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))  # Output: 5
