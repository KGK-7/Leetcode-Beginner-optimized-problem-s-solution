from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left <= right:
            mid=left+(right-left) //2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left+=1
            else:
                right-=1
        
        return -1

sol=Solution()
# Example usage:
print(sol.search([1, 2, 3, 4, 5], 3))  # Output: 2
print(sol.search([1, 2, 3, 4, 5], 6))  # Output: -1

# This code defines a class Solution with a method search that implements binary search.
# The method takes a sorted list of integers and a target integer as input,
# and returns the index of the target if found, or -1 if not found.
# The binary search algorithm works by repeatedly dividing the search interval in half,
# checking if the middle element is equal to the target, and adjusting the search boundaries accordingly.
# The time complexity of this implementation is O(log n), where n is the number of elements in the list.
# The space complexity is O(1) since it uses a constant amount of space for variables.
# The code is efficient and concise, leveraging the properties of binary search to quickly find the target element.
