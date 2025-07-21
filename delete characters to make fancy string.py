from itertools import groupby

class Solution(object):
    def makeFancyString(self, s):
        result = []
        for ch, group in groupby(s):
            group_list = list(group)
            result.extend(group_list[:2])
        return ''.join(result)

s=Solution()
# Example usage
print(s.makeFancyString("leeetcode"))  # Output: "leetcode"
print(s.makeFancyString("aaabaaaa"))   # Output: "aabaa"
print(s.makeFancyString("aab"))        # Output: "aab"
