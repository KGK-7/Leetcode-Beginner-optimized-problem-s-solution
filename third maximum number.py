from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first=second=third=None
        for n in nums:
            if n==first or n==second or n==third:
                continue
            if first is None or n>first:
                third=second
                second=first
                first=n
            elif second is None or n>second:
                third=second
                second=n
            elif third is None or n>third:
                third=n
        return third if third is not None else first

sol=Solution()
sol.thirdMax([3, 2, 1])  # Output: 1
sol.thirdMax([1, 2])      # Output: 2
sol.thirdMax([2, 2, 3, 1])  # Output: 1
