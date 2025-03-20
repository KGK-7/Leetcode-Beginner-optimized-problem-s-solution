from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        MyDict={}
        for i, n in enumerate(nums):
            diff=target-n
            if diff in MyDict:
                return [MyDict[diff], i]
            MyDict[n]=i
        