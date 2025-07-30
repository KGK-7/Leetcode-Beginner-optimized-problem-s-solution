from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i , w in enumerate(words):
            if w.count(x):
                res.append(i)
        return res

s=Solution()
# Example usage:
words = ["hello", "world", "python", "programming"] 
x = "o"
print(s.findWordsContaining(words, x))  # Output: [0, 1]
