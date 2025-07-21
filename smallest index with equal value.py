from typing import List
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i , num in enumerate(nums):
            if i % 10 == num :
                return i
        return -1

s= Solution()
print(s.smallestEqual([0,1,2,3,4,5,6,7,8,9]))
print(s.smallestEqual([4,3,2,1,0,5,6,7,8,9]))
print(s.smallestEqual([1,2,3,4,5,6,7,8,9,0]))
print(s.smallestEqual([2,1,3,4,5,6,7,8,9,0]))