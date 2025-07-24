from typing import List
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            n = len(row)
            for i in range( (n + 1)// 2 ):
                row[i] , row[n-1-i] = 1 - row[n-1-i] , 1- row[i]
        
        return image

s= Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))  # Output: [[1,0,0],[0,1,0],[1,1,1]]
print(s.flipAndInvertImage([[1,1,0],[1,1,0],[0,0,0]]))  # Output: [[1,0,0],[1,0,0],[1,1,1]]      