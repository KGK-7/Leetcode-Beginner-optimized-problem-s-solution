class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            result.extend( [nums[i+1]] * nums[i])

        return result 

s = Solution()
print(s.decompressRLElist([1,2,3,4]))  # Output: [2, 4, 4]
print(s.decompressRLElist([1,1,2,3]))  # Output: [1, 3, 3]
print(s.decompressRLElist([2,5,3,1]))  # Output: [5, 5, 1, 1, 1]