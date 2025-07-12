class Solution:
    def titleToNumber(columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result

s= Solution()
print(s.titleToNumber("A"))  # Output: 1
print(s.titleToNumber("Z"))  # Output: 26
print(s.titleToNumber("AA")) # Output: 27
        

