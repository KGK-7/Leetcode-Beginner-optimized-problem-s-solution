class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for ch in s:
            if len(result) >=2 and result[-1] == ch and result[-2] == ch:
                continue
            result.append(ch)
        return ''.join(result)

s= Solution()
print(s.makeFancyString("leeetcode"))  # Output: "leetcode"
print(s.makeFancyString("aaabaaaa"))  # Output: "aabaa"
print(s.makeFancyString("aab"))       # Output: "aab"
print(s.makeFancyString("aaa"))       # Output: "aa"