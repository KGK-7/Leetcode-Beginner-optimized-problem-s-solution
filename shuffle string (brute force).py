class Solution(object):
    def restoreString(self, s, indices):
        n = len(s)
        res = [""] * n

        for i in range(n):
            res[indices[i]] = s[i]
        
        return "".join(res)

# Example usage:
s = Solution()
print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3]))  # Output: "leetcode"
print(s.restoreString("abc", [0,1,2]))  # Output: "abc"
print(s.restoreString("aiohn", [3,1,4,2,0]))  # Output: "nihao"
print(s.restoreString("a", [0]))  # Output: "a"
