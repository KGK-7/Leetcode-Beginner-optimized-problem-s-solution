class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            row.reverse()
            n = len(row)
            for i in range(n):
                row[i] = 1- row[i]
        return image

s= Solution()
# Example usage:
image = [[1,1,0],[1,0,1],[0,0,1]]
print(s.flipAndInvertImage(image))  # Output: [[1,0,0],[0,1,0],[1,1,0]]
# Example usage:
# image = [[1,0,0],[0,1,0],[1,1,0]]
# print(s.flipAndInvertImage(image))  # Output: [[0,1,1],[0,1,0],[0,0,1]]