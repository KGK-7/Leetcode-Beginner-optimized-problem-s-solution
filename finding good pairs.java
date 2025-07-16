class Solution {
    public int numIdenticalPairs(int[] nums) {
        HashMap<Integer , Integer> pairs = new HashMap<>();
        for( int n : nums){
            pairs.put(n, pairs.getOrDefault(n, 0)+1);
        } 
        int tot_good_pairs = 0;

        for( int n : pairs.values()){
            tot_good_pairs += (n*(n-1)) / 2;
        }
        return tot_good_pairs;
    }
}