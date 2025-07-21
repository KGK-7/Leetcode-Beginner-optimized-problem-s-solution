class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        arr = [0] * 26
        count = 0
        for ch in allowed:
            arr[ord(ch) - ord('a')] = 1

        for word in words:
            for ch in word:
                if arr[ ord(ch) - ord('a')] == 0:
                    break
            else:
                count += 1
        return count

s= Solution()
print(s.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
from typing import List
print(s.countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
print(s.countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))
# Example usage:
print(s.countConsistentStrings("xyz", ["x","y","z","xy","xz","yz","xyz"]))
print(s.countConsistentStrings("a", ["b","c","d","e"]))