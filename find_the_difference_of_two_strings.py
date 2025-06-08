class Solution(object):
    def findTheDifference(self, s, t):
        count={}

        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        
        for ch in t:
            if ch not in count or count[ch]==0 :
                return ch
            count[ch]-=1

sol=Solution()
print(sol.findTheDifference("abcd", "abcde"))  # Output: "e"
print(sol.findTheDifference("a", "aa"))  # Output: "a"
print(sol.findTheDifference("", "y"))  # Output: "y"