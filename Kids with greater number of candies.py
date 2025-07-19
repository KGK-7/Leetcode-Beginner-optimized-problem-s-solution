from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result

s=Solution()
# Example usage:
print(s.kidsWithCandies([2,3,5,1,3], 3))  # Output: [True, True, True, False, True]
print(s.kidsWithCandies([4,2,1,1,2], 1))  # Output: [True, False, False, False, False]
