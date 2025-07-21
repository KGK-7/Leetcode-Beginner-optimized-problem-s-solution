class Solution(object):
    def makeFancyString(self, s):
        count = 0
        prev_char =''
        result = []

        for ch in s:
            if ch == prev_char:
                count +=1
            else:
                prev_char = ch
                count = 1
            
            if count <=2:
                result.append(ch)

        return ''.join(result)

s= Solution()
print(s.makeFancyString("leeetcode"))  # Output: "leetcode"
print(s.makeFancyString("aaabaaaa"))  # Output: "aabaa"
print(s.makeFancyString("aab"))       # Output: "aab"
print(s.makeFancyString("aaa"))       # Output: "aa"