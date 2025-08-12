class Solution {
    public int repeatedNTimes(int[] nums) {
        int maxValue = 10000;
        int count[] = new int[maxValue + 1];

        for(int n : nums){
            count[n]++;
            if(count[n]== 2){
                return n;
            }
        }
        return -1;
    }
}