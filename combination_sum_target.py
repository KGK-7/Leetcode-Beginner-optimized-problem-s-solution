from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []  

        def backtrack(start_index: int, current_combination: List[int], current_sum: int):
            if current_sum == target:
                result.append(current_combination[:]) 
                return
            
            if current_sum > target:
                return

            for i in range(start_index, len(candidates)):
                num = candidates[i]
                
                current_combination.append(num)

                backtrack(i, current_combination, current_sum + num)

                current_combination.pop()

        backtrack(0, [], 0)
        return result

# Example usage
candidates = [2, 3, 6, 7]
target = 7
solution = Solution()
print(solution.combinationSum(candidates, target))  # Output: [[2, 2, 3], [7]]
# Example usage
print(solution.combinationSum([2, 3, 5], 8))  # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]