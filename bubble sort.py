class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Step 1: Square each number
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        # Step 2: Sort the squared numbers using Bubble Sort
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums

class main:
    def main():
        solution = Solution()
        nums = [-4, -1, 0, 3, 10]
        result = solution.sortedSquares(nums)
        print(result)  # Output: [0, 1, 9, 16, 100]

    if __name__ == "__main__":
        main()
