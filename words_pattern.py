class Solution(object):
    def wordPattern(self, pattern, s):
        s_words=s.split()
        if len(pattern)!=len(s_words):
            return False
        wordMap = {}
        mappedWords = set()

        for ch , w in zip(pattern , s_words):
            if ch in wordMap:
                if wordMap[ch] != w:
                    return False
            else:
                if w in mappedWords:
                    return False
                wordMap[ch] = w
                mappedWords.add(w)
        
        return True

sol=Solution()
print(sol.wordPattern("abba", "dog cat cat dog"))  # True
print(sol.wordPattern("abba", "dog cat cat fish"))  # False
print(sol.wordPattern("aaaa", "dog cat cat dog"))  # False
print(sol.wordPattern("abba", "dog dog dog dog"))  # False