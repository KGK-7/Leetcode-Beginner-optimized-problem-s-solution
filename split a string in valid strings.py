class Solution(object):
    def balancedStringSplit(self, s):
        bal , count = 0, 0
        for ch in s:
            if ch == "R":
                bal += 1
            else:
                bal -= 1
            
            if bal == 0:
                count +=1
        return count

s=Solution()
print(s.balancedStringSplit("RLRRLLRLRL"))  # Output: 4
print(s.balancedStringSplit("RLLLLRRRLR"))  # Output: 3
print(s.balancedStringSplit("LLLLRRRR"))    # Output: 1 