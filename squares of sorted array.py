from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left,right=0,n-1
        result=[0]*n
        pos=n-1

        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result[pos]=nums[left]**2
                left+=1
            else:
                result[pos]=nums[right]**2
                right-=1
            pos-=1
        return result

sol=Solution()
# Example usage:
nums = [-4, -1, 0, 3, 10]
print(sol.sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]
