from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return "".join( char for _ , char in sorted(zip(indices , s)))

s=Solution()
# Example usage:
print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3]))  # Output: "leetcode"
print(s.restoreString("abc", [0,1,2]))  # Output: "abc"
print(s.restoreString("aiohn", [3,1,4,2,0]))
# Output: "nihao"