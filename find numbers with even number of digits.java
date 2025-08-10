class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;

        for(int num : nums){
            int evenCount = 0;
            while(num >0){
                num /= 10;
                evenCount ++;
            }
            if(evenCount % 2 == 0){
                count+=1;
            }
        }
        return count;
    }
}