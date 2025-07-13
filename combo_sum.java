class Solution {
    private int[] candidates;
    private int target;
    private List<List<Integer>> result;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        this.candidates = candidates;
        this.target = target;
        this.result = new ArrayList<>();

        backtrack(0, new ArrayList<>(), 0);
        return result;
    }

    private void backtrack(int start, List<Integer> currentCombo, int currentSum) {
        if (currentSum == target) {
            result.add(new ArrayList<>(currentCombo));
            return;
        }

        if (currentSum > target) return;

        for (int i = start; i < candidates.length; i++) {
            currentCombo.add(candidates[i]);
            backtrack(i, currentCombo, currentSum + candidates[i]);
            currentCombo.remove(currentCombo.size() - 1);
        }
    }
}

