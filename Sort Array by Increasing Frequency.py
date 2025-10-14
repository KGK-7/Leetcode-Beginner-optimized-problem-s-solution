class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if freq[nums[i]] > freq[nums[j]]:
                    nums[i], nums[j] = nums[j], nums[i]
                elif freq[nums[i]] == freq[nums[j]] and nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums
        