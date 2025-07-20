class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev_words = []
        for w in words:
            rev_words.append(w[::-1])
        
        return ' '.join(rev_words)

s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))  # Output: "s'teL ekat edoC teeL tsetnoc"
print(s.reverseWords("God Ding"))  # Output: "doG gniD"