class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MaxNum=set(nums)
        if len(MaxNum)<3:
            return max(MaxNum)
        MaxNum.remove(max(MaxNum))
        MaxNum.remove(max(MaxNum))
        return max(MaxNum)
        
sol=Solution()
print(sol.thirdMax([3, 2, 1]))  # Output: 1
print(sol.thirdMax([1, 2]))      # Output: 2
print(sol.thirdMax([2, 2, 3, 1]))  # Output: 1
print(sol.thirdMax([1, 2, 2, 3, 4]))  # Output: 2