from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result =[folder[0]]

        for i in folder[1:]:
            if not i.startswith(result[-1] + "/"):
                result.append(i)
        
        return result

s=Solution()
# Example usage:
print(s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))  # Output: ["/a", "/c/d", "/c/f"]
print(s.removeSubfolders(["/a/b/c","/a/b/d","/a/b/e"]))  # Output: ["/a/b/c", "/a/b/d", "/a/b/e"]
