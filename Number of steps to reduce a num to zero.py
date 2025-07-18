class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        
        return steps

# Example usage:
s= Solution()
print(s.numberOfSteps(14))  # Output: 6
# Example usage:
print(s.numberOfSteps(8))   # Output: 4