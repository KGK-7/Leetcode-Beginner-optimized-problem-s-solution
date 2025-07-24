class Solution(object):
    def heightChecker(self, heights):
        count = 0
        expected = sorted(heights)
        n = len(heights)
        for i in range(n):
            if heights[i] != expected[i]:
                count += 1
        return count

# Example usage:
s= Solution()
print(s.heightChecker([1,1,4,2,1,3]))  # Output: 3
print(s.heightChecker([5,1,2,3,4]))    # Output: 5
print(s.heightChecker([1,2,3,4,5]))    # Output: 0