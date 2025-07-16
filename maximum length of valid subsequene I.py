class Solution(object):
    def maximumLength(self, nums):
        sub = nums[0] % 2
        odd, even, alt = 0,0,0

        for n in nums:
            if n %2 == 0:
                even+=1
            else:
                odd+=1
            
            if n %2 == sub:
                alt+=1
                sub= 1 - sub
        
        return max(odd, even, alt)


s= Solution()
# Example usage:
print(s.maximumLength([1, 2, 3, 4, 5]))
print(s.maximumLength([1, 3, 5, 7]))
print(s.maximumLength([2, 4, 6, 8]))
print(s.maximumLength([1, 2, 3, 4, 5, 6]))
print(s.maximumLength([1,2,1,1,2,1,2]))
