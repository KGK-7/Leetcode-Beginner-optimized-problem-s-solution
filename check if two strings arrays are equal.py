class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        w1 = ""
        w2 = ""
        for word in word1:
            w1 += word
        for word in word2:
            w2 += word
        
        return w1 == w2

s = Solution()
# Example usage:
print(s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
# Example usage:
print(s.arrayStringsAreEqual(["a", "b"], ["ab"]))