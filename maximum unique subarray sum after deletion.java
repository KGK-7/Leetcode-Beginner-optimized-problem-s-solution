class Solution {
    public int maxSum(int[] nums) {
        boolean allNegative = true;
        int maxValue = Integer.MIN_VALUE;
        for ( int n : nums){
            if ( n >= 0){
            allNegative = false;
        }
            if (n > maxValue){
                maxValue = n;
            }
        }
        if (allNegative){
            return maxValue;
        }
        HashSet<Integer> unique_num = new HashSet<>();
        for ( int n : nums){
            unique_num.add(n);
        }
        int sum = 0;
        for( int num : unique_num ){
            if (num > 0){
                sum += num;
            }
        }
        return sum;
    }
}